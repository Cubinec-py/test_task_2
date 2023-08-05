from pathlib import Path


class Config:
    def __init__(self):
        self.db_path = f"{Path.cwd()}/bot_list.db"
        print(self.db_path)

    @staticmethod
    def check_db_path():
        here = Path.cwd().parent
        return (here / "bot_list.db").exists()
