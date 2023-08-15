# main.py

from src import scraper, sms_sender

if __name__ == "__main__":
    verse = scraper.get_verse_of_the_day()
    if verse:
        sms_sender.send_sms(verse)
        print("SMS sent successfully!")
    else:
        print("Failed to fetch the verse.")
