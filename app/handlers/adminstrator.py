from aiogram import types

from functions import send_to_alls
from misc import dp
from models import Chats


@dp.message_handler(is_owner=True,text=['/send'],  is_reply=True)
async def admin(message: types.Message):
    keyboard_markup = types.InlineKeyboardMarkup()

    keyboard_markup.add(
        types.InlineKeyboardButton('Yuborish', callback_data='send-all'),
    )
    await message.reply_to_message.reply("Barchasi to'g'ri bo'lsa yuborish tugmasini bosing",
                                         reply_markup=keyboard_markup)


@dp.callback_query_handler(text=['send-all'])
async def answer_call(query: types.CallbackQuery):
    await query.message.edit_text("Yuborilmoqda...")
    send_wait = await send_to_alls.broadcaster(query.message.reply_to_message)
    await query.message.edit_text(str(send_wait))


@dp.message_handler(is_owner=True, commands=['test'])
async def _(message: types.Message):
    Stat = Chats.Statistica()
    await message.reply(f"Userlar: {Stat[0]}\nBarcha musiqalar: {Stat[1]}")
