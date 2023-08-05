from captcha_methods.inline_keyboard_captcha import InlineKeyboardCaptcha
from captcha_methods.message_math_captcha import MessageMathCaptcha


class BotCaptchaMethods:
    def __init__(self, client):
        self.client = client
        self.inline_captcha = InlineKeyboardCaptcha(self.client)
        self.message_captcha = MessageMathCaptcha(self.client)

    async def method_one(self, data, channel):
        await self.inline_captcha.inline_keyboard_parse(data, channel)

    async def method_two(self, data, channel):
        await self.message_captcha.message_math_captcha(data, channel)
