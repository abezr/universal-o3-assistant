"""LangGraph graph construction utilities for the Universal Data Assistant."""
from typing import Any

from langgraph.graph import StateGraph


class BaseGraphState(dict[str, Any]):
    """Placeholder state container for the base graph."""


def create_base_graph() -> StateGraph:
    """Return a LangGraph ``StateGraph`` with a minimal dictionary state schema."""
    graph: StateGraph = StateGraph(BaseGraphState)
    return graph
