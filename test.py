from instances import db
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, InlineKeyboardButton, InlineKeyboardMarkup
import sqlite3

# buttons = generate_tag_keyboard()

# keyboard = ReplyKeyboardMarkup()

# for i in buttons:
#     keyboard.add(i)

# print(keyboard)

# print(start_keyboard)

print(db.get_price(title="Father"))


# db.cursor.execute("SELECT * FROM `check`").fetchall()