"""Core Pydantic data contracts used across the Universal Data Assistant."""
from __future__ import annotations

from typing import Any, Dict, List, Optional

from pydantic import BaseModel, ConfigDict, Field, field_validator


class DocChunk(BaseModel):
    """Represents a normalized slice of source documentation."""

    id: str = Field(..., description="Unique identifier for the chunk")
    document_id: str = Field(..., description="Identifier of the parent document")
    text: str = Field(..., description="Content for this chunk")
    source: Optional[str] = Field(
        default=None, description="Human-friendly descriptor of the chunk origin"
    )
    metadata: Dict[str, Any] = Field(
        default_factory=dict,
        description="Arbitrary metadata such as headings, file paths, etc.",
    )

    model_config = ConfigDict(arbitrary_types_allowed=True)


class RetrievalResult(BaseModel):
    """Container describing a vector store retrieval hit."""

    query: str = Field(..., description="Original query text driving retrieval")
    chunk: DocChunk = Field(..., description="Chunk that matched the query")
    score: float = Field(..., description="Similarity score from the vector store")
    rank: Optional[int] = Field(
        default=None, description="Optional rank for deterministic ordering"
    )
    metadata: Dict[str, Any] = Field(
        default_factory=dict,
        description="Additional information from the vector store backend",
    )

    @field_validator("score")
    @classmethod
    def _validate_score(cls, value: float) -> float:
        if not 0.0 <= value <= 1.0:
            raise ValueError("score must be between 0 and 1 inclusive")
        return value


class LLMResponse(BaseModel):
    """Structured response emitted by the synthesis and auditing stages."""

    answer: str = Field(..., description="Natural language answer returned to the user")
    citations: List[str] = Field(
        default_factory=list,
        description="Ordered list of chunk identifiers backing the answer",
    )
    audit_trail: List[Dict[str, Any]] = Field(
        default_factory=list,
        description="Chronological list of audit events for the response",
    )
    usage: Optional[Dict[str, Any]] = Field(
        default=None,
        description="Token usage statistics or model-specific billing information",
    )
    metadata: Dict[str, Any] = Field(
        default_factory=dict,
        description="Auxiliary data associated with the response",
    )
    raw_model_output: Optional[Dict[str, Any]] = Field(
        default=None,
        description="Raw LLM response payload for downstream inspection",
    )

    @field_validator("citations", mode="after")
    @classmethod
    def _validate_citations(cls, value: List[str]) -> List[str]:
        for item in value:
            if not isinstance(item, str) or not item:
                raise ValueError("citation identifiers must be non-empty strings")
        return value
