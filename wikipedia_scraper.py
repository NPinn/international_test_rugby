## wikipedia_scraper.py
# Looks to scrape a given wikipedia page
# Scrapes the given page as html and then converts to plain text

import requests
from bs4 import BeautifulSoup

# Base API URL and headers
WIKI_API_URL = "https://en.wikipedia.org/w/api.php"
HEADERS = {
    "User-Agent": "npinnock_wiki_scraper/0.0.1 (https://github.com/NPinn; nathan.pinnock@hotmail.com)"
}

def fetch_wikipedia_page(title: str) -> dict:
    """
    Fetch full details of a Wikipedia page, including text, links, images, categories, coordinates, and infobox data.
    Returns a dictionary with structured information.
    """
    params = {
        "action": "parse",
        "format": "json",
        "page": title,
        "prop": "text"
    }
    
    response = requests.get(WIKI_API_URL, headers=HEADERS, params=params)
    data = response.json()
    
    html = data["parse"]["text"]["*"]
    soup = BeautifulSoup(html, "html.parser")

    plain_text = soup.get_text()

    return plain_text