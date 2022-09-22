from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, KeyboardButton, ReplyKeyboardMarkup

SEND_MESSAGE = "✉️Xabar yuborish"

send_message_keyboard = ReplyKeyboardMarkup(
    [[KeyboardButton(SEND_MESSAGE)]], resize_keyboard=True, one_time_keyboard=True
)

