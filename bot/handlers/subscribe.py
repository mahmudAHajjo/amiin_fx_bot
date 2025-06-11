import logging
from aiogram import Router, F
from aiogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
from bot.config import TRC20_ADDRESS, PAYMENTS_CONTACT

# Set up logging at the top of the file
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    filename='logs/bot.log'
)
logger = logging.getLogger(__name__)

router = Router()

# -----------------------------
# Subscription Plan Definitions
# -----------------------------
SUBSCRIPTION_PLANS = {
    "1_month": {"price": "99", "duration": "1 Month"},
    "3_months": {"price": "199", "duration": "3 Months"},
    "lifetime": {"price": "599", "duration": "Lifetime"}
}

# -----------------------------
# Inline Keyboard Markup
# -----------------------------
SUBSCRIPTION_KEYBOARD = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="🥉 1 MONTH ($99)", callback_data="sub_1_month")],
        [InlineKeyboardButton(text="🥈 3 MONTHS ($199)", callback_data="sub_3_months")],
        [InlineKeyboardButton(text="🥇 LIFETIME ($599)", callback_data="sub_lifetime")],
        [InlineKeyboardButton(text="📞 Contact Support", url="https://t.me/amiin_fx10")]
    ]
)

def get_payment_methods_keyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="💳 Pay with USDT (TRC20)", callback_data="payment_trc20")],
            [InlineKeyboardButton(text="💰 Pay with MPESA", callback_data="payment_mpesa")],
            [InlineKeyboardButton(text="🔙 Back to Plans", callback_data="back_to_plans")]
        ]
    )

# -----------------------------
# Handler: Subscribe Button
# -----------------------------
@router.message(F.text == "💼 Subscribe")
async def subscribe_handler(message: Message):
    logger.info(f"Subscribe handler called by user {message.from_user.id}")
    await message.answer(
        "✅ Trade With The XAUUSD EMPEROR!\n\n"
        "Tap on the following products below to subscribe:",
        reply_markup=SUBSCRIPTION_KEYBOARD
    )

# -----------------------------
# Subscription Selection Handler
# -----------------------------
@router.callback_query(F.data.startswith("sub_"))
async def process_subscription(callback_query: CallbackQuery):
    logger.info(f"Subscription selection handler called with data: {callback_query.data}")
    plan_key = callback_query.data.replace("sub_", "")
    logger.debug(f"Processing plan_key: {plan_key}")
    plan_details = SUBSCRIPTION_PLANS.get(plan_key)
    
    if not plan_details:
        logger.error(f"Invalid plan key: {plan_key}")
        await callback_query.answer("⚠️ Invalid subscription option")
        return

    logger.info(f"Selected plan: {plan_details}")

    payment_text = (
        f"VIP Signals {plan_details['duration']} - ${plan_details['price']}.00\n\n"
        "Gain access to our Premium VIP channel on Telegram for "
        f"{plan_details['duration'].lower()} by subscribing to this plan. "
        "Comes with a mix of day trading, swing trading, and occasional "
        "scalping signals—curated for more active traders.\n\n"
        "TERMS & CONDITIONS\n"
        "• Past results do not guarantee future performance. Always ensure "
        "you're using proper risk management and protecting your capital.\n\n"
        "• Use of stolen debit/credit cards is strictly prohibited. If caught, "
        "you'll be banned from the channel permanently.\n\n"
        "• Use only valid emails when subscribing. Your access will be sent "
        "to the email you provide.\n\n"
        "• Do not open disputes or chargebacks. Doing so will lead to a "
        "permanent ban from the community.\n\n"
        "• If you face any payment issues, contact mohamedamiin1301@gmail.com "
        "or message @amiin_fx10 on Telegram.\n\n"
        "• Subscriptions are not automatic. You must manually renew when your "
        "current subscription expires.\n\n"
        "• By purchasing, you agree to receive updates related to Amiin Fx services.\n\n"
        "• Once added to the Premium Channel, please read the pinned "
        "instructions carefully.\n\n"
        "PRIVACY POLICY\n"
        "Your information is never shared with third parties. You may receive "
        "updates related to Forex services.\n\n"
        "REFUND POLICY\n"
        "We have a strict no-refund policy. Refunds are only considered for "
        "duplicate charges or unauthorized transactions.\n\n"
        "Select your preferred payment method below:"
    )

    await callback_query.message.edit_text(
        payment_text,
        parse_mode="HTML",
        reply_markup=get_payment_methods_keyboard()
    )
    await callback_query.answer()

@router.callback_query(F.data == "payment_trc20")
async def handle_trc20_payment(callback_query: CallbackQuery):
    logger.info(f"Processing TRC20 payment for user {callback_query.from_user.id}")
    try:
        first_line = callback_query.message.text.split('\n')[0]
        logger.debug(f"Message first line: {first_line}")
        
        payment_text = (
            f"💎 {first_line}\n\n"
            "💳 USDT (TRC20) Address:\n"
            f"`{TRC20_ADDRESS}`\n\n"
            "📱 After payment, send proof to:\n"
            f"{PAYMENTS_CONTACT}"
        )
        
        await callback_query.message.edit_text(
            payment_text,
            parse_mode="Markdown",
            reply_markup=get_payment_methods_keyboard()
        )
    except Exception as e:
        logger.error(f"Error processing TRC20 payment: {e}", exc_info=True)
    
    await callback_query.answer()

@router.callback_query(F.data == "payment_mpesa")
async def handle_mpesa_payment(callback_query: CallbackQuery):
    logger.info(f"Processing MPESA payment for user {callback_query.from_user.id}")
    try:
        first_line = callback_query.message.text.split('\n')[0]
        logger.debug(f"Message first line: {first_line}")
        
        payment_text = (
            f"💎 {first_line}\n\n"
            "💰 MPESA Payment Details:\n"
            "Paybill: *247247*\n"
            "Account: *0840183797198*\n\n"
            "📱 After payment, send proof to:\n"
            f"{PAYMENTS_CONTACT}"
        )
        
        await callback_query.message.edit_text(
            payment_text,
            parse_mode="Markdown",
            reply_markup=get_payment_methods_keyboard()
        )
    except Exception as e:
        logger.error(f"Error processing MPESA payment: {e}", exc_info=True)
    
    await callback_query.answer()

@router.callback_query(F.data == "back_to_plans")
async def handle_back_to_plans(callback_query: CallbackQuery):
    logger.info(f"Back to plans handler called by user {callback_query.from_user.id}")
    await callback_query.message.edit_text(
        "✅ Trade With The XAUUSD EMPEROR!\n\n"
        "Tap on the following products below to subscribe:",
        reply_markup=SUBSCRIPTION_KEYBOARD
    )
    await callback_query.answer()
