import sys
from pathlib import Path

import pytest
from fastapi.testclient import TestClient

sys.path.append(str(Path(__file__).resolve().parents[1] / "app"))

from app.main import app, db_products, db_users


@pytest.fixture(autouse=True)
def reset_state():
    db_users.clear()
    db_products.clear()
    yield
    db_users.clear()
    db_products.clear()


@pytest.fixture
def client():
    return TestClient(app)


def test_root(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}


def test_read_users_empty(client):
    response = client.get("/users")
    assert response.status_code == 200
    assert response.json() == []


def test_create_user(client):
    payload = {"_id": 1, "name": "Alice", "email": "alice@example.com"}
    response = client.post("/user", json=payload)
    assert response.status_code == 201
    assert response.json() == payload


def test_read_users_after_create(client):
    payload = {"_id": 1, "name": "Alice", "email": "alice@example.com"}
    client.post("/user", json=payload)

    response = client.get("/users")
    assert response.status_code == 200
    assert response.json() == [payload]


def test_update_user(client):
    original = {"_id": 1, "name": "Alice", "email": "alice@example.com"}
    updated = {"_id": 1, "name": "Alice Smith", "email": "alice.smith@example.com"}
    client.post("/user", json=original)

    response = client.put("/user", json=updated)
    assert response.status_code == 200
    assert response.json() == updated


def test_update_user_not_found(client):
    payload = {"_id": 999, "name": "Ghost", "email": "ghost@example.com"}
    response = client.put("/user", json=payload)
    assert response.status_code == 404
    assert response.json() == {"detail": "User not found"}


def test_delete_user(client):
    payload = {"_id": 1, "name": "Alice", "email": "alice@example.com"}
    client.post("/user", json=payload)

    response = client.delete("/user", params={"_id": 1})
    assert response.status_code == 200
    assert response.json() == {"message": "User deleted"}

    users_response = client.get("/users")
    assert users_response.json() == []


def test_delete_user_not_found(client):
    response = client.delete("/user", params={"_id": 999})
    assert response.status_code == 404
    assert response.json() == {"detail": "User not found"}


def test_read_products_empty(client):
    response = client.get("/products")
    assert response.status_code == 200
    assert response.json() == []


def test_create_product(client):
    payload = {"_id": 10, "name": "Keyboard", "price": 89.99}
    response = client.post("/product", json=payload)
    assert response.status_code == 201
    assert response.json() == payload


def test_read_products_after_create(client):
    payload = {"_id": 10, "name": "Keyboard", "price": 89.99}
    client.post("/product", json=payload)

    response = client.get("/products")
    assert response.status_code == 200
    assert response.json() == [payload]


def test_update_product(client):
    original = {"_id": 10, "name": "Keyboard", "price": 89.99}
    updated = {"_id": 10, "name": "Mechanical Keyboard", "price": 119.99}
    client.post("/product", json=original)

    response = client.put("/product", json=updated)
    assert response.status_code == 200
    assert response.json() == updated


def test_update_product_not_found(client):
    payload = {"_id": 777, "name": "Missing", "price": 1.0}
    response = client.put("/product", json=payload)
    assert response.status_code == 404
    assert response.json() == {"detail": "Product not found"}


def test_delete_product(client):
    payload = {"_id": 10, "name": "Keyboard", "price": 89.99}
    client.post("/product", json=payload)

    response = client.delete("/product", params={"_id": 10})
    assert response.status_code == 200
    assert response.json() == {"message": "Product deleted"}

    products_response = client.get("/products")
    assert products_response.json() == []


def test_delete_product_not_found(client):
    response = client.delete("/product", params={"_id": 999})
    assert response.status_code == 404
    assert response.json() == {"detail": "Product not found"}
