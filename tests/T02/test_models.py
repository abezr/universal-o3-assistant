"""Unit tests for the core Pydantic data models."""
from __future__ import annotations

import datetime as dt

import pytest

from uda.models import DocChunk, LLMResponse, RetrievalResult


def test_doc_chunk_defaults() -> None:
    chunk = DocChunk(id="chunk-1", document_id="doc-1", text="Sample text.")

    assert chunk.metadata == {}
    assert chunk.source is None
    assert chunk.text == "Sample text."


def test_doc_chunk_accepts_metadata() -> None:
    chunk = DocChunk(
        id="chunk-2",
        document_id="doc-2",
        text="Another sample",
        source="handbook.md",
        metadata={"section": "Intro", "captured_at": dt.datetime(2024, 1, 1)},
    )

    assert chunk.metadata["section"] == "Intro"
    assert isinstance(chunk.metadata["captured_at"], dt.datetime)


def test_retrieval_result_requires_valid_score() -> None:
    chunk = DocChunk(id="chunk-3", document_id="doc-3", text="Body")

    result = RetrievalResult(query="what is policy?", chunk=chunk, score=0.42)

    assert result.score == pytest.approx(0.42)
    assert result.rank is None


def test_retrieval_result_rejects_out_of_bounds_score() -> None:
    chunk = DocChunk(id="chunk-4", document_id="doc-4", text="Body")

    with pytest.raises(ValueError):
        RetrievalResult(query="bad score", chunk=chunk, score=1.5)


def test_llm_response_defaults_and_optional_payloads() -> None:
    response = LLMResponse(answer="All systems go")

    assert response.citations == []
    assert response.audit_trail == []
    assert response.usage is None
    assert response.metadata == {}
    assert response.raw_model_output is None


def test_llm_response_validates_citations() -> None:
    with pytest.raises(ValueError):
        LLMResponse(answer="Test", citations=[""])

    response = LLMResponse(answer="Valid", citations=["chunk-1", "chunk-2"])
    assert response.citations == ["chunk-1", "chunk-2"]
