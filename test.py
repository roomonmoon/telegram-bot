from instances import db
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, InlineKeyboardButton, InlineKeyboardMarkup
import sqlite3

# buttons = generate_tag_keyboard()

# keyboard = ReplyKeyboardMarkup()

# for i in buttons:
#     keyboard.add(i)

# print(keyboard)

# print(start_keyboard)

# print(db.get_price(title="Father"))

print(db.add_user_with_tag(123, "Хуила"))

# permission = ("can_send_messages: = None", "can_send_media_messages: = None", "can_send_polls: = None", "can_send_other_messages: = None", "can_add_web_page_previews: = None", "can_change_info: = None", "can_invite_users: = None", "can_pin_messages: = None", "can_manage_topics: = None")
# print(permission[0])

# db.cursor.execute("SELECT * FROM `check`").fetchall()