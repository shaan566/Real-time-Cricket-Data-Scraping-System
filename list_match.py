from flask import Flask, render_template_string, request
from scraper.fixtures import get_fixtures
from scraper.scorecard import view_scorecard
import json
import os

app = Flask(__name__)

MATCH_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Upcoming Matches from CREX</title>
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background-color: #101820;
            color: #ffffff;
            padding: 20px;
            margin: 0;
        }

        h1 {
            text-align: center;
            color: #ffcc00;
            margin-bottom: 30px;
        }

        .match {
            background-color: #1e2a38;
            padding: 20px;
            margin: 15px auto;
            border-radius: 8px;
            max-width: 800px;
            box-shadow: 0 4px 10px rgba(0,0,0,0.3);
            transition: transform 0.2s ease-in-out;
        }

        .match:hover {
            transform: scale(1.01);
        }

        h2 {
            color: #ffffff;
            margin-bottom: 10px;
        }

        .info {
            color: #bbbbbb;
            font-size: 14px;
            margin: 5px 0;
        }

        .info a {
            color: #00bcd4;
            text-decoration: none;
        }

        .info a:hover {
            text-decoration: underline;
        }
    </style>
</head>
<body>
    <h1>🏏 Upcoming Matches from CREX</h1>
    {% for match in matches %}
        <div class="match">
            <h2>{{ match.title }}</h2>
            <p class="info">🕒 {{ match.start_time }}</p>
            <p class="info">
                🔗 <a href="{{ match.url }}" target="_blank">Live Link</a> |
                📊 <a href="/scorecard?url={{ match.url }}">View Scorecard</a>
            </p>
        </div>
    {% endfor %}
</body>
</html>
"""

@app.route("/")
def home():
    matches = get_fixtures()
    os.makedirs("data", exist_ok=True)
    with open("data/fixtures.json", "w", encoding="utf-8") as f:
        json.dump(matches, f, indent=2)
    return render_template_string(MATCH_TEMPLATE, matches=matches)


@app.route("/scorecard")
def scorecard():
    match_url = request.args.get("url")
    if not match_url:
        return "❌ Match URL missing", 400

    scorecard_html = view_scorecard(match_url)

    return render_template_string(f"""
    <html>
    <head>
        <title>🏏 Scorecard</title>
        <style>
            body {{
                font-family: Arial;
                background-color: #f9f9f9;
                padding: 20px;
            }}
            table {{
                width: 100%;
                border-collapse: collapse;
                margin-bottom: 20px;
            }}
            th, td {{
                border: 1px solid #ccc;
                padding: 8px;
                text-align: center;
            }}
            th {{
                background-color: #222;
                color: #fff;
            }}
            h2 {{
                color: #333;
            }}
            a {{
                display: inline-block;
                margin-top: 20px;
                color: #007BFF;
                text-decoration: none;
            }}
        </style>
    </head>
    <body>
        <h1>📊 Scorecard</h1>
        {scorecard_html}
        <a href="/">← Back to Matches</a>
    </body>
    </html>
    """)

if __name__ == "__main__":
    app.run(debug=True)
