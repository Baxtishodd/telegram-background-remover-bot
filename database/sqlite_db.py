import sqlite3 as sq
from create_bot import dp, bot
from aiogram import types, Dispatcher


def sql_start():
    global base, cur
    base = sq.connect('users_table.db')
    cur = base.cursor()
    if base:
        print("Data base connected OK!")
        base.execute('CREATE TABLE IF NOT EXISTS users(firstname TEXT, username TEXT, user_id TEXT PRIMARY KEY, '
                     'phone TEXT)')
        base.execute('CREATE TABLE IF NOT EXISTS advertisements(photo_id TEXT, caption TEXT, user_id TEXT PRIMARY KEY)')
        base.commit()


async def sql_add_user(state):
    async with state.proxy() as data:
        cur.execute(f'INSERT INTO users VALUES (?, ?, ?, ?)', tuple(data.values()))
        base.commit()


async def sql_add_adv(state):
    async with state.proxy() as data:
        cur.execute('INSERT INTO users VALUES (?, ?, ?)', tuple(data.values()))
        base.commit()


async def all_users_id():
    return cur.execute(f"SELECT user_id FROM Users;")


async def show_adv(message):
    for ret in cur.execute("SELECT * FROM advertisements").fetchall():
        media = types.MediaGroup()

        media.attach_photo(ret[0], caption=ret[1])
        for i in ret[0][1::]:
            media.attach_photo(i)

        await bot.send_media_group(message.from_user.id, media=media)

