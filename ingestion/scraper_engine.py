import requests
from bs4 import BeautifulSoup
import hashlib
from datetime import datetime
import os

from ingestion.sources import SECTOR_SOURCES


# ---------------- FETCHERS ----------------

def fetch_rss(url):
    response = requests.get(url, timeout=20)
    response.raise_for_status()
    return response.text


# ---------------- PARSERS ----------------

def extract_rss(xml):
    soup = BeautifulSoup(xml, "xml")
    items = soup.find_all("item")

    updates = []
    for item in items[:8]:  # limit for readability
        if item.title:
            updates.append(item.title.text.strip())

    return updates


# ---------------- UTIL ----------------

def content_hash(text):
    return hashlib.md5(text.encode("utf-8")).hexdigest()


# ---------------- MAIN INGESTION ----------------

def run_ingestion():
    print("🚀 Starting ingestion engine...\n")

    for sector, config in SECTOR_SOURCES.items():
        try:
            source_type = config.get("type", "manual")
            updates = []

            # -------- RSS SOURCE (RBI) --------
            if source_type == "rss":
                raw = fetch_rss(config["url"])
                updates = extract_rss(raw)

            # -------- NON-RSS SOURCES --------
            else:
                updates = []

            # -------- PREPARE TEXT --------
            if updates:
                text_blob = (
                    f"[SOURCE] {config['authority']}\n"
                    f"[SECTOR] {sector.upper()}\n\n"
                    + "\n".join(f"- {u}" for u in updates)
                    + f"\n\nLast updated at {datetime.now()}"
                )
            else:
                text_blob = (
                    f"[SOURCE] {config['authority']}\n"
                    f"[SECTOR] {sector.upper()}\n\n"
                    "No extractable policy updates were detected.\n"
                    "This may be due to access restrictions or non-RSS sources.\n\n"
                    f"Last checked at {datetime.now()}"
                )

            # -------- WRITE FILE --------
            os.makedirs(os.path.dirname(config["save_path"]), exist_ok=True)

            with open(config["save_path"], "w", encoding="utf-8") as f:
                f.write(text_blob)

            print(f"📁 File written for {sector}")

        except Exception as e:
            print(f"❌ Error ingesting {sector}: {e}")

    print("\n✅ Ingestion run completed.")


# ---------------- ENTRY ----------------

if __name__ == "__main__":
    run_ingestion()
