from bot_filter import BotFilter


if "__main__" == __name__:
    task = BotFilter()
    with task.client:
        task.client.loop.run_until_complete(
            task.process_captcha("pogromista", private=False)
        )
