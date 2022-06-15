from aiogram import types, Dispatcher
from create_bot import dp, bot
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ParseMode
from database import sqlite_db
import requests
from time import sleep


# Admin id
ADMIN = '555278365'

# Chanel id
CHANNEL_ID = '-1001233690072'


class Form(StatesGroup):
    name = State()


ID = None


class Users(StatesGroup):
    firstname = State()
    phonenumber = State()
    username = None
    user_id = None


@dp.message_handler(commands=['start', 'help'])
async def command_start(message: types.Message):
    chat_id = message.from_user.id
    await bot.send_message(message.from_user.id, "Botimizga Xush kelibsiz!\nMarhamat rasm yuborasizmi?")

    # if chat_id not in [1245752, 5646542, 1254546]:
    #     await Users.firstname.set()
    #     await bot.send_message(chat_id, "Siz ro'yhatdan o'tmagansiz! \nIsmingizni kiriting")





@dp.message_handler(content_types=['photo'])
async def NewPicture(message: types.Message):
    """
    process advertisement picture
    """
    chat_id = message.chat.id
    file_id = pictureName = message.photo[1].file_unique_id

    await message.photo[-1].download(f"download/{pictureName}.jpg")

    response = requests.post(
        'https://api.remove.bg/v1.0/removebg',
        files={'image_file': open(f'download/{file_id}.jpg', 'rb')},
        data={'size': 'auto'},
        headers={'X-Api-Key': 'Pz898jUwEqLfwGbGNzen92cG'},
    )


    await bot.send_message(chat_id,
                           f"✅ Qabul qilindi\n", parse_mode=ParseMode.HTML)
    await message.answer_chat_action('upload_photo')
    sleep(5)

    if response.status_code == requests.codes.ok:
        with open(f"Upload/{pictureName}.jpg", 'wb') as out:
            out.write(response.content)
            await bot.send_photo(chat_id, photo=open(f"Upload/{pictureName}.jpg", 'rb'))
    else:
        print("Error:", response.status_code, response.text)


@dp.message_handler()
async def Listener_messages(message: types.Message):
    await message.answer(f"Xush kelibsiz {message.from_user.first_name}</b>", parse_mode=ParseMode.HTML)


@dp.message_handler(commands=['elonlarim'])
async def showMyAdvertisement(message: types.Message):
    await sqlite_db.show_adv(message)

    # for ret in cur.execute("SELECT * FROM advertisements").fetchall():
    #     await bot.send_media_group()


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'help'])
    dp.register_message_handler(showMyAdvertisement, commands=['elonlarim'])
