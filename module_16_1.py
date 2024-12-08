from fastapi import FastAPI, Path, Query

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Главная страница"}

@app.get("/user/admin")
async def admin():
    return {"message": "Вы вошли как администратор"}

@app.get("/user/{user_id}")
async def user_id(user_id: int = Path()):
    return {"message": f"Вы вошли как пользователь № {user_id}"}

@app.get("/user")
async def user(username: str = Query(), age: int = Query()):
    return {"message": f"Информация о пользователе. Имя: {username}, Возраст: {age}"}
