from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.security import OAuth2PasswordBearer
from fastapi.middleware.graphql import GraphQLApp
from motor.motor_asyncio import AsyncIOMotorClient
from starlette.middleware.cors import CORSMiddleware
from graphene import ObjectType, Schema, Field, String

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

class Query(ObjectType):
    hello = String(name=String(default_value="World"))

    async def resolve_hello(root, info, name):
        return f"Hello, {name}!"

schema = Schema(query=Query)

app.add_route("/graphql", GraphQLApp(schema=schema))

MONGO_URI = "mongodb://localhost:27017"
DATABASE_NAME = "mydatabase"

async def get_database():
    client = AsyncIOMotorClient(MONGO_URI)
    db = client(DATABASE_NAME)
    return db

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI backend!"}
