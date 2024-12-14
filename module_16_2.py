from fastapi import FastAPI, Path, Annotated
from pydantic import BaseModel, Field

app = FastAPI()

class UserID(BaseModel):
    user_id: int = Field(..., ge=1, le=100, description="Enter User ID", example=1)

class User(BaseModel):
    username: str = Field(..., min_length=5, max_length=20, description="Enter username", example="UrbanUser")
    age: int = Field(..., ge=18, le=120, description="Enter age", example=24)

@app.get("/user/{user_id}", response_model=UserID)
async def get_user(user_id: UserID = Path(...)):
    return user_id

@app.get("/user/{username}/{age}", response_model=User)
async def get_user(username: User = Path(...), age: User = Path(...)):
    return {"username": username, "age": age}
