import telethon

from bot_congig.join_group import JoinGroup as BotJoinGroup
from database.methods import DbMethods
from captcha_methods.methods import BotCaptchaMethods


class BotFilter(BotJoinGroup):
    def __init__(self):
        super().__init__()
        self.db_methods = DbMethods()
        self.captcha_methods = BotCaptchaMethods(self.client)
        self.event = None

    async def process_captcha(self, channel, private=False):
        bot_ids = await self.db_methods.get_from_db_all_bot_ids()
        if not await self.join_group(channel, private):
            return
        await self.get_captcha_message(bot_ids)
        callback_data = [self.event] if self.event else None
        if callback_data and callback_data[0].from_id:
            bot_id = int(callback_data[0].from_id.user_id)
            result = await self.db_methods.get_from_db_by_bot_id(bot_id)
            if not result:
                print("Bot not added to database")
                return
            try:
                await self.captcha_methods.__getattribute__(result)(
                    callback_data, channel
                )
            except AttributeError as e:
                print("Captcha method not found", e)
        else:
            print("No callback data received")

    async def get_captcha_message(self, bot_ids):
        @self.client.on(telethon.events.NewMessage())
        async def handler(event):
            self.event = event
            await self.client.disconnect()

        await self.client.run_until_disconnected()
