from aiogram.utils import executor
from instances import dp
from handlers import client, admin, other
import applogger

logger = applogger.get_logger(__name__)

async def on_startup(_):
    logger.info('Bot was started successful.')
    try:
        handlers()
        logger.info(f"All handlers was started successful.")
    except Exception as ex:
        logger.critical(ex)


def handlers():
    admin.register_handlers_admin(dp)
    client.register_handlers_client(dp)

def main():
    try:
        logger.warning(executor.start_polling(dp, skip_updates=True, on_startup=on_startup))
    except Exception as ex:
        logger.critical(ex) 

if __name__ == "__main__":
    main()