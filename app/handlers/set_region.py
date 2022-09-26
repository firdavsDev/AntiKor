from aiogram import types
from aiogram.dispatcher import FSMContext
from functions import functions
from misc import dp
from states.main_states import Application


@dp.message_handler(state=Application.region)
async def set_region(message: types.Message, state: FSMContext):
    region = message.text

    await state.update_data(
        {"region": region}
    )
    #save region to database
    status, app = await functions.set_region(message.from_user.id, region=region)
    await message.answer(status)

    await Application.next()

