from fastapi import APIRouter, Depends
from motor.motor_asyncio import AsyncIOMotorDatabase
from mongo.db_actions import insert_one, find_all
from main import get_database
from pydantic import BaseModel

router = APIRouter()


class UserCreate(BaseModel):
    username: str
    password: str


@router.post("/create-account", response_model=dict)
async def create_account(user_data: UserCreate, db: AsyncIOMotorDatabase = Depends(get_database)):
    users_collection = db["users"]
    
    result = await insert_one(users_collection, {
        "username": user_data.username, 
        "password": user_data.password
    })
    
    new_user_id = str(result)
    return {"message": f"Account created. ID: {new_user_id}"}


@router.get("/accounts", response_model=list)
async def list_users(db: AsyncIOMotorDatabase = Depends(get_database)):
    users_collection = db["users"]
    
    users = await find_all(users_collection)
    return users
