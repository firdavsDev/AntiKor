from aiogram.types import ChatType, Message, CallbackQuery

from misc import dp
from models import Chats


@dp.message_handler(chat_type=ChatType.PRIVATE, commands=['start'])
async def send_welcome(message: Message):
    Chats.User(message.from_user.id)
    text = """
/start - Botni qayta ishga tushirish
/dev - Dasturchi haqida
"""
    await message.reply(text,
                        disable_web_page_preview=True, parse_mode="Html")

#dev
@dp.message_handler(chat_type=ChatType.PRIVATE, commands=['dev'])
async def send_welcome(message: Message):
    Chats.User(message.from_user.id)
    text = """
    Dasturchi: @Firdavs_dev* 
"""
    await message.reply(text,
                        disable_web_page_preview=True, parse_mode="Html")

@dp.callback_query_handler(text_startswith=['delete'])
async def _delete_message(query: CallbackQuery):
    await query.message.delete()
