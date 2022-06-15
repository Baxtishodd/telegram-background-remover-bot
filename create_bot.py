from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

import os

# bot = Bot(token=os.getenv('TOKEN'))
bot = Bot('5143413292:AAH5DmiYQ5I2vFOmir16SVKyxI4NSvzEAyw')

storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

# https://api.telegram.org/bot5099386865:AAHgg8Rug1s-CVi7dcdTqulbMfxSd9yviRQ/getMe

