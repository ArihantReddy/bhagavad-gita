import json
import random
from pathlib import Path


class QuoteService:
    def __init__(self):
        file_path = Path(__file__).parent.parent / "data" / "gita_quotes.json"

        if not file_path.exists():
            raise FileNotFoundError(
                f"Quotes file not found: {file_path}"
            )

        with open(file_path, "r", encoding="utf-8") as file:
            self.quotes = json.load(file)

        if not self.quotes:
            raise ValueError("No Bhagavad Gita quotes found in JSON file.")

        print(f"Loaded {len(self.quotes)} Bhagavad Gita quotes.")

    def get_random_quote(self):
        return random.choice(self.quotes)