from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, InlineKeyboardButton, InlineKeyboardMarkup
import sqlite3, applogger

logger = applogger.get_logger(__name__)

unban = InlineKeyboardButton('Unban', callback_data='check_ban_status')
back = InlineKeyboardButton('Back', callback_data='start')

start_keyboard = InlineKeyboardMarkup()
start_keyboard.add(unban)

back_button = InlineKeyboardMarkup().add(InlineKeyboardButton(text="Back", callback_data="start"))




def generate_tag_keyboard():
    db = sqlite3.connect('data.db')
    sql = db.cursor()
    buttons = InlineKeyboardMarkup()
    for id, title, price in sql.execute("SELECT id,title,price FROM tags"):
        buttons.add(InlineKeyboardButton(f'{title} — {price}₽', callback_data=f'{id}'))
    sql.close()
    return buttons.add(back)

def payment_keyboard(isUrl=True, url="", bill=""):
    keyboard = InlineKeyboardMarkup()
    if isUrl:
        pay = InlineKeyboardButton(text="Pay", url=url)
        keyboard.insert(pay)


    check = InlineKeyboardButton(text="Check", callback_data="check_"+bill)
    back = InlineKeyboardButton(text="Back", callback_data="start")
    keyboard.add(check).add(back)
    return keyboard


