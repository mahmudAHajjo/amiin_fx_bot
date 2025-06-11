from aiogram import Router, F
from aiogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters import Command
from bot.config import SUPPORT_EMAIL, SUPPORT_TELEGRAM, PAYMENTS_CONTACT, TRC20_ADDRESS

router = Router()

# FAQ items dictionary with proper Markdown formatting
FAQ_ITEMS = {
    "cancel": {
        "question": "I want to cancel my subscription",
        "answer": "*Your subscription details:*\n"
                 "• Not a recurring charge\n"
                 "• One-time payment only\n"
                 "• Manual renewal required after expiry"
    },
    "multiple_charge": {
        "question": "My card was charged multiple times",
        "answer": f"*For multiple charges, contact us:*\n"
                 f"• Email: `{SUPPORT_EMAIL}`\n"
                 f"• Telegram: `{SUPPORT_TELEGRAM}`"
    },
    "no_access": {
        "question": "I did not receive access",
        "answer": f"*To get access:*\n"
                 f"• Send payment proof to `{PAYMENTS_CONTACT}`\n"
                 "• Include your Telegram username\n"
                 "• We'll add you within 24 hours"
    },
    "support": {
        "question": "No response after contacting support",
        "answer": "*Support Response Times:*\n"
                 "• Allow up to 48 hours for response\n"
                 "• We handle all queries in order received"
    },
    "signals": {
        "question": "No signals after subscription",
        "answer": "*About Our Signals:*\n"
                 "• Quality over quantity\n"
                 "• We wait for perfect setups\n"
                 "• Professional analysis takes time\n"
                 "• Signals sent at optimal moments"
    },
    "refund": {
        "question": "I want a refund",
        "answer": "*Refund Policy:*\n"
                 "• Only for duplicate charges\n"
                 "• Only for unauthorized transactions\n"
                 "• No refunds after VIP access granted"
    },
    "contact": {
        "question": "How do I contact support?",
        "answer": f"*Contact Options:*\n"
                 f"• Telegram: `{SUPPORT_TELEGRAM}`\n"
                 f"• Email: `{SUPPORT_EMAIL}`"
    }
}

def get_faq_keyboard():
    keyboard = []
    for key, item in FAQ_ITEMS.items():
        keyboard.append([InlineKeyboardButton(
            text=f"❓ {item['question']}", 
            callback_data=f"faq_{key}"
        )])
    return InlineKeyboardMarkup(inline_keyboard=keyboard)

@router.message(Command("help"))
@router.message(F.text == "❓ Help")
async def help_handler(message: Message):
    help_text = (
        "📚 *Frequently Asked Questions*\n"
        "Select a question below to get help:"
    )
    await message.answer(
        help_text,
        parse_mode="Markdown",
        reply_markup=get_faq_keyboard()  # Show FAQ keyboard
    )

@router.callback_query(F.data.startswith("faq_"))
async def faq_callback(callback: CallbackQuery):
    faq_key = callback.data.replace("faq_", "")
    if faq_key in FAQ_ITEMS:
        await callback.message.edit_text(
            f"*❓ {FAQ_ITEMS[faq_key]['question']}*\n\n"
            f"✅ {FAQ_ITEMS[faq_key]['answer']}\n\n"
            "Select another question or use /help to start over.",
            parse_mode="Markdown",
            reply_markup=get_faq_keyboard()
        )
    await callback.answer()

@router.callback_query(F.data == "payment_trc20")
async def handle_trc20_payment(callback: CallbackQuery):
    payment_text = (
        "*💳 USDT (TRC20) Payment Details*\n\n"
        f"Network: `TRC20`\n"
        f"Address: `{TRC20_ADDRESS}`\n\n"
        "📝 *Instructions:*\n"
        "1. Copy the address above\n"
        "2. Send the exact amount in USDT\n"
        f"3. Send payment proof to {PAYMENTS_CONTACT}"
    )
    await callback.message.edit_text(
        payment_text,
        parse_mode="Markdown",
        reply_markup=get_payment_methods_keyboard()
    )
    await callback.answer()

def get_payment_methods_keyboard():
    keyboard = [
        [InlineKeyboardButton(text="💳 USDT (TRC20)", callback_data="payment_trc20")],
        [InlineKeyboardButton(text="💰 MPESA", callback_data="payment_mpesa")],
        [InlineKeyboardButton(text="⬅️ Back", callback_data="back_to_plans")]
    ]
    return InlineKeyboardMarkup(inline_keyboard=keyboard)

@router.callback_query(F.data == "payment_mpesa")
async def handle_mpesa_payment(callback: CallbackQuery):
    mpesa_text = (
        "*💰 MPESA Payment Details*\n\n"
        "*Business Number:* `247247`\n"
        "*Account Number:* `0840183797198`\n\n"
        "📝 *Instructions:*\n"
        "1. Go to M-PESA\n"
        "2. Select Pay Bill\n"
        "3. Enter Business Number\n"
        "4. Enter Account Number\n"
        "5. Enter Amount\n"
        "6. Enter M-PESA PIN\n\n"
        f"Send payment confirmation to {PAYMENTS_CONTACT}"
    )
    await callback.message.edit_text(
        mpesa_text,
        parse_mode="Markdown",
        reply_markup=get_payment_methods_keyboard()
    )
    await callback.answer()

# Example subscription keyboard (replace with your actual subscription plans)
SUBSCRIPTION_KEYBOARD = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="🔥 1 Month VIP - $50", callback_data="subscribe_1m")],
        [InlineKeyboardButton(text="🔥 3 Months VIP - $120", callback_data="subscribe_3m")],
        [InlineKeyboardButton(text="⬅️ Back", callback_data="back_to_main")]
    ]
)

@router.callback_query(F.data == "back_to_plans")
async def handle_back_to_plans(callback: CallbackQuery):
    await callback.message.edit_text(
        "✅ Trade With The XAUUSD EMPEROR!\n\n"
        "Tap on the following products below to subscribe:",
        reply_markup=SUBSCRIPTION_KEYBOARD
    )
    await callback.answer()