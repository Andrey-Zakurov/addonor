# обработчики текстовых сообщений
from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardRemove

from keyboards.menus import main_menu, menu_replykeyboard

router = Router()


@router.message(F.text == "777")
async def start_main_menu(message):
    print("router run")
    data = {
            "buttons": (
                        "кнопка1",
                        "кнопка2",
                        "кнопка3",
                       ),
            "settings": {
                        "adjust": 1
                        }
        }
    await message.answer("какая то информация", reply_markup=menu_replykeyboard(data))

