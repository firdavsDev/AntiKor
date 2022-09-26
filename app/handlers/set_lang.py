import logging

from aiogram import types
from buttons.keyboards import send_app_cb
from buttons.language import lang_cb
from buttons.regions import region_buttons
from buttons.keyboards import send_app_button

from functions import functions
from models import Chats
from config import OWNER_ID
from language import ru, uz
from misc import dp
from states.main_states import Application

#log
logging.basicConfig(level=logging.INFO)
log = logging.getLogger('set_lang')


#set lang
@dp.callback_query_handler(lang_cb.filter(lang = 'uz'), state=None)
@dp.callback_query_handler(lang_cb.filter(lang='ru'), state=None)
async def set_lang(call: types.CallbackQuery, callback_data: dict):
    user = Chats.User(call.from_user.id)
    status = await functions.set_lang(call.from_user.id, callback_data['lang'])
    if call.from_user.id == OWNER_ID:
        status = uz.uz['updated_lang'] if user.lang == 'uz' else ru.ru['updated_lang']
        await call.message.answer(str(status))
    else:
        await call.message.answer(str(status), reply_markup=send_app_button(user))
    await call.message.delete()
    await call.answer(cache_time=30, show_alert=True)



@dp.callback_query_handler(send_app_cb.filter(app='send_app'), state=None)
async def send_app_state(call: types.CallbackQuery, callback_data: dict):
    user = Chats.User(call.from_user.id)
    status = uz.uz['region'] if user.lang == 'uz' else ru.ru['region']
    await call.message.answer(str(status), reply_markup=region_buttons(user.lang))
    await call.message.delete()
    await call.answer(cache_time=30, show_alert=True)

    #set region state
    await Application.region.set()


