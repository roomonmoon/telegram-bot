from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, InlineKeyboardButton, InlineKeyboardMarkup
import sqlite3, applogger, payment

logger = applogger.get_logger(__name__)

unban = InlineKeyboardButton('Unban', callback_data='unban')
back = InlineKeyboardButton('Back', callback_data='start')

start_keyboard = InlineKeyboardMarkup()
start_keyboard.add(unban)



def generate_tag_keyboard():
    db = sqlite3.connect('data.db')
    sql = db.cursor()
    buttons = InlineKeyboardMarkup()
    for id, title, price in sql.execute("SELECT id,title,price FROM tags"):
        buttons.add(InlineKeyboardButton(f'{title} — {price}₽', callback_data=f'{id}'))
    sql.close()
    return buttons.add(back)

def payment_keyboard(billing_url, billing_id):
    pay = InlineKeyboardButton(text="Pay", url=f"{billing_url}")
    check = InlineKeyboardButton(text="Check", callback_data="CheckPaymentStatus")
    back = InlineKeyboardButton(text="Back", callback_data="start")
    keyboard = InlineKeyboardMarkup()
    keyboard.add(pay).add(check).add(back)
    return keyboard


