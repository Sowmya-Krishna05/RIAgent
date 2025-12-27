import os
from datetime import datetime

BASE_DIR = "data"

def get_relevant_docs(query: str):
    docs = []
    last_updated = None
    query_words = set(query.lower().split())

    for domain in os.listdir(BASE_DIR):
        domain_path = os.path.join(BASE_DIR, domain)
        if not os.path.isdir(domain_path):
            continue

        for file in os.listdir(domain_path):
            if not file.endswith(".txt"):
                continue

            file_path = os.path.join(domain_path, file)
            with open(file_path, "r", encoding="utf-8") as f:
                lines = f.readlines()

            relevant = [
                line for line in lines
                if any(word in line.lower() for word in query_words)
            ]

            if relevant:
                docs.append(
                    f"[{domain.upper()} – KEY UPDATES]\n"
                    + "\n".join(relevant[:5])  # show only top 5
                )

            modified = datetime.fromtimestamp(os.path.getmtime(file_path))
            if last_updated is None or modified > last_updated:
                last_updated = modified

    return docs, last_updated
