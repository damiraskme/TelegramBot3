import logging
import os
from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from download_tiktok import *
from messages.addition import basic_func
from messages.addition.bot_states import start_state

bot = basic_func.bot
dp = basic_func.dp

async def download_tiktok_answer(message:types.Message, state: FSMContext):
    await start_state.tiktok.set()
    await message.reply("Send link of the tiktok")


async def download_tiktok(message:types.Message, state: FSMContext):
    downloadVideo(message.text, message.from_user.id)
    id = message.from_user.id
    if (os.path.isfile("messages/tiktok_videos/file_{id}.mp4")):
        print("yes")
    with open(f"messages/tiktok_videos/file_{id}.mp4", "rb") as tiktok_video:
        # Send the MP4 file to the user
        await start_state.function_choice.set()
        await bot.send_video(message.from_user.id, tiktok_video, caption="Your tiktok video file")
        await message.answer("Want to do something else or cancel with /cancel")
    # Check if file exists and if True: delete the file
    deleteTiktok(message.from_user.id)

def setup(dp: Dispatcher):
    dp.register_message_handler(download_tiktok_answer, state=start_state.function_choice, commands=["tiktok"])
    dp.register_message_handler(download_tiktok, state=start_state.tiktok)
