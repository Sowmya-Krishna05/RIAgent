import os
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")


def read_sector_file(sector):
    sector_dir = os.path.join(DATA_DIR, sector)

    if not os.path.exists(sector_dir):
        return ""

    for fname in os.listdir(sector_dir):
        if fname.endswith(".txt"):
            with open(os.path.join(sector_dir, fname), "r", encoding="utf-8") as f:
                return f.read()

    return ""


def detect_sector(question: str):
    q = question.lower()

    if any(k in q for k in ["rbi", "bank", "banks", "finance"]):
        return "finance"
    if any(k in q for k in ["ugc", "student", "education"]):
        return "education"
    if any(k in q for k in ["health", "hospital", "medical"]):
        return "healthcare"
    if any(k in q for k in ["labour", "worker", "employment"]):
        return "labour"
    if any(k in q for k in ["digital", "it", "technology"]):
        return "digital"

    return None


def answer_question(question: str):
    sector = detect_sector(question)

    if not sector:
        return (
            "No directly matching policy updates were found for this query.",
            None,
        )

    content = read_sector_file(sector)

    if not content.strip():
        return (
            f"[{sector.upper()} – KEY UPDATES]\n\n"
            "Policy data is currently unavailable for this sector.",
            datetime.now(),
        )

    # Extract bullet points if present
    bullets = [line.strip() for line in content.splitlines() if line.strip().startswith("-")]

    # 🔒 CRITICAL FIX: ALWAYS RETURN CONTENT
    if bullets:
        answer = f"[{sector.upper()} – KEY UPDATES]\n\n" + "\n".join(bullets)
    else:
        # Fallback: return first meaningful lines
        meaningful = [
            line.strip()
            for line in content.splitlines()
            if len(line.strip()) > 30
        ][:5]

        answer = f"[{sector.upper()} – KEY UPDATES]\n\n" + "\n".join(meaningful)

    return answer, datetime.now()
