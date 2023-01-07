from aiogram.utils import executor
from instances import dp

async def on_startup(_):
    print("Bot online")

from handlers import client, admin, other

client.register_handlers_client(dp)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
