import os

from telethon import TelegramClient
from dotenv import load_dotenv

load_dotenv()


class Bot:
    def __init__(self):
        self.api_id = int(os.environ.get("API_ID"))
        self.api_hash = os.environ.get("API_HASH")
        self.session_file = "447477445692.session"
        # self.session_file = '447471334258.session'
        self.client = TelegramClient(self.session_file, self.api_id, self.api_hash)

    async def main(self):
        for dialog in await self.client.get_dialogs():
            print(dialog)


if __name__ == "__main__":
    bot = Bot()
    with bot.client:
        bot.client.loop.run_until_complete(bot.main())
