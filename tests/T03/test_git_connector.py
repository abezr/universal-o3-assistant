from __future__ import annotations

import asyncio
from pathlib import Path
from typing import List

from uda.ingest.git import GitConnector
from uda.models import DocChunk


def _create_file(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def _collect(connector: GitConnector) -> List[DocChunk]:
    async def _run() -> List[DocChunk]:
        return [chunk async for chunk in connector.collect()]

    return asyncio.run(_run())


def test_git_connector_collects_text_files(tmp_path: Path) -> None:
    repo = tmp_path / "repo"
    repo.mkdir()
    (repo / ".git").mkdir()
    _create_file(repo / "README.md", "hello")
    _create_file(repo / "src" / "main.py", "print('ok')\n")
    _create_file(repo / "docs" / "guide.txt", "usage guide")

    connector = GitConnector(repo)

    chunks = _collect(connector)

    assert [chunk.metadata["path"] for chunk in chunks] == [
        "README.md",
        "docs/guide.txt",
        "src/main.py",
    ]
    assert all(chunk.source == "git" for chunk in chunks)
    assert all(chunk.text for chunk in chunks)
    assert {chunk.document_id for chunk in chunks} == {
        "repo:README.md",
        "repo:docs/guide.txt",
        "repo:src/main.py",
    }


def test_git_connector_honors_glob_filters(tmp_path: Path) -> None:
    repo = tmp_path / "repo"
    repo.mkdir()
    _create_file(repo / "keep.md", "doc")
    _create_file(repo / "ignore.log", "noise")
    _create_file(repo / "nested" / "keep.py", "print('hi')")

    connector = GitConnector(
        repo,
        include_globs=("*.md", "*.py"),
        exclude_globs=("nested/*",),
    )

    chunks = _collect(connector)

    assert [chunk.metadata["path"] for chunk in chunks] == ["keep.md"]
