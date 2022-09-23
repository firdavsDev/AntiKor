from aiogram import Dispatcher
from aiogram.utils.executor import Executor

from misc import dp
from utils.set_bot_commands import set_default_commands

runner = Executor(dp)


async def on_startup_polling(dispatcher: Dispatcher):
    # Birlamchi komandalar (/star va /set_lang)
    await set_default_commands(dispatcher)
    #pooling 
    await dispatcher.start_polling()


def setup():
    runner.on_startup(on_startup_polling, webhook=False, polling=True)
    runner.start_polling()
