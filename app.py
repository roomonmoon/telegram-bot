from data import TOKEN

import time
import logging

from aiogram import Bot, Dispatcher, executor, types 

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot)

@dp.message_handler()
async def start_handler(message: types.Message):
    user_id = message.from_user.id
    full_name = message.from_user.full_name
    logging.info(f'{message.text}')

    await message.reply(f'Привет, {full_name}!')

if __name__ == "__main__":
    executor.start_polling(dp)
