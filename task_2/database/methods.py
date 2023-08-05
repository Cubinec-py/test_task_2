from database.connection import Connection as DbConnection


class DbMethods(DbConnection):
    def __init__(self):
        super().__init__()

    async def add_to_db(self, bot_id, call_method):
        db = await self.get_db()
        cursor = await db.execute(self.query.add_to_db, (bot_id, call_method))
        await db.commit()
        await db.close()
        data = await self.get_from_db_by_id(cursor.lastrowid)
        return data

    async def get_from_db_by_bot_id(self, bot_id):
        db = await self.get_db()
        cursor = await db.execute(self.query.get_from_db_by_bot_id, (bot_id,))
        result = await cursor.fetchone()
        await cursor.close()
        await db.close()
        return result[0] if result else None

    async def get_from_db_by_id(self, id):
        db = await self.get_db()
        cursor = await db.execute(self.query.get_from_db_by_id, (id,))
        result = await cursor.fetchone()
        await cursor.close()
        await db.close()
        return result[0] if result else None

    async def get_from_db_all_bot_ids(self):
        db = await self.get_db()
        cursor = await db.execute(self.query.get_from_db_all_bot_ids)
        result = await cursor.fetchall()
        await cursor.close()
        await db.close()
        return [bot_id[0] for bot_id in result] if result else None

    async def delete_from_db(self, bot_id):
        db = await self.get_db()
        await db.execute(self.query.delete_from_db, (bot_id,))
        await db.commit()
        await db.close()
