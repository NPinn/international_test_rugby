import requests
import json
import os
import glob

WR_API = "https://api.wr-rims-prod.pulselive.com/rugby/v3"

print('Extracting Details')
page = 0
all_matches = []
while True:
    ret = requests.get(f"{WR_API}/match?pageSize=100&sort=asc&page={page}").json()

    matches = ret['content']

    if not matches:
        break

    print(f"Results as of Page {page}: Retrieved {len(matches)} items (total so far: {len(all_matches)})")
    all_matches.extend(matches)

    page += 1
print(f"Total matches retrieved: {len(all_matches)}")

print('Creating Full Match Dictionary')
full_dict = {}
for match in all_matches:
    if match['status'] != 'U':
        clean_dict = {}
        # Match Details
        #clean_dict['matchId'] = match['matchId']
        clean_dict['matchAltId'] = match['matchAltId']
        clean_dict['description'] = match['description']
        clean_dict['eventPhase'] = match['eventPhase']
        #Venue Details
        try:
            clean_dict['venueId'] = match['venue']['id']
            clean_dict['venueAltId'] = match['venue']['altId']
            clean_dict['venueName'] = match['venue']['name']
            clean_dict['venueCity'] = match['venue']['city']
            clean_dict['venueCountry'] = match['venue']['country']
        except:
            clean_dict['venue'] = match['venue']
        # Match Date
        clean_dict['matchDate'] = match['time']['label']
        # Match Attendance
        clean_dict['matchAttendance'] = match['attendance']
        # Team A Details
        clean_dict['teamAid'] = match['teams'][0]['id']
        clean_dict['teamAaltId'] = match['teams'][0]['altId']
        clean_dict['teamAname'] = match['teams'][0]['name']
        clean_dict['teamAabbreviation'] = match['teams'][0]['abbreviation']
        clean_dict['teamAcountryCode'] = match['teams'][0]['countryCode']
        clean_dict['teamAannotations'] = match['teams'][0]['annotations']
        clean_dict['teamAmetadata'] = match['teams'][0]['metadata']
        clean_dict['teamAscore'] = match['scores'][0]
        # Team B Details
        clean_dict['teamBid'] = match['teams'][1]['id']
        clean_dict['teamBaltId'] = match['teams'][1]['altId']
        clean_dict['teamBname'] = match['teams'][1]['name']
        clean_dict['teamBabbreviation'] = match['teams'][1]['abbreviation']
        clean_dict['teamBcountryCode'] = match['teams'][1]['countryCode']
        clean_dict['teamBannotations'] = match['teams'][1]['annotations']
        clean_dict['teamBmetadata'] = match['teams'][1]['metadata']
        clean_dict['teamBscore'] = match['scores'][1]
        # Result
        clean_dict['matchResult'] = match['scores']
        # Other Details
        clean_dict['matchKc'] = match['kc']
        clean_dict['matchStatus'] = match['status']
        clean_dict['matchOutcome'] = match['outcome']
        clean_dict['events'] = match['events']
        clean_dict['sport'] = match['sport']
        clean_dict['competition'] = match['competition']
    
        full_dict[match['matchId']] = clean_dict

print('Save Results')
with open("data/raw_data/all_rugby_matches.json", "w") as jfile:
    json.dump(full_dict, jfile)