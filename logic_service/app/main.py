from fastapi import FastAPI
from .routers import ai

app = FastAPI()

app.include_router(ai.router, prefix="/api/ai")