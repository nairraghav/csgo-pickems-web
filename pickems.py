# documentation: https://developer.valvesoftware.com/wiki/Counter-Strike:_Global_Offensive_PickEm_Fantasy_Management
import requests
from os import getenv as os_getenv

steam_web_api_key = os_getenv("STEAM_WEB_API_KEY")
my_steam_id = os_getenv("MY_STEAM_ID")
my_steam_authentication_code_for_rio = os_getenv("MY_STEAM_AUTHENTICATION_CODE_FOR_RIO")
event_number = 20  # this is the event code for rio

tournament_url = f"https://api.steampowered.com/ICSGOTournaments_730/GetTournamentLayout/v1?key={steam_web_api_key}&event={event_number}"
get_pickems_url = f"https://api.steampowered.com/ICSGOTournaments_730/GetTournamentPredictions/v1?key={steam_web_api_key}&event={event_number}&steamid={my_steam_id}&steamidkey={my_steam_authentication_code_for_rio}"

tournament_info = requests.get(url=tournament_url).json()
# result
# event
# name
# sections
# sectionid
# name
# groups
# groupid
# name (prelim / group stage / quarter finals / etc)
# points_per_pick
# picks_allowed
# teams
# pickid
# picks
# index
# teams
# pickid
# logo
# name
