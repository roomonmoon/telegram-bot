from aiogram.utils import executor
from instances import dp
from handlers import client, admin
from pyqiwip2p import QiwiP2P



def handlers():
    client.register_handlers_client(dp)
    admin.register_handlers_admin(dp)

def main():
    handlers()
    executor.start_polling(dp, skip_updates=True)

if __name__ == "__main__":
    main()