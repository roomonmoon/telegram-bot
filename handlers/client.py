from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from instances import bot, p2p, db, CHANNEL_ID, CHANNEL_CHAT_ID
from keyboards import start_keyboard, back_button, unban_payment_keyboard, generate_tag_keyboard, tag_payment_keyboard


# logger = applogger.get_logger(__name__)


async def example():
    print(db.remove_timeout_bill())
    if db.get_user_with_timeleft() != []:
        for user in db.get_user_with_timeleft():
            await bot.promote_chat_member(CHANNEL_CHAT_ID, user[0])
            db.remove_user_with_tag(user[0])
            print(f'{user[0]} was demote.')


        

async def process_cancel_callback(query: types.CallbackQuery):
    db.remove_billing_check(bill_id=query.data[6:])
    await query.message.edit_text("Start keyboard", reply_markup=start_keyboard)

async def process_start_command(message: types.Message):
    await message.answer("Start keyboard", reply_markup=start_keyboard)

async def process_start_callback(query: types.CallbackQuery):
    await query.message.edit_text('Start keyboard', reply_markup=start_keyboard)

async def process_check_ban_status_callback(query: types.CallbackQuery):
    channelStatus = await bot.get_chat_member(chat_id=CHANNEL_ID, user_id=query.from_user.id)
    chatStatus = await bot.get_chat_member(chat_id=CHANNEL_CHAT_ID, user_id=query.from_user.id)
    print("Channel: ", channelStatus['status'])
    print("Chat: ", chatStatus['status'])
    if chatStatus['status'] == 'kicked' or channelStatus['status'] == 'kicked':  
        await query.message.edit_text("You're was kicked from the channel", reply_markup=InlineKeyboardMarkup().add(InlineKeyboardButton(text="Payment", callback_data="unban")).add(InlineKeyboardButton(text="Back", callback_data="start")))
    else:
        await query.message.edit_text("You're haven't ban in our channel", reply_markup=back_button)


async def process_unban_callback(query: types.CallbackQuery):
        bill = p2p.bill(amount=1, lifetime=15)
        db.add_billing_check(query.from_user.id, bill.bill_id, None)    
        await query.message.edit_text("Please, make pay and then hold check button. You'll unban in our chat.", reply_markup=unban_payment_keyboard(url=bill.pay_url, bill=str(bill.bill_id)))


async def process_check_billing_status(query: types.CallbackQuery):
    bill = str(query.data[6:])
    info = db.get_billing_check(bill)
    if info != False:
        if str(p2p.check(bill_id=bill).status) == "PAID":
            await bot.unban_chat_member(chat_id=CHANNEL_ID, user_id=query.from_user.id)
            await bot.unban_chat_member(chat_id=CHANNEL_CHAT_ID, user_id=query.from_user.id)
            db.remove_billing_check(bill)
            await query.answer("You're succesfully paid.")
            await query.message.answer("Welcome. You was unbanned in chat. Please don't repeat you misstakes!\n[CHAT:  https://t.me/+4DQ0-5haYmZlZDhi]\n[CHANNEL: https://t.me/+csmgI67BzuthM2Ni]", reply_markup=start_keyboard)
        else:
            await query.answer("You haven't paid yet.")


async def process_show_tags_callback(query: types.CallbackQuery):
    await query.message.edit_text("Avaible tags", reply_markup=generate_tag_keyboard())

async def process_catch_tag_callback(query: types.CallbackQuery):
    user = await bot.get_chat_member(CHANNEL_CHAT_ID, query.from_user.id)
    print(user['status'])
    if user['status'] == "member" or "administrator" or "restricted":
        title = str(query.data[4:])
        price = db.get_price(title)
        bill = p2p.bill(amount=price, lifetime=15)
        db.add_billing_check(query.from_user.id, bill.bill_id, title)
        await query.message.edit_text(f"{title}", reply_markup=tag_payment_keyboard(bill.pay_url, str(bill.bill_id)))
    else:
        await query.message.edit_text("You're not a member! Please join in the chat.", reply_markup=start_keyboard)

async def process_tag_check_billing_status(query: types.CallbackQuery):
    bill = str(query.data[7:])
    info = db.get_billing_check(bill)
    title = db.get_billing_tag(query.from_user.id)
    price = db.get_price(title)
    if info != False:
        if str(p2p.check(bill_id=bill).status) == "WAITING":
            await bot.promote_chat_member(CHANNEL_CHAT_ID, query.from_user.id, can_manage_chat=True)
            await bot.set_chat_administrator_custom_title(CHANNEL_CHAT_ID, query.from_user.id, custom_title=str(title))
            db.add_user_with_tag(query.from_user.id, title)
            db.remove_billing_check(bill)
            await query.message.answer(f"You're succesfully paid. Now you're {title}! My congratulations.", reply_markup=start_keyboard)
        else:
            await query.answer(f"You haven't paid yet. Please pay {price}₽!")
    

def register_handlers_client(dp : Dispatcher):
    dp.register_message_handler(process_start_command, commands=['start']) 
    dp.register_callback_query_handler(process_start_callback, text="start")
    dp.register_callback_query_handler(process_cancel_callback, text_contains="cancel")
    dp.register_callback_query_handler(process_check_ban_status_callback, text="check_ban_status")
    dp.register_callback_query_handler(process_unban_callback, text="unban")   
    dp.register_callback_query_handler(process_check_billing_status, text_contains="check_")
    dp.register_callback_query_handler(process_show_tags_callback, text="tags")
    dp.register_callback_query_handler(process_catch_tag_callback, text_contains="tag_")
    dp.register_callback_query_handler(process_tag_check_billing_status, text_contains="tagpay_")
