from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardRemove
from language import ru, uz
from misc import dp
from models.Chats import User

from states.main_states import Application


@dp.message_handler(state=Application.structure)
async def set_structure_type(message: types.Message, state: FSMContext):
    structure = message.text
    
    await state.update_data(
        {"structure": structure}
    )

    user = User(message.from_user.id)
    status = uz.uz['message'] if user.lang == 'uz' else ru.ru['message']
    await message.answer(status, reply_markup=ReplyKeyboardRemove(selective=False))

    #next handler
    await Application.msg.set()

