from aiogram.utils import executor
from instances import db, dp
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, InlineKeyboardButton, InlineKeyboardMarkup
import sqlite3
import time



request = db.get_users()

for item in request:
    print(item)
    
