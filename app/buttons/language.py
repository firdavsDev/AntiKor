from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

#language
language_buttons = InlineKeyboardMarkup()
language_buttons.row(
    InlineKeyboardButton("🇺🇿O'zbekcha", callback_data = "uz"),
    InlineKeyboardButton('🇷🇺Русский', callback_data = 'ru'),

)

