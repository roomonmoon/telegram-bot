from instances import db
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, InlineKeyboardButton, InlineKeyboardMarkup
import sqlite3

# buttons = generate_tag_keyboard()

# keyboard = ReplyKeyboardMarkup()

# for i in buttons:
#     keyboard.add(i)

# print(keyboard)

# print(start_keyboard)
user_id = 1
bill_id = 1233

db.add_billing_check(user_id, bill_id)

# db.cursor.execute("SELECT * FROM `check`").fetchall()