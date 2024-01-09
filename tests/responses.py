from __future__ import annotations

import requests


def _detail(response: requests.Response) -> str:
    data: dict = response.json()
    assert "detail" in data, "Response does not contain an error message"
    return data["detail"]


def assert_successful(response: requests.Response) -> dict:
    assert response.status_code == 200, _detail(response)
    return response.json()


def assert_failure(
    response: requests.Response,
    expected_error_code: int,
    expected_error_message: str | None = None,
) -> None:
    assert response.status_code == expected_error_code

    if expected_error_message is not None:
        error_message = _detail(response)
        assert error_message == expected_error_message
