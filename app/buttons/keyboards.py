from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.callback_data import CallbackData
from language import uz, ru
import asyncio


#send application
start_app_cb = CallbackData('application','app')

def send_app_button(user):
    start_app_inline_button = InlineKeyboardMarkup()
    region = uz.uz['send_app'] if user.lang == 'uz' else ru.ru['send_app']
    structure = uz.uz['structure'] if user.lang == 'uz' else ru.ru['structure']

    start_app_inline_button.row(
        InlineKeyboardButton(region, callback_data = start_app_cb.new(app='send_app')),
        InlineKeyboardButton(structure, callback_data = start_app_cb.new(app='select_structure')),
    )
    return start_app_inline_button

