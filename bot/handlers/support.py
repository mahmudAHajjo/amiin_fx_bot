from aiogram import Router, F
from aiogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters import Command
from bot.config import SUPPORT_EMAIL, SUPPORT_TELEGRAM, PAYMENTS_CONTACT
from bot.keyboards.reply import get_main_keyboard

router = Router()

# Create support keyboard with direct links
def get_support_keyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="📱 Telegram Support", url="https://t.me/amiin_fx10")],
            [InlineKeyboardButton(text="💳 Payment Support", url="https://t.me/AmiinFXpayments")],
            [InlineKeyboardButton(text="📧 Email Support", callback_data="show_email")]
        ]
    )

@router.message(F.text == "📞 Support")
async def support_handler(message: Message):
    try:
        support_text = (
            "🛟 *AMIIN FX Support*\n\n"
            "*Available Support Channels:*\n\n"
            "*General Support:*\n"
            "`@amiin\\_fx10`\n\n"
            "*Payment Support:*\n"
            "`@AmiinFXpayments`\n\n"
            "*Email Support:*\n"
            "`mohamedamiin1301@gmail\\.com`\n\n"
            "_⏱ Response time: 24\\\\-48 hours_\n\n"
            "Choose a support option below:"
        )
        
        await message.answer(
            support_text,
            parse_mode="Markdown",  # Changed back to regular Markdown
            reply_markup=get_support_keyboard()
        )
    except Exception as e:
        print(f"Error in support handler: {e}")

@router.callback_query(F.data == "show_email")
async def show_email(callback: CallbackQuery):
    await callback.message.edit_text(
        "*📧 Email Support Details*\n\n"
        "`mohamedamiin1301@gmail.com`\n\n"
        "*Include in your email:*\n"
        "• Telegram Username\n"
        "• Transaction ID (if payment related)\n"
        "• Clear issue description\n\n"
        "_We'll respond within 24-48 hours_",
        parse_mode="Markdown",
        reply_markup=get_support_keyboard()
    )
    await callback.answer()