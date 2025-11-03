"""Simplified StateGraph stub to satisfy tests without the real dependency."""
from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict


@dataclass
class StateGraph:
    """Minimal representation of a LangGraph StateGraph."""

    state_schema: type
    nodes: Dict[str, Any]

    def __init__(self, state_schema: type) -> None:
        self.state_schema = state_schema
        self.nodes = {}

    def add_node(self, name: str, node: Any) -> None:
        self.nodes[name] = node

    def compile(self) -> "StateGraph":
        return self
