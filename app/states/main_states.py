from aiogram.dispatcher.filters.state import StatesGroup, State


# Shaxsiy ma'lumotlarni yig'sih uchun Application holatdan yaratamiz
class Application(StatesGroup):
    # Foydalanuvchi buyerda 2 ta holatdan o'tishi kerak
    region = State() # Region
    msg = State() # Message
