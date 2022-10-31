# documentation: https://developer.valvesoftware.com/wiki/Counter-Strike:_Global_Offensive_PickEm_Fantasy_Management
import requests
from os import getenv as os_getenv
from pprint import pprint as pprint_pprint

# get this from: https://steamcommunity.com/dev/apikey
steam_web_api_key = os_getenv(
    "STEAM_WEB_API_KEY", 
    "0"
)
# usually on your steamcommunity url
# if not: https://steamid.io/
my_steam_id = os_getenv(
    "MY_STEAM_ID", 
    "0"
)
# get this from: https://help.steampowered.com/en/wizard/HelpWithGameIssue/?appid=730&issueid=128&transid=2073071513017432044&line_item=2073071513017432046
my_steam_authentication_code_for_rio = os_getenv(
    "MY_STEAM_AUTHENTICATION_CODE_FOR_RIO",
    "0"
)
event_number = 20  # this is the event code for rio

tournament_url = f"https://api.steampowered.com/ICSGOTournaments_730/GetTournamentLayout/v1?key={steam_web_api_key}&event={event_number}"
get_pickems_url = f"https://api.steampowered.com/ICSGOTournaments_730/GetTournamentPredictions/v1?key={steam_web_api_key}&event={event_number}&steamid={my_steam_id}&steamidkey={my_steam_authentication_code_for_rio}"

tournament_info = requests.get(url=tournament_url).json()
tournament_info = tournament_info["result"]
tournament_name = tournament_info["name"]
# 0 - challengers (1 group, 8 picks), 1 - legends (1 group, 8 picks), 2 - QF (4 groups, 1 pick each), 3 - SF (2 groups, 1 pick each), 4 - GF (1 group, 1 pick)
tournament_sections = tournament_info["sections"]
challengers_group = tournament_sections[0]["groups"][0]
challengers_teams = challengers_group["teams"]
# each entry has logo, name, pickid
tournament_teams = tournament_info["teams"]


tournament_teams_map = {team["pickid"]: team["name"] for team in tournament_teams}
pprint_pprint(tournament_teams_map)

print("Challenger Teams:")
challenger_team_names = [tournament_teams_map[team["pickid"]] for team in challengers_teams]
print(challenger_team_names)

current_pickems = requests.get(url=get_pickems_url).json()["result"]
# pick 0: 3-0 team
# pick 8: 0-3 team
pprint_pprint(current_pickems)