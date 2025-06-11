from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties
from bot.config import BOT_TOKEN
from bot.handlers import start, subscribe, help, support

# Fixed bot initialization with DefaultBotProperties
bot = Bot(
    token=BOT_TOKEN,
    default=DefaultBotProperties(parse_mode=ParseMode.MARKDOWN)
)
dp = Dispatcher()

# Register all handlers
dp.include_router(start.router)
dp.include_router(subscribe.router)
dp.include_router(help.router)
dp.include_router(support.router)