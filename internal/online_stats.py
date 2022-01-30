import requests

from aiogram import types


async def region_online(message: types.Message):
    pve_count = 0
    pvp_count = 0
    if message.get_args() == "ru":
        server = "Russian"
        response = requests.get("https://api.wfstats.cf/stats/ru").json()
        for i in response:
            if "pve" in i:
                pve_count += response[i]
            elif "pvp" in i:
                pvp_count += response[i]
    else:
        server = "International"
        response = requests.get("https://api.wfstats.cf/stats/int").json()
        for i in response:
            if "pve" in i:
                pve_count += response[i]
            elif "pvp" in i:
                pvp_count += response[i]

    total_count = pve_count + pvp_count

    message_text = f"""
*Warface {server} current online:*

PVE: {pve_count}
PVP: {pvp_count}
Total: {total_count}
"""
    await message.answer(message_text, parse_mode="Markdown")