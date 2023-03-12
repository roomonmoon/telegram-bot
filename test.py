from aiogram.utils import executor
from instances import db, dp
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, InlineKeyboardButton, InlineKeyboardMarkup
import sqlite3
import time
import templates

<<<<<<< HEAD


request = db.get_users()

for item in request:
    print(item)
    
=======
request = db.get_users()

for row in range(len(request)):
    print(row)
>>>>>>> aa0d039de93003c80c814d9349615596b025b2e2
