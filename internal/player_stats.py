from aiogram import types
import requests

async def player_stats(message: types.Message):
    work_string = message.get_args()

    server = "int"
    if "ru" in work_string:
        server = "ru"
    username = work_string.split()[0]

    print(username)

    response = requests.get(f"https://api.wfstats.cf/player/stats?nickname={username}&server={server}").json()
    if "msg" in response:
        if response["msg"] in ["player_not_found", "player_inactive", "player_hidden"]:
            return await message.reply(response["status"].replace("{}", username)) 
    elif "message" in response:
        print(response)
        if response["message"] == "Internal server error":
            return await message.reply(f"Player {username} not found in server {server}, or player inactive")

    if server == "ru":
        server_str = "Russian"
    else:
        server_str = "International"

    clan_str = """
    """
    if "clan_name" in response:
        clan_str = f"""<b>Clan:</b> {response["clan_name"]}
        """
    
    message_text = f"""
<b>Statistics for player {username}:</b>
<b>Server</b>: {server_str}
<b>Rank</b>: {response["rank_id"]}
<b>Total play:</b> {response["playtime_h"] if "playtime_h" in response else 0}h {response["playtime_m"] if "playtime_m" in response else 0}m
<b>Experience:</b> {response["experience"] if "experience" in response else 0}
{clan_str}
<b>PVP short:</b>
- <b>Total kills:</b> {response["kills"] if "kills" in response else 0}
- <b>Friendly kills:</b> {response["friendly_kills"] if "friendly_kills" in response else 0}
- <b>Death</b>: {response["death"] if "death" in response else 0}
- <b>K/D Ratio</b>: {response["pvp"] if "pvp" in response else 0}
- <b>Wins:</b> {response["pvp_wins"] if "pvp_wins" in response else 0}
- <b>Lost:</b> {response["pvp_lost"] if "pvp_lost" in response else 0}
- <b>Total games:</b> {response["pvp_all"] if "pvp_all" in response else 0}

<b>PVE short:</b>
- <b>Total kills:</b> {response["pve_kills"] if "pve_kills" in response else 0}
- <b>Friendly kills:</b> {response["pve_friendly_kills"] if "pve_friendly_kills" in response else 0}
- <b>Death</b>: {response["pve_death"] if "pve_death" in response else 0}
- <b>K/D Ratio</b>: {response["pve"] if "pve" in response else 0}
- <b>Wins:</b> {response["pve_wins"] if "pve_wins" in response else 0}
- <b>Lost:</b> {response["pve_lost"] if "pve_lost" in response else 0}
- <b>Total games:</b> {response["pve_all"] if "pve_all" in response else 0}
"""
    buttons = [
        types.InlineKeyboardButton(text="All information", callback_data=f"allinfo/{username}/{server}"),
        types.InlineKeyboardButton(text="PVE", callback_data=f"pve/{username}/{server}"),
        types.InlineKeyboardButton(text="PVP", callback_data=f"pvp/{username}/{server}")
    ]
    if "clan_name" in response:
        buttons.append(types.InlineKeyboardButton(text="Clan", callback_data=f"clan/{response['clan_name']}/{server}/{username}"))
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(*buttons)
    await message.reply(message_text, parse_mode="HTML", reply_markup=keyboard)


async def allinfo_event(query, username, server):
    response = requests.get(f"https://api.wfstats.cf/player/stats?nickname={username}&server={server}").json()
    if "msg" in response:
        if response["msg"] in ["player_not_found", "player_inactive", "player_hidden"]:
            return await query.message.reply(response["status"].replace("{}", username)) 
    elif "message" in response:
        if response["message"] == "Internal server error":
            return await query.message.reply(f"Player {username} not found in server {server}, or player inactive")

    if server == "ru":
        server_str = "Russian"
    else:
        server_str = "International"
    
    clan_str = """
    """
    if "clan_name" in response:
        clan_str = f"""<b>Clan:</b> {response["clan_name"]}
<b>ClanID:</b> {response["clan_id"]}
        """

    message_text = f"""
<b>All Statistics for player {username}:</b>
<b>UserID:</b> {response["user_id"]}
<b>Server</b>: {server_str}
<b>Rank</b>: {response["rank_id"]}
<b>Total play:</b> {response["playtime_h"] if "playtime_h" in response else 0}h {response["playtime_m"] if "playtime_m" in response else 0}m
<b>Experience:</b> {response["experience"] if "experience" in response else 0}
{clan_str}
<b>General:</b>
- <b>Ammo restored:</b> {response["stat"]["player_ammo_restored"] if "player_ammo_restored" in response["stat"] else 0}
- <b>Climb Assists:</b> {response["stat"]["player_climb_assists"] if "player_climb_assists" in response["stat"] else 0}
- <b>Climb Coops:</b> {response["stat"]["player_climb_coops"] if "player_climb_coops" in response["stat"] else 0}
- <b>Damage:</b> {response["stat"]["player_damage"] if "player_damage" in response["stat"] else 0}
- <b>Heal:</b> {response["stat"]["player_heal"] if "player_heal" in response["stat"] else 0}
- <b>Max Damage:</b> {response["stat"]["player_max_damage"] if "player_max_damage" in response["stat"] else 0}
- <b>Max Session Time:</b> {float('{:.1f}'.format(int(str(response["stat"]["player_max_session_time"]))/3600)) if "player_max_session_time" in response["stat"] else 0}h
- <b>Repair:</b> {response["stat"]["player_repair"] if "player_repair" in response["stat"] else 0}
- <b>Resurrected By Coin:</b> {response["stat"]["player_resurrected_by_coin"] if "player_resurrected_by_coin" in response["stat"] else 0}
- <b>Resurrected By Medic:</b> {response["stat"]["player_resurrected_by_medic"] if "player_resurrected_by_medic" in response["stat"] else 0}
- <b>LobbyTime:</b> {float('{:.1f}'.format(int(str(response["stat"]["player_lobbytime"])[:-2])/3600)) if "player_lobbytime" in response["stat"] else 0}h

<b>PVP:</b>
- <b>Total kills:</b> {response["kills"] if "kills" in response else 0}
- <b>Friendly kills:</b> {response["friendly_kills"] if "friendly_kills" in response else 0}
- <b>Death</b>: {response["death"] if "death" in response else 0}
- <b>K/D Ratio</b>: {response["pvp"] if "pvp" in response else 0}
- <b>Wins:</b> {response["pvp_wins"] if "pvp_wins" in response else 0}
- <b>Lost:</b> {response["pvp_lost"] if "pvp_lost" in response else 0}
- <b>Total games:</b> {response["pvp_all"] if "pvp_all" in response else 0}
- <b>W/L Ratio:</b> {response["pvpwl"] if "pvpwl" in response else 0}
- <b>Favorite:</b> {response["favoritPVP"] if "favoritPVP" in response else "Rifleman"}

<b>PVE:</b>
- <b>Total kills:</b> {response["pve_kills"] if "pve_kills" in response else 0}
- <b>Friendly kills:</b> {response["pve_friendly_kills"] if "pve_friendly_kills" in response else 0}
- <b>Death</b>: {response["pve_death"] if "pve_death" in response else 0}
- <b>K/D Ratio</b>: {response["pve"] if "pve" in response else 0}
- <b>Wins:</b> {response["pve_wins"] if "pve_wins" in response else 0}
- <b>Lost:</b> {response["pve_lost"] if "pve_lost" in response else 0}
- <b>Total games:</b> {response["pve_all"] if "pve_all" in response else 0}
- <b>Favorite:</b> {response["favoritPVE"] if "favoritPVE" in response else "Rifleman"}
"""
    buttons = [
        types.InlineKeyboardButton(text="Back", callback_data=f"info/{username}/{server}"),
    ]
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(*buttons)

    await query.message.edit_text(message_text, parse_mode="HTML", reply_markup=keyboard)


async def pveinfo_event(query, username, server, player_class=None):
    response = requests.get(f"https://api.wfstats.cf/player/stats?nickname={username}&server={server}").json()
    if "msg" in response:
        if response["msg"] in ["player_not_found", "player_inactive", "player_hidden"]:
            return await query.message.reply(response["status"].replace("{}", username)) 
    elif "message" in response:
        if response["message"] == "Internal server error":
            return await query.message.reply(f"Player {username} not found in server {server}, or player inactive")

    if server == "ru":
        server_str = "Russian"
    else:
        server_str = "International"
    
    clan_str = """
    """
    if "clan_name" in response:
        clan_str = f"""<b>Clan:</b> {response["clan_name"]}
<b>ClanID:</b> {response["clan_id"]}
        """

    headshots = 0
    hits = 0
    shots = 0
    play_time = 0


    for i in response["class"]:
        obj = response["class"][i]["PVE"]
        items = ["player_headshots", "player_hits", "player_shots"]
        for j in items:
            if j not in obj:
                obj[j] = 0
        if "player_playtime" not in obj:
            obj["player_playtime"] = 10
        headshots += obj["player_headshots"]
        hits += obj["player_hits"]
        shots += obj["player_shots"]
        play_time += int(str(obj["player_playtime"])[:-1])

    class_str = """
    """
    if player_class in ["Rifleman", "Heavy", "Recon", "Engineer", "Medic"]: 
        class_str =f"""
<b>{player_class} PVE Statistics:</b>
- <b>Headshots:</b> {response["class"][player_class]["PVE"]["player_headshots"] if "player_headshots" in response["class"][player_class]["PVE"] else 0}
- <b>Hits:</b> {response["class"][player_class]["PVE"]["player_hits"] if "player_hits" in response["class"][player_class]["PVE"] else 0}
- <b>Playtime:</b> {int(int(str(response["class"][player_class]["PVE"]["player_headshots"])[:-1])/3600) if "player_headshots" in response["class"][player_class]["PVE"] else 0}
- <b>Shots:</b> {response["class"][player_class]["PVE"]["player_shots"] if "player_shots" in response["class"][player_class]["PVE"] else 0}
"""


    message_text = f"""
<b>PVE Statistics for player {username}:</b>
<b>Server</b>: {server_str}
<b>Rank</b>: {response["rank_id"]}
<b>Total play:</b> {response["playtime_h"] if "playtime_h" in response else 0}h {response["playtime_m" if "playtime_m" in response else 0]}m
<b>Experience:</b> {response["experience"] if "experience" in response else 0}
{clan_str}
<b>PVE:</b>
- <b>Total kills:</b> {response["pve_kills"] if "pve_kills" in response else 0}
- <b>AI kills:</b> {response["mode"]["PVE"]["player_kills_ai"] if "player_kills_ai" in response["mode"]["PVP"] else 0}
- <b>Melee kills:</b> {response["mode"]["PVE"]["player_kills_melee"] if "player_kills_melee" in response["mode"]["PVP"] else 0}
- <b>Friendly kills:</b> {response["pve_friendly_kills"] if "pve_friendly_kills" in response else 0}
- <b>Headshots:</b> {headshots}
- <b>Total hits:</b> {hits}
- <b>Total shots:</b> {shots}
- <b>Playtime:</b> {int(play_time/3600)} hours
- <b>S/H ratio:</b> {float('{:.1f}'.format(shots/hits))}
- <b>Death</b>: {response["pve_death"] if "pve_death" in response else 0}
- <b>K/D Ratio</b>: {response["pve"] if "pve" in response else 0}
- <b>Wins:</b> {response["pve_wins"] if "pve_wins" in response else 0}
- <b>Lost:</b> {response["pve_lost"] if "pve_lost" in response else 0}
- <b>Total games:</b> {response["pve_all"] if "pve_all" in response else 0}
- <b>Favorite:</b> {response["favoritPVE"] if "favoritPVE" in response else "Rifleman"}
- <b>Left from room:</b> {response["mode"]["PVE"]["player_sessions_left"] if "player_sessions_left" in response["mode"]["PVP"] else 0}
- <b>Kicked from room:</b> {response["mode"]["PVE"]["player_sessions_kicked"] if "player_sessions_kicked" in response["mode"]["PVP"] else 0}
- <b>Lost Connection:</b> {response["mode"]["PVE"]["player_sessions_lost_connection"] if "player_sessions_lost_connection" in response["mode"]["PVP"] else 0}

{class_str}
"""
    buttons = [
        types.InlineKeyboardButton(text="Rifleman", callback_data=f"pve/{username}/{server}/Rifleman"),
        types.InlineKeyboardButton(text="Medic", callback_data=f"pve/{username}/{server}/Medic"),
        types.InlineKeyboardButton(text="Engineer", callback_data=f"pve/{username}/{server}/Engineer"),
        types.InlineKeyboardButton(text="Recon", callback_data=f"pve/{username}/{server}/Recon"), 
        types.InlineKeyboardButton(text="Heavy", callback_data=f"pve/{username}/{server}/Heavy"),
        types.InlineKeyboardButton(text="Back", callback_data=f"info/{username}/{server}"),
    ]
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(*buttons)

    await query.message.edit_text(message_text, parse_mode="HTML", reply_markup=keyboard)


async def pvpinfo_event(query, username, server, player_class=None):
    response = requests.get(f"https://api.wfstats.cf/player/stats?nickname={username}&server={server}").json()
    if "msg" in response:
        if response["msg"] in ["player_not_found", "player_inactive", "player_hidden"]:
            return await query.message.reply(response["status"].replace("{}", username)) 
    elif "message" in response:
        if response["message"] == "Internal server error":
            return await query.message.reply(f"Player {username} not found in server {server}, or player inactive")

    if server == "ru":
        server_str = "Russian"
    else:
        server_str = "International"
    
    clan_str = """
    """
    if "clan_name" in response:
        clan_str = f"""<b>Clan:</b> {response["clan_name"]}
<b>ClanID:</b> {response["clan_id"]}
        """

    headshots = 0
    hits = 0
    shots = 0
    play_time = 0


    for i in response["class"]:
        obj = response["class"][i]["PVE"]
        items = ["player_headshots", "player_hits", "player_shots"]
        for j in items:
            if j not in obj:
                obj[j] = 0
        if "player_playtime" not in obj:
            obj["player_playtime"] = 10
        headshots += obj["player_headshots"]
        hits += obj["player_hits"]
        shots += obj["player_shots"]
        play_time += int(str(obj["player_playtime"])[:-1])

    class_str = """
    """
    if player_class in ["Rifleman", "Heavy", "Recon", "Engineer", "Medic"]: 
        class_str =f"""
<b>{player_class} PVP Statistics:</b>
- <b>Headshots:</b> {response["class"][player_class]["PVP"]["player_headshots"] if "player_headshots" in response["class"][player_class]["PVP"] else 0}
- <b>Hits:</b> {response["class"][player_class]["PVP"]["player_hits"] if "player_hits" in response["class"][player_class]["PVP"] else 0}
- <b>Playtime:</b> {int(int(str(response["class"][player_class]["PVP"]["player_headshots"])[:-1])/3600) if "player_headshots" in response["class"][player_class]["PVP"] else 0}
- <b>Shots:</b> {response["class"][player_class]["PVP"]["player_shots"] if "player_shots" in response["class"][player_class]["PVP"] else 0}
"""      

    message_text = f"""
<b>PVP Statistics for player {username}:</b>
<b>Server</b>: {server_str}
<b>Rank</b>: {response["rank_id"]}
<b>Total play:</b> {response["playtime_h" if "playtime_h" in response else 0]}h {response["playtime_m" if "playtime_m" in response else 0]}m
<b>Experience:</b> {response["experience"] if "experience" in response else 0}
{clan_str}
<b>PVP:</b>
- <b>Total kills:</b> {response["kills"] if "kills" in response else 0}
- <b>AI kills:</b> {response["mode"]["PVP"]["player_kills_player"] if "player_kills_player" in response["mode"]["PVP"] else 0}
- <b>Melee kills:</b> {response["mode"]["PVP"]["player_kills_melee"] if "player_sessions_draw" in response["mode"]["PVP"] else 0}
- <b>Friendly kills:</b> {response["mode"]["PVP"]["player_kills_player_friendly"] if "player_kills_player_friendly" in response["mode"]["PVP"] else 0}
- <b>Headshots:</b> {headshots}
- <b>Total hits:</b> {hits}
- <b>Total shots:</b> {shots}
- <b>Playtime:</b> {int(play_time/3600)} hours
- <b>S/H ratio:</b> {float('{:.1f}'.format(shots/hits))}
- <b>Death</b>: {response["death"] if "death" in response else 0}
- <b>K/D Ratio</b>: {response["pvp"] if "pvp" in response else 0}
- <b>Favorite:</b> {response["favoritPVP"] if "favoritPVP" in response else "Rifleman"}
- <b>Total games:</b> {response["pvp_all"] if "pvp_all" in response else 0}
- <b>Wins:</b> {response["pvp_wins"] if "pvp_wins" in response else 0}
- <b>Lost:</b> {response["pvp_lost"] if "pvp_lost" in response else 0}
- <b>Left from room:</b> {response["mode"]["PVP"]["player_sessions_left"] if "player_sessions_left" in response["mode"]["PVP"] else 0}
- <b>Kicked from room:</b> {response["mode"]["PVP"]["player_sessions_kicked"] if "player_sessions_kicked" in response["mode"]["PVP"] else 0}
- <b>Lost Connection:</b> {response["mode"]["PVP"]["player_sessions_lost_connection"] if "player_sessions_lost_connection" in response["mode"]["PVP"] else 0}
- <b>Sessions Draw:</b> {response["mode"]["PVP"]["player_sessions_draw"] if "player_sessions_draw" in response["mode"]["PVP"] else 0}

{class_str}
"""
    buttons = [
        types.InlineKeyboardButton(text="Rifleman", callback_data=f"pve/{username}/{server}/Rifleman"),
        types.InlineKeyboardButton(text="Medic", callback_data=f"pve/{username}/{server}/Medic"),
        types.InlineKeyboardButton(text="Engineer", callback_data=f"pve/{username}/{server}/Engineer"),
        types.InlineKeyboardButton(text="Recon", callback_data=f"pve/{username}/{server}/Recon"),
        types.InlineKeyboardButton(text="Heavy", callback_data=f"pve/{username}/{server}/Heavy"),
        types.InlineKeyboardButton(text="Back", callback_data=f"info/{username}/{server}"),
    ]
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(*buttons)

    await query.message.edit_text(message_text, parse_mode="HTML", reply_markup=keyboard)


async def get_clan_event(query, clanname, server, username):
    response = requests.get(f"https://api.wfstats.cf/clan/members?name={clanname}&server={server}").json()
    if "msg" in response:
        if response["msg"] in ["clan_not_found"]:
            return await query.message.reply(response["status"].replace("{}", clanname)) 
    elif "message" in response:
        if response["message"] == "Internal server error":
            return await query.message.reply(f"Clan {clanname} not found in server {server}")
    clan = response

    clan_roles = {
        "OFFICER": "OFFICER",
        "REGULAR": "SOLIDER",
        "MASTER": "MASTER"
    }

    message_text = f"""<b>{clanname} Information:</b>
- <b>Clan Name:</b> {clanname}
- <b>ClanID:</b> {clan["id"]}
- <b>Server:</b> {server}
- <b>Clan Points:</b> {clan["clan_points"]}
- <b>Members Count:</b> {len(clan["members"])}
- <b>Members TOP: (Tap For Get Details)</b>
"""
    buttons = []

    for i in clan["members"]:
        buttons.append(types.InlineKeyboardButton(text=f"{clan_roles[i['clan_role']]}     {i['nickname']}     {i['clan_points']}", callback_data=f"info/{i['nickname']}/{server}"))

    buttons.append(types.InlineKeyboardButton(text="Back", callback_data=f"info/{username}/{server}"),)
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(*buttons)

    await query.message.edit_text(message_text, parse_mode="HTML", reply_markup=keyboard)