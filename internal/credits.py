import os

from aiogram import types
from dotenv import load_dotenv

load_dotenv()

async def credits_event(message: types.Message):
    await message.answer(f"""
<b>WFStats - Internal:</b>

<b>Developer:</b>
- <b>Telegram</b>:
  - <a href="tg://user?id={os.getenv("OWNER_ID")}">Igor Savenko aka СтаричокМираАйти</a>
- <b>Warface Image</b> - <a href="https://ru.warface.com/custom/ub/fbb7ee231cc73b3baa7f1a2550599192/30b70b897669cdd3c06bb6d333115b42/bar.jpg">[DenSec]</a>
- <b>Warface Promo</b> - <a href="https://ru.warface.com/promo/referal/?ref=3o1na2n">Tap</a>

Stack:
- <b>Python3</b> + <b>AIOgram</b>

<b>Used APIs:</b>
<a href="https://api.wfstats.cf/">WFStats.cf api</a>
<a href="https://wfstats.cf">WFStats.cf website</a>

<b>Source code:</b>
https://github.com/denver-code/warfacestats_bot/
""", parse_mode="HTML", disable_web_page_preview=False)