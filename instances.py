import os, logging
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()
logger = logging.basicConfig(level=logging.INFO) 

bot = Bot(token=str(os.getenv('APP_TOKEN')))
dp = Dispatcher(bot=bot, storage=storage)