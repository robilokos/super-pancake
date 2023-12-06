from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.security import OAuth2PasswordBearer
from ariadne import gql, QueryType, make_executable_schema, graphql_sync, ObjectType
from ariadne.asgi import GraphQL
from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase
from starlette.middleware.cors import CORSMiddleware
from graphene import ObjectType, Schema, Field, String
from pydantic import BaseModel
from bson import ObjectId

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

MONGO_URI = "mongodb://mongodb:27017/mydatabase"

async def get_database():
    client = AsyncIOMotorClient(MONGO_URI)
    db = client.get_database()
    return db

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI backend!"}


class UserCreate(BaseModel):
    username: str
    password: str

@app.post("/create-account", response_model=dict)
async def create_account(user_data: UserCreate, db: AsyncIOMotorDatabase = Depends(get_database)):
    try:
        users_collection = db["users"]
        result = await users_collection.insert_one({
            "username": user_data.username, 
            "password": user_data.password
        })
        new_user_id = str(result.inserted_id)

        return {"message": f"Account created. ID: {new_user_id}"}
    except ValidationError as e:
        raise HTTPException(status_code=422, detail=str(e))

@app.get("/accounts")
async def get_account(db: AsyncIOMotorDatabase = Depends(get_database)):
    users_collection = db["users"]
    users_cursor = users_collection.find({})
    users = [user async for user in users_cursor]

    for user in users:
        user["_id"] = str(user["_id"])
    
    return {"message": users}