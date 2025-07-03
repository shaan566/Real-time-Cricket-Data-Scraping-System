from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import json
import os

BASE_URL = "https://crex.com"

def get_fixtures():
    chrome_options = Options()
    chrome_options.add_argument("--headless=new")  # modern headless mode
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")

    service = Service(r"C:\Users\Shaan\OneDrive\Desktop\project2\Assignment\chromedriver-win64\chromedriver.exe")
    driver = webdriver.Chrome(service=service, options=chrome_options)

    print("🔄 Loading match list...")
    driver.get(BASE_URL + "/fixtures/match-list")

    # Save page HTML for debugging
    with open("debug_crex.html", "w", encoding="utf-8") as f:
        f.write(driver.page_source)

    # ✅ Execute JavaScript to extract data directly
    fixtures = driver.execute_script("""
        return Array.from(document.querySelectorAll('a.match-card-wrapper')).map(a => ({
            url: a.href,
            title: Array.from(a.querySelectorAll('span.team-name'))
                        .map(el => el.textContent.trim())
                        .join(' vs '),
            start_time: (a.querySelector('.start-text') || a.querySelector('.liveTag'))?.textContent.trim() || 'TBD'
        }));
    """)

    driver.quit()

    print(f"✅ Found {len(fixtures)} matches.")

    # ✅ Save to JSON
    os.makedirs("data", exist_ok=True)
    with open("data/fixtures.json", "w", encoding="utf-8") as f:
        json.dump(fixtures, f, indent=2)

    return fixtures
