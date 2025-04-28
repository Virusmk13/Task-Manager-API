from fastapi import FastAPI
from routers import users, tasks
import models
from database import engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Task Manager API",
    description="Un API pentru gestionarea utilizatorilor și taskurilor",
    version="1.0.0"
)

app.include_router(users.router)
app.include_router(tasks.router)

@app.get("/")
def read_root():
    return {"message": "Bun venit la Task Manager API!"}
