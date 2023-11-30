# обработчики текстовых сообщений
from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardRemove

from keyboards.menus import main_menu

router = Router()


@router.message(F.text == "77")
async def start_main_menu(message):
    print("router run")
    await message.answer("какая то информация", reply_markup=main_menu())

