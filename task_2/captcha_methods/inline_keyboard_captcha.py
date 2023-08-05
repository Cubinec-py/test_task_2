class InlineKeyboardCaptcha:
    def __init__(self, client):
        super().__init__()
        self.client = client
        self.captcha_text = "👉🏻Я НЕ БОТ👈🏻"

    async def inline_keyboard_parse(self, callback_data, channel=None):
        if not self.client.is_connected():
            await self.client.connect()
        await callback_data[0].message.click(text=self.captcha_text)
