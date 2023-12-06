from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase
from fastapi import Depends
from os import environ


class Database:
    def __init__(self, uri: str):
        self.client = None
        self.db = None
        self.uri = uri

    async def connect(self):
        self.client = AsyncIOMotorClient(self.uri)
        self.db = self.client.get_database()

    async def disconnect(self):
        if self.client:
            self.client.close()

    def get_database(self) -> AsyncIOMotorDatabase:
        return self.db


MONGO_URI = environ.get("MONGO_URI", "mongodb://mongodb:27017/mydatabase")
database = Database(MONGO_URI)