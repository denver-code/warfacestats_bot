from aiogram import types
import requests

async def player_stats(message: types.Message):
    work_string = message.get_args()

    server = "int"
    if "ru" in work_string:
        server = "ru"
    username = work_string.split()[0]

    response = requests.get(f"https://api.wfstats.cf/player/stats?nickname={username}&server={server}").json()
    if "msg" in response:
        if response["msg"] == "player_not_found":
            return await message.reply(response["status"].replace("{}", username)) 
        elif response["msg"] == "player_inactive":
            return await message.reply(response["status"].replace("{}", username))
    elif "message" in response:
        if response["message"] == "Internal server error":
            return await message.reply(f"Player {username} not found in server {server}")

    if server == "ru":
        server_str = "Russian"
    else:
        server_str = "International"
    
    message_text = f"""
<b>Statistics for player {username}:</b>
<b>Server</b>: {server_str}
<b>Rank</b>: {response["rank_id"]}
<b>Total play:</b> {response["playtime_h"]} hours
<b>Clan:</b> {response["clan_name"]}

<b>PVP short:</b>
- <b>Total kills:</b> {response["kills"]}
- <b>Friendly kills:</b> {response["friendly_kills"]}
- <b>Death</b>: {response["death"]}
- <b>K/D Ratio</b>: {response["pvp"]}
- <b>Wins:</b> {response["pvp_wins"]}
- <b>Lost:</b> {response["pvp_lost"]}
- <b>Total games:</b> {response["pvp_all"]}

<b>PVE short:</b>
- <b>Total kills:</b> {response["pve_kills"]}
- <b>Friendly kills:</b> {response["pve_friendly_kills"]}
- <b>Death</b>: {response["pve_death"]}
- <b>K/D Ratio</b>: {response["pve"]}
- <b>Wins:</b> {response["pve_wins"]}
- <b>Lost:</b> {response["pve_lost"]}
- <b>Total games:</b> {response["pve_all"]}
"""
    await message.answer(message_text, parse_mode="HTML")