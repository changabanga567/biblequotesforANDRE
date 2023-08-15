# src/scraper.py

import requests
from bs4 import BeautifulSoup

def get_verse_of_the_day():
    url = 'https://www.verseoftheday.com/'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Assuming the verse is in a tag with a specific class (this might need adjustment based on website structure)
    verse_tag = soup.find('tag_name', class_='specific_class')  # Replace 'tag_name' and 'specific_class' appropriately
    verse = verse_tag.text if verse_tag else None

    return verse
