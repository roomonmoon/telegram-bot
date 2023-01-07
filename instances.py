import os, logging
from aiogram import Bot, Dispatcher

logger = logging.basicConfig(level=logging.INFO) 

bot = Bot(token=str(os.getenv('APP_TOKEN')))
dp = Dispatcher(bot=bot)