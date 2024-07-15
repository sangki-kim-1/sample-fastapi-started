from fastapi import APIRouter

router = APIRouter(
  prefix="/users",
  tags=["users"],
  responses={404: {"description": "Not found"}},
)

@router.get("/", tags=["users"])
def find_users():
  return [{"username": "Rick"}, {"username": "Morty"}]

@router.get("/me", tags=["users"])
def find_me():
  return {"username": "Me"}

@router.get("/{username}", tags=["users"])
def find_user_by_user_name(username: str):
  return {"username": username}