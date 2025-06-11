import asyncio
from bot.utils.logging import setup_logging
from bot.loader import bot, dp

def main():
    setup_logging()
    asyncio.run(dp.start_polling(bot))

if __name__ == '__main__':
    main()