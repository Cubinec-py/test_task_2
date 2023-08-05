from telethon.sync import TelegramClient
from bot_congig.config import Config as BotConfig


class Connection(BotConfig):
    def __init__(self):
        super().__init__()
        self.client = TelegramClient(self.session_file, self.api_id, self.api_hash)
