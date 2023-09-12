from aiogram import Bot, Dispatcher, executor
from config import TELEGRAM_BOT_TOKEN

bot = Bot(TELEGRAM_BOT_TOKEN)
dp = Dispatcher(bot)

if __name__ == "__main__":
    from handlers.default import *
    from handlers.executor import *

    executor.start_polling(dp, skip_updates=True)
