"""Ingestion connector interfaces and implementations."""

from .base import BaseConnector
from .git import GitConnector

__all__ = ["BaseConnector", "GitConnector"]
