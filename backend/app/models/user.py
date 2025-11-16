from pydantic import BaseModel


class User(BaseModel):
    username: str
    email: str | None = None
    message: str


class UserResponse(BaseModel):
    id: int
    username: str
    email: str | None = None

    class Config:
        from_attributes = True