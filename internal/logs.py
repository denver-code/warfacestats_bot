import os

from aiogram import types


async def send_log(message: types.Message):
    if message.from_user.id == int(os.getenv("OWNER_ID")):
        await message.reply_document(open("logs/warfacestats_bot.log", 'rb'))