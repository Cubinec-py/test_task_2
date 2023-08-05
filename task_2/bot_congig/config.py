import os

from dotenv import load_dotenv
from pathlib import Path

load_dotenv()


class Config:
    def __init__(self):
        self.api_id = int(os.environ.get("API_ID"))
        self.api_hash = os.environ.get("API_HASH")
        self.session_file = f"{Path.cwd()}/sessions/447471334258.session"
