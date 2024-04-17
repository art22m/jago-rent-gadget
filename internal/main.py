from fastapi import FastAPI

from fastapi import FastAPI
from .item.router import router as item_router
from .user.router import router as user_router

app = FastAPI()
app.include_router(item_router)
app.include_router(user_router)
