from fastapi import FastAPI, Path, Body
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

users = {'1': 'Имя: Example, возраст: 18'}

class User(BaseModel):
    username: str
    age: int

@app.get("/users")
async def get_users():
    return users

@app.post("/user/{username}/{age}", response_model=User)
async def create_user(username: str = Path(...), age: int = Path(...)):
    max_id = max(users.keys())
    new_id = str(int(max_id) + 1)
    users[new_id] = f"Имя: {username}, возраст: {age}"
    return User(username=username, age=age)

@app.put("/user/{user_id}/{username}/{age}", response_model=User)
async def update_user(user_id: str = Path(...), username: str = Path(...), age: int = Path(...)):
    if user_id not in users:
        return {"error": "User not found"}
    users[user_id] = f"Имя: {username}, возраст: {age}"
    return User(username=username, age=age)

@app.delete("/user/{user_id}")
async def delete_user(user_id: str = Path(...)):
    if user_id not in users:
        return {"error": "User not found"}
    del users[user_id]
    return {"success": "User deleted"}
