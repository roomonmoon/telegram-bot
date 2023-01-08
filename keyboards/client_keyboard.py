from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

b1 = KeyboardButton('/start')
b2 = KeyboardButton('/help')
b3 = KeyboardButton('/quit')

client_kb = ReplyKeyboardMarkup()

client_kb.add(b1).add(b2).add(b3)