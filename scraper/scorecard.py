def view_scorecard(match_url):
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.chrome.service import Service
    from selenium.webdriver.common.by import By
    import time

    chrome_options = Options()
    chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")

    service = Service(r"C:\Users\Shaan\OneDrive\Desktop\project2\Assignment\chromedriver-win64\chromedriver.exe")
    driver = webdriver.Chrome(service=service, options=chrome_options)

    print(f"🔍 Opening match: {match_url}")
    driver.get(match_url)
    time.sleep(5)

    html_output = ""

    innings = driver.find_elements(By.CSS_SELECTOR, "div.batsman-table-wrapper")

    for inning in innings:
        try:
            team = inning.find_element(By.CSS_SELECTOR, ".team-name").text.strip()
        except:
            team = "Unknown Team"

        html_output += f"<h2>🏏 {team} Batting</h2><table border='1' cellpadding='8' cellspacing='0'><tr><th>Player</th><th>Dismissal</th><th>Runs</th><th>Balls</th><th>4s</th><th>6s</th><th>SR</th></tr>"

        rows = inning.find_elements(By.CSS_SELECTOR, "table tbody tr")
        for row in rows:
            cols = row.find_elements(By.TAG_NAME, "td")
            if len(cols) >= 6:
                name = cols[0].text.strip()
                dismissal = cols[1].text.strip()
                runs = cols[2].text.strip()
                balls = cols[3].text.strip()
                fours = cols[4].text.strip()
                sixes = cols[5].text.strip()
                sr = cols[6].text.strip() if len(cols) > 6 else "NA"

                html_output += f"<tr><td>{name}</td><td>{dismissal}</td><td>{runs}</td><td>{balls}</td><td>{fours}</td><td>{sixes}</td><td>{sr}</td></tr>"

        html_output += "</table><br>"

    driver.quit()
    return html_output
