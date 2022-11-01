# documentation: https://developer.valvesoftware.com/wiki/Counter-Strike:_Global_Offensive_PickEm_Fantasy_Management
import requests
from os import getenv as os_getenv
from pprint import pprint as pprint_pprint

# get this from: https://steamcommunity.com/dev/apikey
steam_web_api_key = os_getenv(
    "STEAM_WEB_API_KEY", 
    ""
)
# usually on your steamcommunity url
# if not: https://steamid.io/
my_steam_id = os_getenv(
    "MY_STEAM_ID", 
    ""
)
# get this from: https://help.steampowered.com/en/wizard/HelpWithGameIssue/?appid=730&issueid=128&transid=2073071513017432044&line_item=2073071513017432046
my_steam_authentication_code_for_rio = os_getenv(
    "MY_STEAM_AUTHENTICATION_CODE_FOR_RIO",
    ""
)
event_number = 20 #19  # this is the event code for rio

tournament_url = f"https://api.steampowered.com/ICSGOTournaments_730/GetTournamentLayout/v1?key={steam_web_api_key}&event={event_number}"
print(f"Tournament URL: \n{tournament_url}")
get_pickems_url = f"https://api.steampowered.com/ICSGOTournaments_730/GetTournamentPredictions/v1?key={steam_web_api_key}&event={event_number}&steamid={my_steam_id}&steamidkey={my_steam_authentication_code_for_rio}"
print(f"Pickems URL: \n{get_pickems_url}")
set_pickems_url = f"https://api.steampowered.com/ICSGOTournaments_730/UploadTournamentPredictions/v1?key={steam_web_api_key}"
# POST Body Data
# event=X&steamid=XX&steamidkey=XX-XX-XX&sectionid=X&groupid=X&index=X&pickid=X&itemid=X(429500386?)

tournament_info = requests.get(url=tournament_url).json()
tournament_info = tournament_info["result"]
tournament_name = tournament_info["name"]
# 0 - challengers (1 group, 8 picks), 1 - legends (1 group, 8 picks), 2 - QF (4 groups, 1 pick each), 3 - SF (2 groups, 1 pick each), 4 - GF (1 group, 1 pick)
tournament_sections = tournament_info["sections"]
group_information = dict()
picks = dict()

# each entry has logo, name, pickid
tournament_teams = tournament_info["teams"]



tournament_teams_map = {team["pickid"]: team["name"] for team in tournament_teams}
print("Team Pick Id -> Team Name")
pprint_pprint(tournament_teams_map)
print("\n\n")

challengers_group = tournament_sections[0]["groups"][0]
group_information["challengers"] = {"name": challengers_group["name"], "groupid": challengers_group["groupid"]}
picks[challengers_group["groupid"]] = {"name": challengers_group["name"]}
challengers_teams = challengers_group["teams"]
print("Challenger Teams:")
challengers_team_names = [tournament_teams_map.get(team["pickid"], "Teams Not Set") for team in challengers_teams]
pprint_pprint(challengers_team_names)
print("\n\n")

legends_group = tournament_sections[1]["groups"][0]
group_information["legends"] = {"name": legends_group["name"], "groupid": legends_group["groupid"]}
picks[legends_group["groupid"]] = {"name": legends_group["name"]}
legends_teams = legends_group["teams"]
print("Legend Teams:")
legend_team_names = [tournament_teams_map.get(team["pickid"], "Teams Not Set") for team in legends_teams]
pprint_pprint(legend_team_names)
print("\n\n")

quarters_groups = tournament_sections[2]["groups"]
group_information["quarters"] = list()
quarters_teams = list()
for quarters_group in quarters_groups:
    group_information["quarters"].append({"name": quarters_group["name"], "groupid": quarters_group["groupid"]})
    picks[quarters_group["groupid"]] = {"name": quarters_group["name"]}
    quarters_teams.extend(quarters_group["teams"])
    quarter_team_names = [tournament_teams_map.get(team["pickid"], "Teams Not Set") for team in quarters_teams]
print("Quarters Teams:")
pprint_pprint(quarter_team_names)
print("\n\n")

semis_groups = tournament_sections[3]["groups"]
group_information["semis"] = list()
semis_teams = list()
for semis_group in semis_groups:
    group_information["semis"].append({"name": semis_group["name"], "groupid": semis_group["groupid"]})
    picks[semis_group["groupid"]] = {"name": semis_group["name"]}
    semis_teams.extend(semis_group["teams"])    
    semis_team_names = [tournament_teams_map.get(team["pickid"], "Teams Not Set") for team in semis_teams]
print("Semis Teams:")
pprint_pprint(semis_team_names)
print("\n\n")

finals_group = tournament_sections[4]["groups"][0]
group_information["finals"] = {"name": finals_group["name"], "groupid": finals_group["groupid"]}
picks[finals_group["groupid"]] = {"name": finals_group["name"]}
finals_teams = finals_group["teams"]
print("Finals Teams:")
finals_teams_names = [tournament_teams_map.get(team["pickid"], "Teams Not Set") for team in finals_teams]
pprint_pprint(finals_teams_names)
print("\n\n")


# pick 0: 3-0 team
# pick 8: 0-3 team
print("My Picks")
current_pickems = requests.get(url=get_pickems_url).json()["result"]["picks"]
for pick in current_pickems:
    pick_groupid = pick["groupid"]
    pick_index = pick["index"]
    pick_team = tournament_teams_map[pick["pick"]]
    picks[pick_groupid][pick_index] = pick_team
print("\n\n")

pprint_pprint(picks)