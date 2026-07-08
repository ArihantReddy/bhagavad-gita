import json
import random
from pathlib import Path


class QuoteService:
    def __init__(self):
        file_path = Path(__file__).parent.parent / "data" / "gita_quotes.json"

        with open(file_path, "r", encoding="utf-8") as file:
            self.quotes = json.load(file)

    def get_random_quote(self):
        return random.choice(self.quotes)