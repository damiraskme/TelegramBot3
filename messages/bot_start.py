import logging
import time
import os
import json
from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
import basic_func
from bot_states import function_form


bot = basic_func.bot
dp = basic_func.dp

user_database_dictionary = {"user":{
    "name": None,
    "id": None,
    "mention": None,
    "time": None,
}}
user_database_list = []


# Start command
async def send_start(message: types.Message, state: FSMContext):
    user_database_dictionary.update({"user":{
        "id": message.from_user.id,
        "name": message.from_user.full_name,
        "mention": message.from_user.mention,
        "time": time.asctime(),}})
    user_database_list.append(user_database_dictionary)
    with open(f"database.json", "w+", encoding="utf-8") as json_database:
        if os.path.isfile("database.json"):
            if (os.stat("database.json").st_size == 0):
                json.dump(user_database_list, json_database, ensure_ascii=False,sort_keys=True, indent=4, separators=(",", ": "))
            else:
                json_read = json.load(json_database)
                if user_database_dictionary["user"] in json_read:
                    logging.info("User already in database")
                else:
                    json_read = json.load(json_database)
                    user_database_list.append(user_database_dictionary)
                    json.dump(user_database_list, json_database, ensure_ascii=False,sort_keys=True, indent=4, separators=(",", ": "))
    await state.finish()
    await function_form.function_choice.set()
    await message.reply(f"Hi {message.from_user.mention}")
    await message.answer("\nChoose from:\nDownload tiktok video /tiktok\nDownload youtube video /youtube\nWrite notes /note\nOr cancel with /cancel")

# Cancel command
async def send_cancel(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    logging.info("Cancelling state %r", current_state)
    await state.finish()
    await message.reply("Cancelled", reply_markup=types.ReplyKeyboardRemove())

# Useless help command
async def send_help(message: types.Message, state: FSMContext):
    await message.reply(f"No help {message.from_user.mention}")

def setup(dp: Dispatcher):
    dp.register_message_handler(send_start, state="*", commands=["start"])
    dp.register_message_handler(send_cancel, state="*", commands=["cancel"])
    dp.register_message_handler(send_help, state="*", commands=["help"])



