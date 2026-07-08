import json
import time
import requests
from bs4 import BeautifulSoup

BASE_URL = "https://www.srimadgita.com"

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/138.0.0.0 Safari/537.36"
    )
}

# Official Bhagavad Gita verse counts
CHAPTERS = [
    (1, 47),
    (2, 72),
    (3, 43),
    (4, 42),
    (5, 29),
    (6, 47),
    (7, 30),
    (8, 28),
    (9, 34),
    (10, 42),
    (11, 55),
    (12, 20),
    (13, 35),
    (14, 27),
    (15, 20),
    (16, 24),
    (17, 28),
    (18, 78),
]

quotes = []
quote_id = 1


def scrape_verse(chapter, verse):

    url = f"{BASE_URL}/verse/chapter-{chapter}-verse-{verse}"

    try:

        response = requests.get(
            url,
            headers=HEADERS,
            timeout=30
        )

        if response.status_code != 200:
            print(f"Skipped {chapter}:{verse}")
            return None

        soup = BeautifulSoup(response.text, "lxml")

        translation = soup.select_one("p.translation-text")

        if translation is None:
            print(f"No translation found -> Chapter {chapter}, Verse {verse}")
            return None

        return {
            "id": 0,
            "chapter": chapter,
            "verse": verse,
            "quote": translation.get_text(" ", strip=True)
        }

    except Exception as e:

        print(f"Error at Chapter {chapter} Verse {verse}")
        print(e)
        return None


print("Starting scraper...\n")

for chapter, total in CHAPTERS:

    print(f"========== Chapter {chapter} ({total} verses) ==========")

    for verse in range(1, total + 1):

        print(f"Verse {verse}")

        result = scrape_verse(chapter, verse)

        if result:

            result["id"] = quote_id
            quote_id += 1

            quotes.append(result)

        time.sleep(0.5)

print("\nSaving JSON...")

with open("gita_quotes.json", "w", encoding="utf-8") as f:

    json.dump(
        quotes,
        f,
        ensure_ascii=False,
        indent=4
    )

print("\nFinished.")
print(f"Total quotes saved: {len(quotes)}")