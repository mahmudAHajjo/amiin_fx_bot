from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command
from bot.keyboards.reply import get_main_keyboard

router = Router()

@router.message(Command("start"))
async def cmd_start(message: Message):
    await message.answer(
        "👋 Welcome to AMIIN FX Bot!\n\n"
        "Choose an option from the menu below:",
        reply_markup=get_main_keyboard()
    )