
# основной скрипт, запускающий приложение, в нем реализована логика
# подключения к базе данных, запуск поллинга телеграм и организация
# взаимодействия модулей программы
import sqlite3
import asyncio
import logging
# импорты модулей aiogram
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
#-----------модули приложения---------------
# функции работы с базой находятся в модуле dbase
from dbase import data_object as DB
# получение конфигурационных данных
from config import token, token_dev
# роутеры
from handlers import test, text
# клавиатуры
from keyboards import menus, dialogs


# настройка логирования
logging.basicConfig(level=logging.INFO, filename="py_log.log", filemode="w")


# инициализация
async def main():
    print("Test from develop")
    bot = Bot(token_dev)
    dp = Dispatcher()
    dp.include_router(test.router)
    dp.include_router(text.router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())

