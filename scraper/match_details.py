# scraper/match_details.py
from bs4 import BeautifulSoup
from selenium import webdriver
import time

options = webdriver.ChromeOptions()
options.add_argument('--headless')

def get_match_details(match_url):
    driver = webdriver.Chrome(options=options)
    driver.get(match_url)
    time.sleep(3)  # Wait for JS to load

    soup = BeautifulSoup(driver.page_source, 'html.parser')
    
    # Example: Extract match info tab
    match_info = {}
    info_div = soup.find("div", text="Match Info")
    if info_div:
        match_info["venue"] = soup.find("span", string="Venue").find_next_sibling("span").text
    
    # Add similar blocks for squads, live, scorecard
    driver.quit()
    return match_info
