from aiogram import types, Dispatcher
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, InlineKeyboardButton, InlineKeyboardMarkup
from instances import dp, bot
from keyboards import start_keyboard, actions_keyboard, generate_tag_keyboard
from templates import *
import sqlite3

# logger = applogger.get_logger(__name__)

async def process_start_command(message: types.Message):
    await message.answer("Стартовая клавиатура!", reply_markup=start_keyboard)

async def process_start_callback(query: types.CallbackQuery):
    await query.message.edit_text('Главное меню', reply_markup=start_keyboard)

async def process_unban_callback(query: types.CallbackQuery):
    user = await bot.get_chat_member(chat_id=CHANNEL_CHAT_ID, user_id=query.from_user.id)
    print(user)
    if user['status'] == 'left':
        await query.message.edit_text("Стоимость разблокировки стоит 2 рубля.", reply_markup=InlineKeyboardMarkup().add(InlineKeyboardButton(text='Оплатить', callback_data='unban')).add(InlineKeyboardButton(text='Проверить оплату', callback_data='checkpayment')).add(InlineKeyboardButton(text='Вернуться', callback_data='start')))
    
    else:
        await query.message.edit_text("Вы не имеете блокировок на этом аккаунте.", reply_markup=InlineKeyboardMarkup().add(InlineKeyboardButton(text='Вернуться', callback_data='start')))


async def process_actions_callback(query: types.CallbackQuery):
    await query.message.edit_text('Доступные действия на данный момент!', reply_markup=actions_keyboard)

async def process_buytag_callback(query: types.CallbackQuery):
    await query.message.edit_text('Список доступных тегов:', reply_markup=generate_tag_keyboard())

async def process_buytag__payment_callback(query: types.CallbackQuery):
    await query.message.edit_text(f"", reply_markup=InlineKeyboardMarkup().add(InlineKeyboardButton(text='Оплатить', callback_data='buytag')).add(InlineKeyboardButton(text='Проверить оплату', callback_data='checkpayment')))
    # await query.message.edit_text(f'{query.data.title()}', reply_markup=payment_keyboard(title, price))
    # pass

def register_handlers_client(dp : Dispatcher):
    dp.register_message_handler(process_start_command, commands=['start'])
    dp.register_callback_query_handler(process_start_callback, text="start")
    dp.register_callback_query_handler(process_unban_callback, text="unban")
    dp.register_callback_query_handler(process_actions_callback, text="actions")
    dp.register_callback_query_handler(process_buytag_callback, text="buytag")
    dp.register_callback_query_handler(process_buytag__payment_callback, lambda tag: tag.data)   

    # dp.register_callback_query_handler(process_callback_button1, lambda c: c.data == '/buytag')