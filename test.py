from instances import db
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, InlineKeyboardButton, InlineKeyboardMarkup
import sqlite3

# buttons = generate_tag_keyboard()

# keyboard = ReplyKeyboardMarkup()

# for i in buttons:
#     keyboard.add(i)

# print(keyboard)

# print(start_keyboard)

db.remove_billing_check(bill_id="WhiteApfel-PyQiwiP2P-91140780-826")

# db.cursor.execute("SELECT * FROM `check`").fetchall()