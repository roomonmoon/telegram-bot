import logging, time

from aiogram import types, Dispatcher

from instances import dp, bot, logger
from keyboards import client_kb


async def process_start_keyboard_command(message: types.Message):
    await message.reply('Клавиатуры вызвана', reply_markup=client_kb)

async def process_start_command(message: types.Message):
    logging.info(f'User: {message.from_user.id}; Fullname: {message.from_user.full_name}; Message: {message.text}; Time: {time.asctime()};')
    await message.answer(f"Привет, {message.from_user.full_name}! Это команда /start")

async def process_help_command(message: types.Message):
    logging.info(f'User: {message.from_user.id}; Fullname: {message.from_user.full_name}; Message: {message.text}; Time: {time.asctime()};')
    await message.answer(f"Привет, {message.from_user.full_name}! Это команда /help")

async def process_exit_command(message: types.Message):
    logging.info(f'User: {message.from_user.id}; Fullname: {message.from_user.full_name}; Message: {message.text}; Time: {time.asctime()};')
    await message.answer(f"Привет, {message.from_user.full_name}! Это команда /quit")

def register_handlers_client(dp : Dispatcher):
    dp.register_message_handler(process_start_keyboard_command, commands=['keyboard', 'kb'])
    dp.register_message_handler(process_start_command, commands=['start'])
    dp.register_message_handler(process_help_command, commands=['help'])
    dp.register_message_handler(process_exit_command, commands=['quit'])