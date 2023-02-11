from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, InlineKeyboardButton, InlineKeyboardMarkup
from instances import db
import applogger

logger = applogger.get_logger(__name__)

removeKeyboard = ReplyKeyboardRemove()

cancel = ReplyKeyboardMarkup()
cancel.add(KeyboardButton("Cancel"))




def start_admin_keyboard():
    addTag = InlineKeyboardButton("Add new tag", callback_data="addnewtag")
    removeTag = InlineKeyboardButton("Remove tag", callback_data="removetag")
    keyboard = InlineKeyboardMarkup()
    return keyboard.add(addTag).add(removeTag)