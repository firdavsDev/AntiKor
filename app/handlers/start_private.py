from aiogram.types import ChatType, Message, ParseMode
from buttons.keyboards import send_app_button
from buttons.language import language_buttons
from config import OWNER_ID
from language import ru, uz
from misc import dp
from models import Chats


@dp.message_handler(chat_type=ChatType.PRIVATE, commands=['start'])
async def send_welcome(message: Message):
    user = Chats.User(message.from_user.id)
    text = ru.ru['start'] if user.lang == 'ru' else uz.uz['start']
    if user.lang is None:
        await message.reply(text,
                    disable_web_page_preview=True, parse_mode=ParseMode.HTML,
                        reply_markup=language_buttons)
    elif message.from_user.id == OWNER_ID:
        text = ru.ru['welcome_admin'] if user.lang == 'ru' else uz.uz['welcome_admin']
        await message.reply(text,
            disable_web_page_preview=True, parse_mode=ParseMode.HTML)
    else:
        await message.reply(text,
            disable_web_page_preview=True, parse_mode=ParseMode.HTML,
                reply_markup=send_app_button(user))
        
#set_lang
@dp.message_handler(chat_type=ChatType.PRIVATE, commands=['set_lang'])
async def set_lang(message: Message):
    user = Chats.User(message.from_user.id)
    text = uz.uz['set_lang'] if user.lang == 'uz' else ru.ru['set_lang']

    await message.reply(text, disable_web_page_preview=True, 
        parse_mode=ParseMode.HTML, 
            reply_markup=language_buttons)

