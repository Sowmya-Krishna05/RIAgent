import requests
from bs4 import BeautifulSoup
import hashlib
import time
from datetime import datetime
import os

from ingestion.sources import SECTOR_SOURCES


def fetch_rss(url):
    r = requests.get(url, timeout=20)
    r.raise_for_status()
    return r.text


def extract_rss(xml):
    soup = BeautifulSoup(xml, "xml")
    items = soup.find_all("item")

    updates = []
    for item in items[:8]:
        updates.append(item.title.text.strip())

    return updates


def content_hash(text):
    return hashlib.md5(text.encode("utf-8")).hexdigest()


def run_ingestion():
    last_hashes = {}

    while True:
        for sector, config in SECTOR_SOURCES.items():
            try:
                # 🔒 RSS-only ingestion
                if config["type"] == "rss":
                    raw = fetch_rss(config["url"])
                    updates = extract_rss(raw)

                # 🔒 Manual sources are not scraped
                elif config["type"] == "manual":
                    continue

                if not updates:
                    continue

                text_blob = "\n".join(updates)
                new_hash = content_hash(text_blob)

                if last_hashes.get(sector) != new_hash:
                    os.makedirs(os.path.dirname(config["save_path"]), exist_ok=True)

                    with open(config["save_path"], "w", encoding="utf-8") as f:
                        f.write(
                            f"[SOURCE] {config['authority']}\n"
                            f"[SECTOR] {sector.upper()}\n\n"
                            "RECENT POLICY UPDATES:\n"
                            + "\n".join(f"- {u}" for u in updates)
                            + f"\n\nLast synced: {datetime.now()}"
                        )

                    print(f"🔔 Update detected in {sector}")
                    last_hashes[sector] = new_hash

            except Exception as e:
                print(f"❌ Error ingesting {sector}: {e}")

        time.sleep(1800)


if __name__ == "__main__":
    run_ingestion()
