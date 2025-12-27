from pathway_pipeline import get_relevant_docs

def answer_question(question):
    docs, last_updated = get_relevant_docs(question)

    if not docs:
        return "", last_updated

    important_lines = []

    JUNK_KEYWORDS = [
        "skip to main content", "selected language", "search the website",
        "home", "about us", "contact us", "archives", "all months",
        "facebook", "twitter", "linkedin", "youtube", "app store",
        "play store", "sitemap", "disclaimer", "copyright"
    ]

    for doc in docs:
        for line in doc.split("\n"):
            clean = line.strip()
            lower = clean.lower()

            # Skip junk lines
            if len(clean) < 40:
                continue
            if any(junk in lower for junk in JUNK_KEYWORDS):
                continue

            # Keep only policy-relevant lines
            if (
                "amendment" in lower
                or "directions" in lower
                or "guidelines" in lower
                or "notification" in lower
                or "eligibility" in lower
            ):
                important_lines.append(clean)

    # HARD LIMIT — THIS IS CRITICAL
    important_lines = important_lines[:8]

    if not important_lines:
        return "", last_updated

    answer = (
        "KEY POLICY UPDATES:\n\n"
        + "\n".join(f"- {line}" for line in important_lines)
    )

    return answer, last_updated
