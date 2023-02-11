from aiogram.utils import executor
from instances import db, dp
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, InlineKeyboardButton, InlineKeyboardMarkup
import sqlite3
import time
import templates

request = db.get_users()

for row in range(len(request)):
    print(row)