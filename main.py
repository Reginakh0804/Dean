
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from config import BOT_TOKEN
from handlers import register_handlers

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())

register_handlers(dp)

if __name__ == "__main__":
    from keep_alive import keep_alive
    keep_alive()
    executor.start_polling(dp, skip_updates=True)
