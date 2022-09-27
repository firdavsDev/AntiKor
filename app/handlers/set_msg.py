from aiogram import types
from aiogram.dispatcher import FSMContext
from functions import functions
from misc import dp
from states.main_states import Application
from functions.send_to_admin import send_to_admin
from models.Chats import User
from language import ru, uz



@dp.message_handler(state=Application.msg, content_types=types.ContentType.all())
async def set_message(message: types.Message, state: FSMContext):
    msg = message

    await state.update_data(
        {"msg": msg}
    )
    user = User(message.from_user.id)

    # Ma`lumotlarni qayta o'qiymiz
    data = await state.get_data()
    saved = await functions.set_application(data=data, user = user)
    if saved:
        #send msg to admin
        await send_to_admin(msg=message)
    
    status = uz.uz['mes_sent'] if user.lang == 'uz' else ru.ru['mes_sent']
    await message.answer(status)

    # State dan chiqaramiz
    await state.finish()

