from aiogram import types
from aiogram.dispatcher import FSMContext
from functions import functions
from misc import dp
from states.main_states import Application
from functions.send_to_admin import send_to_admin



@dp.message_handler(state=Application.msg)
async def set_message(message: types.Message, state: FSMContext):
    msg = message.text

    await state.update_data(
        {"msg": msg}
    )
    #save msg to database
    status = await functions.set_msg(message.from_user.id, msg=msg)

    # Ma`lumotlarni qayta o'qiymiz
    # data = await state.get_data()
    # region = data.get("region")
    # msg = data.get("msg")

    # msg = "Quyidai ma`lumotlar qabul qilindi:\n"
    # msg += f"Viloyat - {region}\n"
    # msg += f"Xabar - {msg}\n"
    
    #send msg to admin
    await send_to_admin(msg=message)
    
    await message.answer(status)

    # State dan chiqaramiz
    # 1-variant
    await state.finish()

    # 2-variant
    # await state.reset_state()

    # 3-variant. Ma`lumotlarni saqlab qolgan holda
    # await state.reset_state(with_data=False)

