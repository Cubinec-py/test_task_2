class SqlQuery:
    def __init__(self):
        self.create_table = (
            "CREATE TABLE IF NOT EXISTS bot_list "
            "(id INTEGER PRIMARY KEY AUTOINCREMENT, bot_id INTEGER, call_method TEXT)"
        )
        self.add_to_db = "INSERT INTO bot_list (bot_id, call_method) VALUES (?, ?)"
        self.get_from_db_by_bot_id = "SELECT call_method FROM bot_list WHERE bot_id = ?"
        self.get_from_db_by_id = "SELECT call_method FROM bot_list WHERE id = ?"
        self.delete_from_db = "DELETE FROM bot_list WHERE bot_id = ?"
        self.get_from_db_all_bot_ids = "SELECT bot_id FROM bot_list"
