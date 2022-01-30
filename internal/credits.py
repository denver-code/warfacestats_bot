import os

from aiogram import types
from dotenv import load_dotenv

load_dotenv()

async def credits_event(message: types.Message):
    await message.answer(f"""
<b>WFStats - Internal:</b>

<b>Developer:</b>
- <b>Telegram</b>:
  - <a href="tg://user?id={os.getenv("OWNER_ID")}">Igor Savenko aka Denver/DenSec</a>
- <b>Warface</b> - <a href="https://pc.warface.com/custom/ub/MV8xNTUwNTAxOHNvbWVfdG9rZW5fa2V5/b817074b473260eba113eabbd1967fbb/bar.jpg">[DenSec]</a>

Stack:
- <b>Python3</b> + <b>AIOgram</b>

<b>Used APIs:</b>
<a href="https://api.wfstats.cf/">WFStats.cf api</a>
<a href="https://wfstats.cf">WFStats.cf website</a>

<b>Source code:</b>
https://github.com/denver-code/warfacestats_bot/
""", parse_mode="HTML", disable_web_page_preview=False)