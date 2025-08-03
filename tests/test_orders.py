import pytest
from httpx import AsyncClient
from main import app

@pytest.mark.asyncio
async def test_homepage():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/")
    assert response.status_code == 200
    assert "Order Management System" in response.text

@pytest.mark.asyncio
async def test_list_orders():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/orders")
    assert response.status_code == 200
    assert "Orders" in response.text or "No orders yet" in response.text

@pytest.mark.asyncio
async def test_new_order_page():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/orders/new")
    assert response.status_code == 200
    assert "New Order" in response.text
