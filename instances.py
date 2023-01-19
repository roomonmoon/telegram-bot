import os, logging
import datetime
from time import time_ns
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()

# logger = logging.basicConfig(format='%(levelname)s %(asctime)s %(message)s', datefmt='%d/%m/%Y %H:%M:%S', filename=f'logs/{datetime.datetime.now().strftime("%d-%m-%y %H-%M-%S")}.log', encoding='utf-8', level=logging.INFO) 

bot = Bot(token=str(os.getenv('APP_TOKEN')))
dp = Dispatcher(bot=bot, storage=storage)