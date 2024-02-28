from fastapi import FastAPI
from fastapi.security import OAuth2PasswordBearer
from ariadne import gql, QueryType, make_executable_schema, graphql_sync, ObjectType
from ariadne.asgi import GraphQL
from motor.motor_asyncio import AsyncIOMotorDatabase
from starlette.middleware.cors import CORSMiddleware
from bson import ObjectId
from mongodb.database import database
from apis.account_api import router as account_router

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
@app.on_event("startup")
async def startup_db_client():
    await database.connect()


@app.on_event("shutdown")
async def shutdown_db_client():
    await database.disconnect()


# Add routers to the app
app.include_router(account_router)
