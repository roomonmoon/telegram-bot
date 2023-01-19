import logging, time

from aiogram import types, Dispatcher

from instances import dp, bot
from keyboards import start_keyboard, actions_keyboard


async def process_callback_start(message: types.Message):
    logging.info(f'User: {message.from_user.id}; Fullname: {message.from_user.full_name}; Message: {message.text};')
    await message.answer("Клавиатура вызвана", reply_markup=start_keyboard)


async def process_info_command(message: types.Message):
    logging.info(f'User: {message.from_user.id}; Fullname: {message.from_user.full_name}; Message: {message.text};')
    await message.answer(f"Привет, {message.from_user.full_name}! Это команда /info")

async def process_actions_command(message: types.Message):
    logging.info(f'User: {message.from_user.id}; Fullname: {message.from_user.full_name}; Message: {message.text};')
    await message.answer("Это команда /actions")
    await message.answer("Inline keyboard", reply_markup=actions_keyboard)

async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Нажата кнопка покупки тега')
    

async def process_unban_command(message: types.Message):
    logging.info(f'User: {message.from_user.id}; Fullname: {message.from_user.full_name}; Message: {message.text};')
    await message.answer(f"Привет, {message.from_user.full_name}! Это команда /unban")

def register_handlers_client(dp : Dispatcher):
    dp.register_message_handler(process_callback_start, commands=['start'])
    dp.register_message_handler(process_info_command, commands=['info'])
    dp.register_message_handler(process_actions_command, commands=['actions'])
    dp.register_callback_query_handler(process_callback_button1, lambda c: c.data == '/buytag')
    dp.register_message_handler(process_unban_command, commands=['unban'])