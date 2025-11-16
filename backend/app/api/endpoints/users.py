from fastapi import APIRouter

router = APIRouter()

@router.post("/users/register")
async def users_register():
	return {"message": "U are registered!"}


@router.post("/users/login")
async def users_login():
	return {"message": "U login in!"}


@router.get("/users/me")
async def users_me():
	return {"message": "Oh, Hello. It's u!"}