# scheduler.py
from apscheduler.schedulers.background import BackgroundScheduler
from scraper.fixtures import get_fixtures
from scraper.match_details import get_match_details

import json
import time

scheduled_matches = set()

def check_and_schedule():
    matches = get_fixtures()
    for match in matches:
        if match["url"] not in scheduled_matches:
            scheduled_matches.add(match["url"])
            print(f"Scheduling job for: {match['title']}")
            scheduler.add_job(scrape_match_data, 'date', run_date=match["start_time"], args=[match["url"]])

def scrape_match_data(match_url):
    data = get_match_details(match_url)
    with open("data/matches.json", "a") as f:
        json.dump({match_url: data}, f)
        f.write("\n")

scheduler = BackgroundScheduler()
scheduler.add_job(check_and_schedule, 'interval', minutes=60)
scheduler.start()
