from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types, Dispatcher
from instances import bot, db

from keyboards.admin_keyboard import start_admin_keyboard

ADMINS = [446776902, 5277925980]

class AddNewTag(StatesGroup):
    title = State()
    price = State()

async def admin_panel(message: types.Message):
    if message.from_user.id in ADMINS:
        await bot.send_message(message.from_user.id, "Admin panel", reply_markup=start_admin_keyboard())
    else:
        await bot.send_message(message.from_user.id, "You're not admin.")

async def start_ANT(query: types.CallbackQuery):
    if query.from_user.id in ADMINS:
        await AddNewTag.title.set()
        await query.message.answer("Step 1, Send me Title of Tag")
    else:
        await bot.send_message(query.from_user.id, "You're not admin.")

async def load_title_tag(message: types.Message, state: FSMContext):
    if message.from_user.id in ADMINS:
        async with state.proxy() as data:
            data['title'] = message.text
            await AddNewTag.next()
            await message.reply('Send 2, Send me price')
    else:
        await bot.send_message(message.from_user.id, "You're not admin.")

async def load_price_tag(message: types.Message, state: FSMContext):
    if message.from_user.id in ADMINS:
        async with state.proxy() as data:
            if message.text.isdigit():
                data['price'] = message.text
                db.add_tag(data['title'], data['price'])
                await state.finish()    
            else:
                await message.reply('Error value. Please input the digital price NOT TEXT')
                await AddNewTag.price.set()
    else:
        await bot.send_message(message.from_user.id, "You're not admin.")


def register_handlers_admin(dp : Dispatcher): 
    dp.register_callback_query_handler(start_ANT, text="newtag", state=None)
    dp.register_message_handler(load_title_tag, state=AddNewTag.title)
    dp.register_message_handler(load_price_tag, state=AddNewTag.price)
    dp.register_message_handler(admin_panel, commands=['moderator', 'admin'])