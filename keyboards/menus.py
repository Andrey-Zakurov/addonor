# клавиатуры менюшек
from aiogram.types import ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder


def main_menu() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    kb.button(text="да")
    kb.button(text="нет")
    kb.adjust(2)
    return kb.as_markup(resize_keyboard=True)


# генерация меню
def menu_replykeyboard(data: dict) -> ReplyKeyboardMarkup:
    """
    example data:
        {
            "buttons": (
                        "кнопка1",
                        ...
                       ),
            "settings": {
                        "adjust": 1
                        }
        }
    """
    kb = ReplyKeyboardBuilder()
    for text_button in data["buttons"]:
        kb.button(text=text_button)
    print("ok")
    kb.adjust(data["settings"]["adjust"])
    print(dir(kb))
    return kb.as_markup(resize_keyboard=True)
