import os
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

def get_apikey():
    env_path = os.path.join("TOKEN.env")
    load_dotenv(env_path)
    API_TOKEN = os.getenv("API_TOKEN")
    return str(API_TOKEN)

bot = Bot(token=get_apikey())
dp = Dispatcher(bot, storage = MemoryStorage())

