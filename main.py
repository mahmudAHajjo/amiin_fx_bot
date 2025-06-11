import asyncio
import logging
from bot.loader import bot, dp
from bot.utils.database import init_db

logging.basicConfig(
    level=logging.INFO,
    filename='logs/bot.log',
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

async def main():
    await init_db()
    print("🤖 Amiin FX Bot is running!")
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())