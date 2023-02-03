from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, InlineKeyboardButton, InlineKeyboardMarkup
from instances import db
import applogger

logger = applogger.get_logger(__name__)

removeKeyboard = ReplyKeyboardRemove()

cancel = ReplyKeyboardMarkup()
cancel.add(KeyboardButton("Cancel"))




def start_admin_keyboard():
    addAdmin = InlineKeyboardButton("Add new admin", callback_data="newadmin")
    removeAdmin = InlineKeyboardButton("Remove admin", callback_data="removeadmin") 
    showAdmins = InlineKeyboardButton("Show list of admins", callback_data="listadmins")
    addTag = InlineKeyboardButton("Add new tag", callback_data="addnewtag")
    # changeTag = InlineKeyboardButton("Change tag", callback_data="changetag")
    removeTag = InlineKeyboardButton("Remove tag", callback_data="removetag")
    showUsers = InlineKeyboardButton("Show list of prisoners", callback_data="listusers")
    keyboard = InlineKeyboardMarkup()
    return keyboard.add(addTag).add(removeTag).add(showUsers)