from fastapi import FastAPI

from app.api.todo import router as todo_router

app = FastAPI( title="Todo API" )

app.include_router(todo_router)

@app.get("/") 
def home(): 
    return { 
        "message": "FastAPI todo app Running!" 
    }