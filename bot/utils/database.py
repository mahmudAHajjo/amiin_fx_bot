import aiosqlite
from datetime import datetime, timedelta

DATABASE_PATH = 'data/subscriptions.db'

async def init_db():
    async with aiosqlite.connect(DATABASE_PATH) as db:
        await db.execute('''
            CREATE TABLE IF NOT EXISTS subscriptions (
                user_id INTEGER PRIMARY KEY,
                username TEXT,
                subscription_type TEXT,
                start_date DATE,
                expiry_date DATE
            )
        ''')
        await db.commit()