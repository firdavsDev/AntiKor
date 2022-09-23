from aiogram.types import  ChatType, Message
from misc import dp
from models import Chats

from buttons.language import language_buttons


@dp.message_handler(chat_type=ChatType.PRIVATE, commands=['start'])
async def send_welcome(message: Message):
    Chats.User(message.from_user.id)
    text = """
Assalom allaykum Telegram botimizga xush kelibsiz!
"""
    await message.reply(text,
                        disable_web_page_preview=True, parse_mode="Html",
                        reply_markup=language_buttons)

#set_lang
@dp.message_handler(chat_type=ChatType.PRIVATE, commands=['set_lang'])
async def send_welcome(message: Message):
    Chats.User(message.from_user.id)
    text = """
    Tilni tanlang!
"""
    await message.reply(text, 
    disable_web_page_preview=True, parse_mode="Html",
    reply_markup=language_buttons)

