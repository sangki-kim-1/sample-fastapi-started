from functools import lru_cache
from typing_extensions import Annotated
from fastapi import Depends, FastAPI

from routers import users_router, item_router
import config

app = FastAPI()

app.include_router(users_router.router)
app.include_router(item_router.router)

@lru_cache
def load_settings():
  return config.Settings()

@app.get("/", tags=["index"])
def root():
  return {"message": "Sample FastAPI application"}

@app.get("/about", tags=["about"])
def about(settings: Annotated[config.Settings, Depends(load_settings)]):
  return {
    "app_name": settings.app_name,
    "admin_email": settings.admin_email,
  }