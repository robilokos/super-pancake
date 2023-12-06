from fastapi import FastAPI
from fastapi.security import OAuth2PasswordBearer
from ariadne import gql, QueryType, make_executable_schema, graphql_sync, ObjectType
from ariadne.asgi import GraphQL
from motor.motor_asyncio import AsyncIOMotorDatabase
from starlette.middleware.cors import CORSMiddleware
from bson import ObjectId
from mongo.db_actions import connect_to_mongo, close_mongo_connection

# TODO: hash user password before storing it in db

app = FastAPI()

# Define origins
origins = [
    "http://localhost",
    "http://localhost:8080",
]

# Add cors
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


# Define GraphQL schema
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


# Add routers to the app
from apis.account_api import router as account_router
app.include_router(account_router)
