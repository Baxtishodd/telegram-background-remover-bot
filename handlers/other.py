from aiogram import types, Dispatcher
from create_bot import dp, bot
from keyboards import client_kb


@dp.message_handler(commands=['feedback'])
async def command_start(message : types.Message):
    try:
        await bot.send_message(message.from_user.id, "Xush kelibsiz bizning botga!", reply_markup=client_kb)
        await message.delete()
    except:
        await message.reply("Murojaat uchun @adminga yozing!")

def register_handlers_other(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=['feedback'])

