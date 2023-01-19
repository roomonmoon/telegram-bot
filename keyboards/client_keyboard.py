from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, InlineKeyboardButton, InlineKeyboardMarkup

"""START KEYBOARD START"""

b1 = InlineKeyboardButton('Информация', callback_data='info')
b2 = InlineKeyboardButton('Действия', callback_data='actions')
b3 = InlineKeyboardButton('Разбан', callback_data='unban')

start_keyboard = InlineKeyboardMarkup()
start_keyboard.add(b1).add(b2).add(b3)

"""START KEYBOARD END"""

"""ACTIONS KEYBOARD START"""

b4 = InlineKeyboardButton('Купить тег', callback_data='buytag')
b5 = InlineKeyboardButton('Перевестись в камеру', callback_data='transferme')
b6 = InlineKeyboardButton('Сколько меня ещё кличать будут?', callback_data='checktime')
back = InlineKeyboardButton('Вернуться', callback_data='start')

actions_keyboard = InlineKeyboardMarkup()
actions_keyboard.add(b4).add(b5).add(b6).add(back)

"""ACTIONS KEYBOARD END"""
b7 = InlineKeyboardButton('Купить тег', callback_data='payment_tag')
buytag_keyboard = InlineKeyboardMarkup()
buytag_keyboard.add(b7).add(back)
"""BUYTAG KEYBOARD START"""



"""BUYTAG KEYBOARD END"""

