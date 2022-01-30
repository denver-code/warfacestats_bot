import os

from aiogram import types
from dotenv import load_dotenv

load_dotenv()

async def credits_event(message: types.Message):
    await message.answer(f"""
*WFStats - Internal:*

*Developer:*
- *Telegram* - [Igor Savenko aka Denver](tg://user?id={os.getenv("OWNER_ID")})
- *Warface* - [DenSec](https://pc.warface.com/custom/ub/MV8xNTUwNTAxOHNvbWVfdG9rZW5fa2V5/b817074b473260eba113eabbd1967fbb/bar.jpg)

Stack:
- *Python3* + *AIOgram*

*Used APIs:*
[WFStats.cf api](https://api.wfstats.cf/)
[WFStats.cf website](https://wfstats.cf)
""", parse_mode="Markdown", disable_web_page_preview=False)