from fastapi import APIRouter

router = APIRouter()

@router.post("/resumes")
async def resumes_post():
	return {"message": "I got ur resume!"}


@router.get("/users/{id}/resumes")
async def resumes_get(id: int):
	return {"message": "There are ur resumes!"}