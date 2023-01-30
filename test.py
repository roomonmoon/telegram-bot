from aiogram.utils import executor
from instances import db, dp
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, InlineKeyboardButton, InlineKeyboardMarkup
import sqlite3

# buttons = generate_tag_keyboard()

# keyboard = ReplyKeyboardMarkup()

# for i in buttons:
#     keyboard.add(i)

# print(keyboard)

# print(start_keyboard)

# print(db.get_price(title="Father"))

result = db.cleeaner()
print(result)
if result != []:
    for i in result:
        print(i[0])
else:
    print('Bad')
# permission = ("can_send_messages: = None", "can_send_media_messages: = None", "can_send_polls: = None", "can_send_other_messages: = None", "can_add_web_page_previews: = None", "can_change_info: = None", "can_invite_users: = None", "can_pin_messages: = None", "can_manage_topics: = None")
# print(permission[0])

# db.cursor.execute("SELECT * FROM `check`").fetchall()