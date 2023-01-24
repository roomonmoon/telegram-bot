from keyboards import generate_tag_keyboard
from keyboards import start_keyboard
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, InlineKeyboardButton, InlineKeyboardMarkup
import sqlite3

# buttons = generate_tag_keyboard()

# keyboard = ReplyKeyboardMarkup()

# for i in buttons:
#     keyboard.add(i)

# print(keyboard)

# print(start_keyboard)

db = sqlite3.connect('data.db')
sql = db.cursor()

var = sql.execute("SELECT title, price FROM tags")

for title, id in sql.execute("SELECT title, price FROM tags"):
    print(title)