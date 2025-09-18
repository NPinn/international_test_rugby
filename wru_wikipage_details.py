### Produce JSON file containing all WRU Tournament Detials and Other Matches
## Details broken down by year

## Import Packages
import re
from datetime import datetime
import json
from wikipedia_scraper import fetch_wikipedia_page

# Establish Name of WRU Wikipedia Page Name
print("Extracting Page Details")
page_name = "List of women's international rugby union test matches"

# Get Page Details
page_details = fetch_wikipedia_page(page_name)

# Get Current Year
## Extracts away year, making this (hopefully) future proof
today = datetime.today()
current_year = today.year

print("Breaking Down Tournaments and Matches per Year")
# Loop Through Wikipedia Page, breaking down Tournaments and Other Matches for each year
full_dict = {}
for year in range(1982, current_year+1):
    year_dict = {}
    
    year_str = str(year)
    match = re.findall(rf"({year_str}\[edit\].*?){year+1}\[edit\]|({year_str}\[edit\].*?)Notes\[edit\]", page_details, flags=re.DOTALL|re.I)

    if match[0][0] != '':
        details = match[0][0]
    else:
        details = match[0][1]

    tournament_match = re.findall(r"Tournaments\[edit\](.*)Other", details, flags=re.DOTALL|re.I)[0]
    if tournament_match == "\nNone\n" or tournament_match == "\nNone\n\n":
        year_dict['tournaments'] = None
    else:
        year_dict['tournaments'] = tournament_match
    
    other_matches_match = re.findall(r"Other matches\[edit\](.*)", details, flags=re.DOTALL|re.I)[0]
    year_dict['other_matches'] = other_matches_match
    
    
    full_dict[year_str] = year_dict

print("Writing Dictionary to Json file")
print("File Name: wru_yearly_breakdown_messy.json in data/raw_data")
with open("data/raw_data/wru_yearly_breakdown_messy.json", "w") as jfile:
    json.dump(full_dict, jfile)