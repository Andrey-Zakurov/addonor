# клавиатуры менюшек
from aiogram.types import ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder


def main_menu() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    kb.button(text="да")
    kb.button(text="нет")
    kb.adjust(2)
    return kb.as_markup(resize_keyboard=True)

