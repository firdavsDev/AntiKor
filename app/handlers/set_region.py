from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardRemove
from language import ru, uz
from misc import dp
from models.Chats import User

from states.main_states import Application


@dp.message_handler(state=Application.region)
async def set_region(message: types.Message, state: FSMContext):
    region = message.text

    await state.update_data(
        {"region": region}
    )

    user = User(message.from_user.id)
    status = uz.uz['message'] if user.lang == 'uz' else ru.ru['message']
    await message.answer(status, reply_markup=ReplyKeyboardRemove(selective=False))

    #next handler
    await Application.next()

