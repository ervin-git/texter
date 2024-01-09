from __future__ import annotations

from fastapi.testclient import TestClient
from responses import assert_failure
from responses import assert_successful


def test_distance(client: TestClient) -> None:
    response = client.post(
        "/distance/",
        params={
            "string_1": "a",
            "string_2": "a",
        },
    )
    response_json = assert_successful(response)
    assert response_json == 0


def test_distance_missing_param(client: TestClient) -> None:
    response = client.post(
        "/distance/",
        params={
            "string_1": "a",
        },
    )
    assert_failure(response, 422)


def test_match(client: TestClient) -> None:
    response = client.post(
        "/match/",
        params={
            "string_1": "a",
            "string_2": "a",
        },
    )
    response_json = assert_successful(response)
    assert response_json == 1.0


def test_match_missing_param(client: TestClient) -> None:
    response = client.post(
        "/match/",
        params={
            "string_1": "a",
        },
    )
    assert_failure(response, 422)
