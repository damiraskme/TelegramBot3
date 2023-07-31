import logging
import os
from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from download_tiktok import *
from download_youtube import *
from bot_states import function_form
import basic_func


bot = basic_func.bot
dp = basic_func.dp

async def download_tiktok_answer(message:types.Message, state: FSMContext):
    await function_form.function_choice.set()
    await message.reply("Tiktok links not working right now")


async def download_tiktok(message:types.Message, state: FSMContext):
    downloadVideo(message.text)
    with open(f"tiktok_videos/video_{random_number_tiktok1}_{random_number_tiktok2}.mp4", "rb", encoding="utf-8") as tiktok_video:
        # Send the MP4 file to the user
        await function_form.function_choice.set()
        await bot.send_video(message.from_user.id, tiktok_video, caption="Your tiktok video file")
        await message.answer("Want to do something else or cancel with /cancel")
        # Check if file exists and if True: delete the file
    if (os.path.isfile(f"tiktok_videos/video_{random_number_tiktok1}_{random_number_tiktok2}.mp4")):
        os.remove(f"tiktok_videos/video_{random_number_tiktok1}_{random_number_tiktok2}.mp4")
        logging.info("File deleted")
    else:
        logging.info("Error")

def setup(dp: Dispatcher):
    dp.register_message_handler(download_tiktok_answer, state=function_form.function_choice, commands=["tiktok"])
    dp.register_message_handler(download_tiktok, state=function_form.tiktok)
