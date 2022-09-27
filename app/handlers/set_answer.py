

from aiogram import types
from functions import functions
from misc import dp

#log
import logging
logging.basicConfig(level=logging.INFO)
log = logging.getLogger('send answer to user')


@dp.message_handler(is_owner=True,  is_reply=True)
async def send_admin_message(message: types.Message):
    try:
        user_status_txt, admin_response_txt = await functions.set_answer(message.reply_to_message.forward_from.id, answer=message)

        #send user response
        await message.bot.send_message(message.reply_to_message.forward_from.id, user_status_txt)
        #send admin response
        await message.bot.send_message(chat_id=message.from_user.id, text=admin_response_txt, disable_notification=False)
    except Exception as e:
        log.error(e)

