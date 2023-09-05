import logging
import os
import calendar
from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from download_tiktok import *
from download_youtube import *
from messages.addition import basic_func
from messages.addition.bot_states import start_state


bot = basic_func.bot
dp = basic_func.dp


async def CalendarStart(message: types.Message):
    with open("json/calendar.json", "r") as file:
        read = file.read()
        
    await message.answer(f"/check/add")