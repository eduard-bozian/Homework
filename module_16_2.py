from fastapi import FastAPI, Path
from typing import Annotated
from pydantic import BaseModel, Field

app = FastAPI()

class UserID(BaseModel):
    user_id: int = Field(..., description="Enter User ID", example=1, gt=0, le=100)

class User(BaseModel):
    username: str = Field(..., description="Enter username", example="UrbanUser", min_length=5, max_length=20)
    age: int = Field(..., description="Enter age", example=24, gt=17, le=120)

@app.get("/user/{user_id}", response_model=UserID)
async def get_user(user_id: UserID = Path(...)):
    return user_id

@app.get("/user/{username}/{age}", response_model=User)
async def get_user(username: User.username, age: User.age = Path(...)):
    return User(username=username, age=age)
