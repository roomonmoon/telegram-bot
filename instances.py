import os, applogger

from aiogram import Bot, Dispatcher
from aiogram.bot.api import TelegramAPIServer
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from pyqiwip2p import QiwiP2P
from pyqiwip2p.p2p_types import QiwiCustomer, QiwiDatetime, PaymentMethods


logger = applogger.get_logger(__name__)

storage = MemoryStorage()

CHANNEL_CHAT_ID = os.getenv('CHANNEL_CHAT_ID')
CHANNEL_ID = os.getenv('CHANNEL_ID')


p2p = QiwiP2P(auth_key=str(os.getenv('QIWI_PRIV_KEY')))
local_server = TelegramAPIServer.from_base('http://localhost')
bot = Bot(token=str(os.getenv('APP_TOKEN')), server=local_server)
dp = Dispatcher(bot=bot, storage=storage)
