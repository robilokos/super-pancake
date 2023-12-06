from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.security import OAuth2PasswordBearer
from ariadne import gql, QueryType, make_executable_schema, graphql_sync, ObjectType
from ariadne.asgi import GraphQL
from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase
from starlette.middleware.cors import CORSMiddleware
from graphene import ObjectType, Schema, Field, String
from pydantic import BaseModel, ValidationError
from bson import ObjectId
from mongo.db_actions import connect_to_mongo, close_mongo_connection, insert_one, find_all

# TODO: hash user password before storing it in db

app = FastAPI()

# define origins
origins = [
    "http://localhost",
    "http://localhost:8080",
]

# add cors
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI backend!"}


# define GraphQL schema
type_defs = gql("""
    type Query {
        hello: String!
    }
""")

query = QueryType()
query.set_field("hello", lambda *_: "Hello, GraphQL!")

schema = make_executable_schema(type_defs, query)

app.add_route("/graphql", GraphQL(schema, debug=True))


# MongoDB connection
MONGO_URI = "mongodb://mongodb:27017/mydatabase"


@app.on_event("startup")
async def startup_db_client():
    app.mongodb_client = await connect_to_mongo(MONGO_URI)
    app.mongodb = app.mongodb_client.get_database()


@app.on_event("shutdown")
async def shutdown_db_client():
    await close_mongo_connection(app.mongodb_client)


def get_database() -> AsyncIOMotorDatabase:
    return app.mongodb


# account apis
class UserCreate(BaseModel):
    username: str
    password: str


@app.post("/create-account", response_model=dict)
async def create_account(user_data: UserCreate, db: AsyncIOMotorDatabase = Depends(get_database)):
    users_collection = db["users"]
    
    result = await insert_one(users_collection, {
        "username": user_data.username, 
        "password": user_data.password
    })
    
    new_user_id = str(result)
    return {"message": f"Account created. ID: {new_user_id}"}


@app.get("/accounts", response_model=list)
async def list_users(db: AsyncIOMotorDatabase = Depends(get_database)):
    users_collection = db["users"]
    
    users = await find_all(users_collection)
    return users
