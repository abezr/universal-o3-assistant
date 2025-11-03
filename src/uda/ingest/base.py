"""Base abstractions for ingestion connectors."""
from __future__ import annotations

from abc import ABC, abstractmethod
from typing import AsyncIterator

from ..models import DocChunk


class BaseConnector(ABC):
    """Common interface every ingestion connector must implement."""

    @abstractmethod
    async def collect(self) -> AsyncIterator[DocChunk]:
        """Yield ``DocChunk`` instances from the backing data source."""

