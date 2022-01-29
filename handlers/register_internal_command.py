from aiogram import types, Dispatcher
from internal.credits import credits_event

def register_internal_commands(dp: Dispatcher):
    dp.register_message_handler(credits_event, commands="credits")