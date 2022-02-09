import os
import logging
from handlers.register_internal_command import register_internal_commands
from internal.player_stats import allinfo_event, player_stats, pveinfo_event, pvpinfo_event, get_clan_event

if not os.path.isdir('logs'):
    os.mkdir("logs")

file_log = logging.FileHandler('logs/warfacestats_bot.log')
console_out = logging.StreamHandler()
logging.basicConfig(handlers=(file_log, console_out),
                            format='[%(asctime)s | %(levelname)s]: %(message)s',
                            datefmt='%m.%d.%Y %H:%M:%S',
                            level=logging.INFO)

from dotenv import load_dotenv

load_dotenv()

config = {
    "TOKEN": os.getenv("TOKEN"),
    "OWNER_ID": os.getenv("OWNER_ID")
}

from aiogram import Bot, Dispatcher, executor, types


bot = Bot(token=config["TOKEN"])
dp = Dispatcher(bot)


@dp.callback_query_handler()
async def callback_query_recognizer(query: types.CallbackQuery):
    if "allinfo" in query.data:
        username = query.data.split("/")[1]
        server = query.data.split("/")[-1]
        await allinfo_event(query, username, server)

    elif "info" in query.data:
        username = query.data.split("/")[1]
        server = query.data.split("/")[-1]
        query.message.reply_to_message["text"] = f"/player {username} {server}"
        await bot.delete_message(chat_id=query.from_user.id, message_id=query.message.message_id)
        await player_stats(query.message.reply_to_message)

    elif "pve" in query.data:
        class_player = None
        if len(query.data.split("/")) == 4:
            class_player = query.data.split("/")[-1]
        username = query.data.split("/")[1]
        server = query.data.split("/")[2]
        await pveinfo_event(query, username, server, class_player)

    elif "pvp" in query.data:
        class_player = None
        if len(query.data.split("/")) == 4:
            class_player = query.data.split("/")[-1]
        username = query.data.split("/")[1]
        server = query.data.split("/")[2]
        await pvpinfo_event(query, username, server, class_player)

    elif "clan" in query.data:
        clan_name = query.data.split("/")[1]
        server = query.data.split("/")[2]
        username = query.data.split("/")[3]
        await get_clan_event(query, clan_name, server, username)


async def set_bot_commands(bot: Bot):
    commands = [
        types.BotCommand(command="start", description="Startup command"),
        types.BotCommand(command="ping", description="Basic command - for checking status"),
        types.BotCommand(command="credits", description="Learn more about this bot"),
        types.BotCommand(command="player", description="<name> Get player info '/player [DenSec]'"),
        types.BotCommand(command="online", description="<ru/int> Get online for ru or int server"),
    ]
    await bot.set_my_commands(commands)


async def on_startup(_):
    await set_bot_commands(bot)
    register_internal_commands(dp)
    await bot.send_message(config["OWNER_ID"], '*WFStats - International - Online🟢*', parse_mode="Markdown")


@dp.message_handler(commands="ping")
async def ping_event(message: types.Message):
    await message.reply("Pong!")


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
