from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types, Dispatcher
from instances import bot

from keyboards.admin_keyboard import start_admin_keyboard

ADMINS = [446776902, 5277925980]

class AddNewAdmin(StatesGroup):
    user_id = State()


async def admin_panel(message: types.Message):
    if message.from_user.id in ADMINS:
        await bot.send_message(message.from_user.id, "Admin panel", reply_markup=start_admin_keyboard())
    else:
        await bot.send_message(message.from_user.id, "Go nahuy")

async def add_new_admin(query: types.CallbackQuery):
    await query.message.edit_text("Send me ID")
    

def register_handlers_admin(dp : Dispatcher): 
    dp.register_message_handler(admin_panel, commands=['moderator', 'admin'])