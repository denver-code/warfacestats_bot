from aiogram import types

async def start_event(message: types.Message):
    message_to_send = """
<b>Hello at WarfaceStatsBot - International!</b>
Here you can see statistics about users and clans on Russian or international servers!

<b>Bot is Under Development! If you found bug, write to developer @idenver_bot</b>

<b>To get information about a user, use:</b>
/player [DenSec]
Replace "[DenSec]" with a nickname.
To specify a Russian server, add "ru" to the command:
/player [DenSec] ru
Or basic send text message with nickname and server.

<b>To find out online servers:</b>
/online - will show the number of users on the European server
/online ru - on the Russian server.

/credits - find out those. bot information.
"""
    await message.answer(message_to_send, parse_mode="HTML")