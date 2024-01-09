from __future__ import annotations

from collections.abc import Generator

import pytest
from fastapi.testclient import TestClient

from texter.texter import app


@pytest.fixture
def client() -> Generator:
    client = TestClient(app)
    yield client
