from apscheduler.schedulers.asyncio import AsyncIOScheduler
from instances import dp, bot
from aiogram.utils import executor
from handlers import client, admin



def handlers():
    client.register_handlers_client(dp)
    admin.register_handlers_admin(dp)

def main():
    scheduler = AsyncIOScheduler()
    scheduler.add_job(client.example, "interval", seconds=60)
    scheduler.start()

    handlers()
    executor.start_polling(dp, skip_updates=True)

if __name__ == "__main__":
    main()