from app.database.database import get_db
from app.models.user import User
from app.schemas.schemas import TelegramUserCreate, UserResponse
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

router = APIRouter()


@router.post("/auth/telegram", response_model=UserResponse)
async def register_telegram_user(
    user_data: TelegramUserCreate, db: Session = Depends(get_db)
):
    db_user = db.query(User).filter(User.telegram_id == user_data.telegram_id).first()

    if db_user:
        db_user.username = user_data.username
        db_user.first_name = user_data.first_name
        db_user.last_name = user_data.last_name
    else:
        db_user = User(
            telegram_id=user_data.telegram_id,
            username=user_data.username,
            first_name=user_data.first_name,
            last_name=user_data.last_name,
        )
        db.add(db_user)

    db.commit()
    db.refresh(db_user)
    return db_user
