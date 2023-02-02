from apscheduler.schedulers.asyncio import AsyncIOScheduler
from instances import dp
from aiogram.utils import executor
from handlers import client, admin



def handlers():
    admin.register_handlers_admin(dp)
    client.register_handlers_client(dp)

def main():
    scheduler = AsyncIOScheduler()
    scheduler.add_job(client.schedule, "interval", seconds=15)
    scheduler.start()

    handlers()
    executor.start_polling(dp, skip_updates=True)

if __name__ == "__main__":
    main()