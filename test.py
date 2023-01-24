from keyboards import generate_tag_keyboard
from keyboards import start_keyboard
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, InlineKeyboardButton, InlineKeyboardMarkup
import asyncio

buttons = generate_tag_keyboard()

keyboard = ReplyKeyboardMarkup()

for i in buttons:
    keyboard.add(i)

print(keyboard)

print(start_keyboard)