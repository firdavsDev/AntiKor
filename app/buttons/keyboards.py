from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.callback_data import CallbackData
from language import uz, ru
import asyncio


#send application
send_app_cb = CallbackData('application','app')

def send_app_button(user):
    send_app__inline_button = InlineKeyboardMarkup()
    asyncio.sleep(.05)  #  (Limit: 30 messages per second)
    text = uz.uz['send_app'] if user.lang == 'uz' else ru.ru['send_app']

    send_app__inline_button.row(
        InlineKeyboardButton(text, callback_data = send_app_cb.new(app='send_app')),
    )
    return send_app__inline_button

