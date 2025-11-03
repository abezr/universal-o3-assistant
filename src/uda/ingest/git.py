"""Git-based ingestion connector implementation."""

from __future__ import annotations

import asyncio
from dataclasses import dataclass
from fnmatch import fnmatch
from pathlib import Path
from typing import AsyncIterator, Iterable, List, Sequence

from ..models import DocChunk
from .base import BaseConnector


@dataclass(slots=True)
class _RepoFile:
    """Lightweight representation of a repository file."""

    absolute_path: Path
    relative_path: Path


class GitConnector(BaseConnector):
    """Simple connector that walks a local Git repository and yields file contents."""

    def __init__(
        self,
        repo_path: Path | str,
        *,
        include_globs: Sequence[str] | None = None,
        exclude_globs: Sequence[str] | None = None,
        encoding: str = "utf-8",
    ) -> None:
        self._root = Path(repo_path).expanduser().resolve()
        if not self._root.is_dir():
            raise ValueError(f"Repository path '{self._root}' does not exist")

        self._include = tuple(include_globs or ())
        self._exclude = tuple(exclude_globs or ())
        self._encoding = encoding

    async def collect(self) -> AsyncIterator[DocChunk]:
        """Yield the contents of each file within the repository tree."""

        files = await asyncio.to_thread(self._discover_files)
        repo_id = self._root.name
        for index, repo_file in enumerate(files):
            text = await asyncio.to_thread(self._read_text, repo_file.absolute_path)
            document_id = f"{repo_id}:{repo_file.relative_path.as_posix()}"
            chunk_id = f"{document_id}#0"
            yield DocChunk(
                id=chunk_id,
                document_id=document_id,
                text=text,
                source="git",
                metadata={
                    "path": repo_file.relative_path.as_posix(),
                    "repository": str(self._root),
                    "sequence": index,
                },
            )

    def _discover_files(self) -> List[_RepoFile]:
        results: List[_RepoFile] = []
        for path in sorted(self._root.rglob("*")):
            if not path.is_file():
                continue

            relative = path.relative_to(self._root)
            if ".git" in relative.parts:
                continue
            if not self._matches(relative):
                continue
            results.append(_RepoFile(absolute_path=path, relative_path=relative))
        return results

    def _matches(self, relative_path: Path) -> bool:
        path_str = relative_path.as_posix()
        if self._include and not self._glob_any(path_str, self._include):
            return False
        if self._exclude and self._glob_any(path_str, self._exclude):
            return False
        return True

    def _glob_any(self, path: str, patterns: Iterable[str]) -> bool:
        return any(fnmatch(path, pattern) for pattern in patterns)

    def _read_text(self, path: Path) -> str:
        return path.read_text(encoding=self._encoding)

