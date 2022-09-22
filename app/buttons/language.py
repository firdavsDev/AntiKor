from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

language_buttons = InlineKeyboardMarkup([
    [
        InlineKeyboardButton("🇺🇿O'zbekcha", callback_data = "uz"),
        InlineKeyboardButton('🇷🇺Русский', callback_data = 'ru'),
        
    ]
])
