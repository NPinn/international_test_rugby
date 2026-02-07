import requests
import json
import os
import glob
from credentials import *

_rel_path = os.path.realpath('')
base_path = os.path.abspath(_rel_path)

data_path = os.path.join(base_path, 'data')
raw_data_path = os.path.join(data_path, 'raw_data')
cleaned_data_path = os.path.join(data_path, 'cleaned_data')

# Import All Rugby Matches
all_rugby_matches_dict = json.load(open(os.path.join(raw_data_path, 'all_rugby_matches.json')))
# Import International Team Ids
international_teams_dict = json.load(open(os.path.join(raw_data_path, "international_rugby_team_ids.json")))

# Find Only International Matches
international_rugby_matches_dict = {}
for matchId, matchDetails in all_rugby_matches_dict.items():
    if matchDetails['teamAid'] in international_teams_dict.keys() and matchDetails['teamBid']:
        international_rugby_matches_dict[matchId] = matchDetails

# Save Results
with open(os.path.join(raw_data_path, "international_rugby_matches.json"), "w") as jfile:
    json.dump(international_rugby_matches_dict, jfile)