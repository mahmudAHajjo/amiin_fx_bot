from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def get_main_keyboard():
    keyboard = [
        [
            KeyboardButton(text="💼 Subscribe"),
        ],
        [
            KeyboardButton(text="❓ Help"),
            KeyboardButton(text="📞 Support")
        ]
    ]
    return ReplyKeyboardMarkup(
        keyboard=keyboard,
        resize_keyboard=True,
        input_field_placeholder="Choose an option"
    )