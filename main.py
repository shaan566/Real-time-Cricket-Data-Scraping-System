import sys
import os
import time
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from scheduler import scheduler

print("Cricradio Scraper Started. Monitoring Fixtures...")
try:
    while True:
        time.sleep(10)
except (KeyboardInterrupt, SystemExit):
    scheduler.shutdown()
    print(" Scraper stopped.")

