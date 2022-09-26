from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.callback_data import CallbackData


#language
lang_cb = CallbackData('language','lang')
language_buttons = InlineKeyboardMarkup()
language_buttons.row(
    InlineKeyboardButton("🇺🇿Ўзбекча", callback_data = lang_cb.new(lang='uz')),
    InlineKeyboardButton('🇷🇺Русский', callback_data = lang_cb.new(lang='ru')),

)

