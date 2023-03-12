from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.filters import Text
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram import types, Dispatcher

from keyboards.admin_keyboard import start_admin_keyboard, cancel, removeKeyboard
from instances import bot, db


ADMINS = [446776902, 5277925980]


class AddNewTag(StatesGroup):
    title = State()
    price = State()


class RemoveTag(StatesGroup):
    title = State()
    

async def admin_panel(message: types.Message):
    if message.from_user.id in ADMINS:
        await bot.send_message(message.from_user.id, "Admin panel", reply_markup=start_admin_keyboard())
    else:
        await bot.send_message(message.from_user.id, "You're not admin.")

async def start_ANT(query: types.CallbackQuery):
    if query.from_user.id in ADMINS:
        await AddNewTag.title.set()
        await query.message.answer("Step 1, Send me Title of Tag", reply_markup=cancel)
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
                await message.reply('Tag added successfully.', reply_markup=removeKeyboard)
                await message.answer('Admin panel', reply_markup=start_admin_keyboard())
            else:
                await message.reply('Error value. Please input the digital price NOT TEXT')
                await AddNewTag.price.set()
    else:
        await bot.send_message(message.from_user.id, "You're not admin.")

async def start_removeTag(query: types.CallbackQuery):
    if query.from_user.id in ADMINS:
        await RemoveTag.title.set()
        await query.message.reply("Send me Title of Tag", reply_markup=cancel)
    else:
        await bot.send_message(query.from_user.id, "You're not admin.")

async def remove_Tag(message: types.Message, state: FSMContext):
    if message.from_user.id in ADMINS:
        async with state.proxy() as data:
            data['title'] = message.text
            if db.remove_tag(data['title']) == True:
                await message.reply('Tag was deleted.', reply_markup=removeKeyboard)
                await message.answer('Admin panel', reply_markup=start_admin_keyboard())
                await state.finish()
            else:
                await bot.send_message(message.from_user.id, "Tags is not exists! Check correct value.")
                await RemoveTag.title.set()
    else:
        await bot.send_message(message.from_user.id, "You're not admin.")






async def cancel_handler(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.finish()
    await message.reply(
        "Cancelled.",
        reply_markup=removeKeyboard,
    )
    await bot.send_message(message.from_user.id, "Admin panel", reply_markup=start_admin_keyboard())

def register_handlers_admin(dp : Dispatcher): 
    dp.register_message_handler(cancel_handler, state="*", commands=['cancel'])
    dp.register_message_handler(cancel_handler, Text(equals="cancel", ignore_case=True), state="*")

    dp.register_callback_query_handler(start_ANT, text="addnewtag", state=None)
    dp.register_message_handler(load_title_tag, state=AddNewTag.title)
    dp.register_message_handler(load_price_tag, state=AddNewTag.price)

    dp.register_callback_query_handler(start_removeTag, state=None)
    dp.register_message_handler(remove_Tag, state=RemoveTag.title)


    
    dp.register_message_handler(admin_panel, commands=['moderator', 'admin'])