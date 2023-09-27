import os
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage

def get_apikey():
    env_path = os.path.join("TOKEN.env")
    load_dotenv(env_path)
    API_TOKEN = os.getenv("API_TOKEN")
    return str(API_TOKEN)

def get_admin():
    env_path = os.path.join("TOKEN.env")
    load_dotenv(env_path)
    ADMIN_TOKEN = os.getenv("ADMIN_TOKEN")
    return int(ADMIN_TOKEN)


bot = Bot(get_apikey(), parse_mode=ParseMode.HTML)
dp = Dispatcher(storage=MemoryStorage())


