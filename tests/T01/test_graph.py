"""Tests for the base LangGraph factory."""
from langgraph.graph import StateGraph

from uda.graph.base import BaseGraphState, create_base_graph


def test_create_base_graph_returns_state_graph_instance() -> None:
    graph = create_base_graph()

    assert isinstance(graph, StateGraph)
    assert graph.state_schema is BaseGraphState
