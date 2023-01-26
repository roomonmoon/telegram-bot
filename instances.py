import os, applogger

from aiogram import Bot, Dispatcher
from aiogram.bot.api import TelegramAPIServer
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from pyqiwip2p import QiwiP2P
from pyqiwip2p.p2p_types import QiwiCustomer, QiwiDatetime, PaymentMethods
from db import Database


logger = applogger.get_logger(__name__)

storage = MemoryStorage()

CHANNEL_CHAT_ID = os.getenv('CHANNEL_CHAT_ID')
CHANNEL_ID = os.getenv('CHANNEL_ID')

db = Database("data.db")
p2p = QiwiP2P(auth_key=str(os.getenv('QIWI_PRIV_KEY')))

bot = Bot(token=str(os.getenv('APP_TOKEN')))
dp = Dispatcher(bot=bot, storage=storage)
