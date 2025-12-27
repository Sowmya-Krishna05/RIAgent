"""
Simulates internet updates by modifying policy files automatically.
In production, this represents web scrapers / RSS feeds / APIs.
"""

import time
from datetime import datetime

FILE_PATH = "data/education/ugc_policy.txt"

def simulate_update():
    while True:
        time.sleep(60)  # every 60 seconds (demo-friendly)

        with open(FILE_PATH, "w", encoding="utf-8") as f:
            f.write(
                f"UGC scholarship eligibility requires income below 5 LPA.\n"
                f"Updated at {datetime.now()}"
            )

        print("🔔 Internet update simulated for Education policy")

if __name__ == "__main__":
    simulate_update()
