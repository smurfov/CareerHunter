from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class TelegramUserCreate(BaseModel):
    telegram_id: int
    username: Optional[str] = None
    first_name: str
    last_name: Optional[str] = None


class UserResponse(BaseModel):
    id: int
    telegram_id: int
    username: Optional[str] = None
    first_name: str
    last_name: Optional[str] = None
    created_at: datetime

    class Config:
        from_attributes = True
