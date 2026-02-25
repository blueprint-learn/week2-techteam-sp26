from fastapi import FastAPI
from model import User, Product

app = FastAPI()


db_users = {}
db_products = {}


@app.get("/")
def read_root():
    return {"message": "Hello World"}


@app.get("/users")
def read_users():
    # TODO: return all users from the database
    pass


@app.post("/user")
def create_user():
    # TODO: create a new user in the database
    pass


@app.put("/user")
def update_user():
    # TODO: update an existing user in the database
    pass


@app.get("/user")
def get_all_users_prefix(prefix: str):
    # TODO: return all users from the database that match the given name prefix
    pass


@app.delete("/user")
def delete_user():
    # TODO: delete an existing user from the database
    pass


@app.get("/products")
def read_products():
    # TODO: return all products from the database
    pass


@app.post("/product")
def create_product():
    # TODO: create a new product in the database
    pass


@app.put("/product")
def update_product():
    # TODO: update an existing product in the database
    pass


@app.delete("/product")
def delete_product():
    # TODO: delete an existing product from the database
    pass
