from aiogram import types, Dispatcher
from instances import bot, p2p, CHANNEL_ID, CHANNEL_CHAT_ID
from keyboards import start_keyboard, payment_keyboard

# logger = applogger.get_logger(__name__)

async def process_start_command(message: types.Message):
    await message.answer("Start keyboard", reply_markup=start_keyboard)


async def process_start_callback(query: types.CallbackQuery):
    await query.message.edit_text('Start keyboard', reply_markup=start_keyboard)

async def process_unban_callback(query: types.CallbackQuery):
    user = await bot.get_chat_member(chat_id=f'{CHANNEL_CHAT_ID}', user_id=query.from_user.id)
    print(user['status'])

    if user['status'] == 'left':
        await query.message.edit_text("You're was kicked from the channel")
        
    else:
        await bot.send_message(query.from_user.id, "You're haven't ban in our channel")


def register_handlers_client(dp : Dispatcher):
    dp.register_message_handler(process_start_command, commands=['start']) 
    dp.register_callback_query_handler(process_start_callback, text="start")
    dp.register_callback_query_handler(process_unban_callback, text="unban")   
