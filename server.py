import asyncio
import logging
import time
import os

from aiogram import Bot, Dispatcher, executor, types 
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

logging.basicConfig(level=logging.INFO)

APP_TOKEN = str(os.getenv('APP_TOKEN'))

bot = Bot(token=str(APP_TOKEN))
dp = Dispatcher(bot=bot)


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    logging.info(f'User: {message.from_user.id}; Fullname: {message.from_user.full_name}; Message: {message.text}; Time: {time.asctime()};')
    await message.answer(f"Привет, {message.from_user.full_name}!")
    pass


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
