🏏 Real-time Cricket Data Scraping System
This is a project I built to track live cricket matches — automatically. It scrapes match data (like upcoming fixtures and live scorecards) from CREX and displays everything on a clean web page using Flask.

I wanted to make it easy to:

See upcoming matches

Click and view live scorecards

All from one place, updated in real time.

💡 Why I Built This
I'm a big fan of cricket, and most sports websites are cluttered or full of ads. So I decided to build my own live dashboard where I control how things look, how fast they load, and what I care about — scores.

🔧 What It Does
📅 Shows upcoming matches with date, time, and links.

📊 Lets you click and view scorecards — showing runs, balls, 4s, 6s, and strike rate for each player.

🔁 Can automatically check for new matches every hour in the background (using a scheduler).

🧼 Simple, clean interface styled like CREX’s dark theme.

🧠 What I Learned
How to use Selenium to control a headless browser and scrape dynamic websites.

How to build a Flask app that serves real-time data.

How to schedule jobs in Python (with APScheduler).

And most importantly, how to debug real-world problems — like page delays, empty selectors, or driver issues.
