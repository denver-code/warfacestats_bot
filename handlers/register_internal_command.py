from aiogram import types, Dispatcher
from internal.credits import credits_event
from internal.player_stats import player_stats
from internal.online_stats import region_online


def register_internal_commands(dp: Dispatcher):
    dp.register_message_handler(credits_event, commands="credits")
    dp.register_message_handler(player_stats, commands="player")
    dp.register_message_handler(region_online, commands="online")