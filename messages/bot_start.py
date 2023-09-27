import logging
import time
import os
import json

from aiogram import types, Router, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

from addition import basic_func
from addition.bot_states import start_state
from addition.days_func import getData


bot = basic_func.bot
dp = basic_func.dp
router_start = Router()

user_database_dictionary = {"user":{
    "name": None,
    "id": None,
    "username": None,
    "time": None,
}}
user_database_list = []


# Start command
@router_start.message(Command("start"))
async def send_start(message: types.Message, state: FSMContext):
    
    admin_id = basic_func.get_admin()
    if (message.from_user.id == admin_id):
        user_database_dictionary.update(
            {"user":{
            "name": message.from_user.full_name,
            "id": message.from_user.id,
            "username": message.from_user.username,
            "time": time.asctime(),
            "admin": {
                "start": getData()[0],
                "end": getData()[1],
                "max": getData()[2],
                "current": getData()[3],
                "streak": getData()[4]
            }}}
        )
    else: 
        user_database_dictionary.update({"user":{
        "name": message.from_user.full_name,
        "id": message.from_user.id,
        "username": message.from_user.username,
        "time": time.asctime(),}})
    user_database_list.append(user_database_dictionary)
    try:
        with open(f"addition/json/database.json", "w+", encoding="utf-8") as json_database:
            if os.path.isfile("addition/json/database.json"):
                if (os.stat("addition/json/database.json").st_size == 0):
                    json.dump(user_database_list, json_database, ensure_ascii=False,sort_keys=False, indent=4, separators=(",", ": "))
                else:
                    json_read = json.load(json_database)
                    if user_database_dictionary["user"] in json_read:
                        logging.info("User already in database")
                    else:
                        json_read = json.load(json_database)
                        user_database_list.append(user_database_dictionary)
                        json.dump(user_database_list, json_database, ensure_ascii=False,sort_keys=False, indent=4, separators=(",", ": "))
        await state.set_state(start_state.function_choice)
        await message.reply(f"Hi {message.from_user.username}")
        await message.answer("\nChoose from:\nDownload tiktok video /tiktok\nDownload youtube video /youtube\nWrite notes /note\nOr cancel with /cancel")
    except FileNotFoundError:
        logging.error(f"Error {state.get_state()}")
        logging.error(f"Cant find json file")

# Cancel command
@router_start.message(Command("cancel"))
async def send_cancel(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    logging.info(f"Cancelling state {current_state}")
    await state.clear()
    await message.reply("Cancelled", reply_markup=types.ReplyKeyboardRemove())

# Useless help command
@router_start.message(Command("help"))
async def send_help(message: types.Message, state: FSMContext):
    await message.reply(f"No help {message.from_user.username}")

