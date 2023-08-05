import aiosqlite

from database.config import Config as DbConfig
from database.sql_queries import SqlQuery


class Connection(DbConfig):
    def __init__(self):
        super().__init__()
        self.query = SqlQuery()

    async def create_db(self):
        async with aiosqlite.connect(self.db_path) as db:
            await db.execute(self.query.create_table)
            await db.commit()

    async def get_db(self):
        if not self.check_db_path():
            await self.create_db()
        db = await aiosqlite.connect(self.db_path)
        db.row_factory = aiosqlite.Row
        return db
