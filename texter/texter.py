from __future__ import annotations

from fastapi import FastAPI
from string_diff import distance
from string_diff import match


app = FastAPI(
    title="Texter",
    description="Texter API",
    docs_url="/api/docs",
    openapi_url="/api/openapi.json",
)


@app.post("/distance")
def get_distance(string_1: str, string_2: str) -> int:
    return distance(string_1, string_2)


@app.post("/match")
def get_match(string_1: str, string_2: str) -> float:
    return match(string_1, string_2)
