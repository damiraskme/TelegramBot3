import logging

from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from basic_func import get_apikey
from messages import bot_start, bot_tiktok, bot_note, bot_youtube



API_TOKEN = get_apikey()
logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot, storage = MemoryStorage())


# Start/cancel/help handlers
setup_start = bot_start.setup(dp)

# Tiktok handlers
setup_tiktok = bot_tiktok.setup(dp)

# Youtube handlers
setup_youtube = bot_youtube.setup(dp)

# Note handlers
setup_note = bot_note.setup(dp)


@dp.message_handler(state="*", commands=["info"])
async def info_send(message: types.Message):
    await message.reply("Bot made by me!")

if __name__ == '__main__':
    setup_start
    setup_tiktok
    setup_youtube
    setup_note
    executor.start_polling(dp, skip_updates=True)