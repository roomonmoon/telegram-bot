import logging, time

from aiogram import types, Dispatcher
from instances import dp, bot, logger


async def process_start_command(message: types.Message):
    logging.info(f'User: {message.from_user.id}; Fullname: {message.from_user.full_name}; Message: {message.text}; Time: {time.asctime()};')
    await message.answer(f"Привет, {message.from_user.full_name}! Это команда /start")

async def process_help_command(message: types.Message):
    logging.info(f'User: {message.from_user.id}; Fullname: {message.from_user.full_name}; Message: {message.text}; Time: {time.asctime()};')
    await message.answer(f"Привет, {message.from_user.full_name}! Это команда /help")

async def process_exit_command(message: types.Message):
    logging.info(f'User: {message.from_user.id}; Fullname: {message.from_user.full_name}; Message: {message.text}; Time: {time.asctime()};')
    await message.answer(f"Привет, {message.from_user.full_name}! Это команда /exit")

def register_handlers_client(dp : Dispatcher):
    dp.register_message_handler(process_start_command, commands=['start'])
    dp.register_message_handler(process_help_command, commands=['help'])
    dp.register_message_handler(process_exit_command, commands=['exit'])