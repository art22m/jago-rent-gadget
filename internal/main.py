from fastapi import FastAPI

from fastapi import FastAPI
from item.router import router as item_router
from user.router import router as user_router

prefix_api = "/api/v1"
app = FastAPI()
app.include_router(item_router, prefix=prefix_api)
app.include_router(user_router, prefix=prefix_api)
