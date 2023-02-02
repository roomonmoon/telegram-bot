from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, InlineKeyboardButton, InlineKeyboardMarkup
from instances import db
import applogger

logger = applogger.get_logger(__name__)

back = InlineKeyboardButton('Back', callback_data='start')
back_button = InlineKeyboardMarkup().add(InlineKeyboardButton(text="Back", callback_data="start"))

def start_client_keyboard():
    unban = InlineKeyboardButton('Unban', callback_data='check_ban_status')
    tags = InlineKeyboardButton('Tags', callback_data='tags')
    reset = InlineKeyboardButton('Reset', callback_data='reset')
    keyboard = InlineKeyboardMarkup()
    keyboard.add(unban).add(tags).add(reset)
    return keyboard



def generate_tag_keyboard():
    buttons = InlineKeyboardMarkup()
    for title, price in db.get_tags():
        buttons.add(InlineKeyboardButton(f'{title} — {price}₽', callback_data="tag_"+title))
    return buttons.add(back)

def unban_payment_keyboard(url="", bill=""):
    pay = InlineKeyboardButton(text="Pay", url=url)
    check = InlineKeyboardButton(text="Check", callback_data="check_"+bill)
    cancel = InlineKeyboardButton(text="Cancel", callback_data="cancel"+bill)
    keyboard = InlineKeyboardMarkup()
    keyboard.add(pay).add(check).add(cancel)
    return keyboard

def tag_payment_keyboard(url="", bill=""):
    pay = InlineKeyboardButton(text="Pay", url=url)
    check = InlineKeyboardButton(text="Check", callback_data="tagpay_"+bill)
    cancel = InlineKeyboardButton(text="Cancel", callback_data="cancel"+bill)
    keyboard = InlineKeyboardMarkup()
    keyboard.add(pay).add(check).add(cancel)
    return keyboard

