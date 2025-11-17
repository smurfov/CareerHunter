from aiogram import Router, types
from aiogram.filters import Command

# from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from core.api import backend_api
from keyboards.main_kb import get_main_keyboard

router = Router()


@router.message(Command("start"))
async def cmd_start(message: types.Message):
    # Регистрируем пользователя в backend
    user_data = await backend_api.register_user(
        telegram_id=message.from_user.id,
        username=message.from_user.username,
        first_name=message.from_user.first_name,
        last_name=message.from_user.last_name,
    )

    if user_data:
        # Создаем клавиатуру с основными кнопками
        keyboard = get_main_keyboard()

        await message.answer(
            f"Привет, {message.from_user.first_name}! 👋\n"
            "Я помогу тебе создать идеальное резюме под любую вакансию.\n"
            "Выбери действие:",
            reply_markup=keyboard,
        )
    else:
        await message.answer(
            "❌ Произошла ошибка при подключении к сервису.\n" "Попробуйте позже."
        )
