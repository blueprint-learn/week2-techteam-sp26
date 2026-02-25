# FastAPI CRUD Exercise

## API Spec

This project exposes an in-memory CRUD API for users and products.

### Health

- `GET /`
  - Response `200`: `{"message": "Hello World"}`

### Users

- `GET /users`
  - Response `200`: list of user objects.
- `POST /user`
  - Body: `{"_id": int, "name": str, "email": str}`
  - Response `201`: created user object.
- `PUT /user`
  - Body: `{"_id": int, "name": str, "email": str}`
  - Response `200`: updated user object.
  - Response `404`: `{"detail": "User not found"}` when `_id` does not exist.
- `GET /user?prefix=`
  - Response `200`: list of user objects that match prefix on the name.
- `DELETE /user/{id}`
  - Response `200`: `{"message": "User deleted"}`
  - Response `404`: `{"detail": "User not found"}` when `_id` does not exist.

### Products

- `GET /products`
  - Response `200`: list of product objects.
- `POST /product`
  - Body: `{"_id": int, "name": str, "price": float}`
  - Response `201`: created product object.
- `PUT /product`
  - Body: `{"_id": int, "name": str, "price": float}`
  - Response `200`: updated product object.
  - Response `404`: `{"detail": "Product not found"}` when `_id` does not exist.
- `DELETE /product/{id}`
  - Response `200`: `{"message": "Product deleted"}`
  - Response `404`: `{"detail": "Product not found"}` when `_id` does not exist.

The expected behavior is captured in `tests/test_api.py`.

## Run the App

Install dependencies:

### macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Start the API:

```bash
cd app
uvicorn main:app --reload
```

### Windows (PowerShell)

```powershell
py -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

Start the API:

```powershell
cd app
uvicorn main:app --reload
```

## Run Tests

### macOS

```bash
pytest -q
```

### Windows (PowerShell)

```powershell
pytest -q
```
