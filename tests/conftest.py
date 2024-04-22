from typing import AsyncGenerator

import pytest_asyncio
from async_asgi_testclient import TestClient

from src.main import app


@pytest_asyncio.fixture
async def client() -> AsyncGenerator[TestClient, None]:
    host, port = "127.0.0.1", "9000"
    scope = {"client": (host, port)}

    async with TestClient(app, scope=scope) as client:
        yield client
