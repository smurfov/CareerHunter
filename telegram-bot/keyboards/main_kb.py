from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    KeyboardButton,
    ReplyKeyboardMarkup,
)


def get_main_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Создать резюме")],
            [KeyboardButton(text="Мои резюме")],
            [KeyboardButton(text="Тарифы")],
            [KeyboardButton(text="Профиль")],
            [KeyboardButton(text="Помощь")],
        ],
        resize_keyboard=True,
    )


def get_cancel_keyboard():
    return InlineKeyboardMarkup(inline_keyboard=[InlineKeyboardButton(text="Отмена")])
