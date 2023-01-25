import os, applogger

from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from pyqiwip2p import QiwiP2P
from pyqiwip2p.p2p_types import QiwiCustomer, QiwiDatetime, PaymentMethods


logger = applogger.get_logger(__name__)

storage = MemoryStorage()

p2p = QiwiP2P(auth_key=str(os.getenv('QIWI_PRIV_KEY')))
bot = Bot(token=str(os.getenv('APP_TOKEN')))
dp = Dispatcher(bot=bot, storage=storage)
