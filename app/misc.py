from logging import basicConfig, ERROR
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from config import TELEGRAM_TOKEN

bot = Bot(TELEGRAM_TOKEN, parse_mode=types.ParseMode.HTML)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
#webhook
dp.middleware.setup(LoggingMiddleware())

basicConfig(level=ERROR)


def setup():
    import filters
    filters.setup(dp)

    import handlers

    from utils import executor
    executor.setup()
