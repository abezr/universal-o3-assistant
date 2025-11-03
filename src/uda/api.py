"""FastAPI application exposing the public HTTP API."""
from fastapi import FastAPI

app = FastAPI(title="Universal Data Assistant")


@app.get("/health")
async def health() -> dict[str, str]:
    """Health check endpoint returning a simple status payload."""
    return {"status": "ok"}
