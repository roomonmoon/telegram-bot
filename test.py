from aiogram.utils import executor
from instances import db, dp
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, InlineKeyboardButton, InlineKeyboardMarkup
import sqlite3
import time

@message_handler



def main():
    executor.start_polling(dp, skip_updates=True)

if __name__ == "__main__":
    main()