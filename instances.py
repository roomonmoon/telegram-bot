import os, applogger

from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

logger = applogger.get_logger(__name__)

storage = MemoryStorage()

bot = Bot(token=str(os.getenv('APP_TOKEN')))
dp = Dispatcher(bot=bot, storage=storage)
