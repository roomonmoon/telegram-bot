from aiogram.utils import executor
from instances import dp
from handlers import client, admin, other


async def on_startup(_):
    print('BOT ONLINE')


def handlers():
    admin.register_handlers_admin(dp)
    client.register_handlers_client(dp)

def main():
    handlers()
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)

if __name__ == "__main__":
    main()