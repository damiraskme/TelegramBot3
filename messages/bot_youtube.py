import logging
import os
from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from download_tiktok import *
from download_youtube import *
from messages.addition import basic_func
from messages.addition.bot_states import start_state, youtube_states


bot = basic_func.bot
dp = basic_func.dp

youtube_links = {}

async def download_youtubemp4_link(message: types.Message, state: FSMContext):
    await youtube_states.youtube_download.set()
    await message.reply("Send the link of the video", reply_markup=types.ReplyKeyboardRemove())

async def download_youtube_answer(message: types.Message, state: FSMContext):
    youtube_links[message.from_user.id] = message.text
    keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    # mp3_button = types.KeyboardButton(text="\U0001F3B5" + "MP3")
    mp3_button = types.InlineKeyboardButton(text="\U0001F3B5" + "MP3", callback_data="mp3_button")
    # mp4_button = types.KeyboardButton(text="\U0001F4F9" + "MP4")
    mp4_button = types.InlineKeyboardButton(text="\U0001F4F9" + "MP4", callback_data="mp4_button")
    # keyboard.add(mp3_button, mp4_button)
    keyboard = types.InlineKeyboardMarkup().add(mp3_button, mp4_button)
    await youtube_states.youtube_choice.set()
    await message.reply("Choose between MP3 or MP4", reply_markup=keyboard)

async def download_youtubemp4(message: types.Message, state: FSMContext):
    try:
        downloadYoutube(youtube_links[message.from_user.id], message.from_user.id)
    except:
        logging.error(f"Error {dp.current_state}")
        logging.error(f"Can't find {youtube_links[message.from_user.id]} link")
        logging.error(f"Wrong link")
    youtube_title = getTitle(youtube_links[message.from_user.id])
    try:
        with open(f"videos/youtube_for_{message.from_user.id}.mp4", "rb") as youtube_video:
        # Send the MP4 file to the user
            youtube_links.clear()
            await start_state.function_choice.set()
            await bot.send_video(message.from_user.id, youtube_video, caption=f"{youtube_title}")
            await bot.send_message("Want to do something else or cancel with /cancel")
    except FileNotFoundError:
        logging.error(f"Error {dp.current_state}")
        logging.error(f"Can't find {youtube_links[message.from_user.id]} file")

        # Check if file exists and if True: delete the file
    try:
        os.remove(f"videos/youtube_for_{message.from_user.id}.mp4")
        logging.info("File deleted")
    except FileNotFoundError:
        logging.error(f"Error {dp.current_state}")
        logging.error(f"Can't find {youtube_links[message.from_user.id]} file")

async def download_youtubemp3(message: types.Message, state: FSMContext):
    try:
        downloadYoutubemp3(youtube_links[message.from_user.id], message.from_user.id)
    except:
        logging.error(f"Error {dp.current_state}")
        logging.error(f"Can't find {youtube_links[message.from_user.id]} link")
        logging.error(f"Wrong link")
    youtube_title = getTitle(youtube_links[message.from_user.id])
    try:
        with open(f"videos/youtube_for_{message.from_user.id}.mp3", "rb") as youtube_video:
            # Send the MP3 file to the user
            youtube_links.clear()
            await start_state.function_choice.set()
            await bot.send_audio(message.from_user.id, youtube_video, caption=f"{youtube_title}")
            await bot.send_message("Want to do something else or cancel with /cancel")
    except FileNotFoundError:
        logging.error(f"Error {dp.current_state}")
        logging.error(f"Can't find {youtube_links[message.from_user.id]} file")

        # Check if file exists and if True: delete the file
    try:
        os.remove(f"videos/youtube_for_{message.from_user.id}.mp3")
        logging.info("File deleted")
    except FileNotFoundError:
        logging.error(f"Error {dp.current_state}")
        logging.error(f"Can't find {youtube_links[message.from_user.id]} file")

def setup(dp: Dispatcher):
    dp.register_message_handler(download_youtubemp4_link, state=start_state.function_choice, commands=["youtube"])
    dp.register_message_handler(download_youtube_answer, state=youtube_states.youtube_download)
    dp.register_callback_query_handler(download_youtubemp4, text="mp4_button", state=youtube_states.youtube_choice)
    dp.register_callback_query_handler(download_youtubemp3, text="mp3_button", state=youtube_states.youtube_choice)

    # dp.register_message_handler(download_youtubemp4, Command(ignore_case=True, commands=["mp4"]), state=youtube_states.youtube_choice)
    # dp.register_message_handler(download_youtube, Command(ignore_case=True, commands=["mp3"]), state=youtube_states.youtube_choice)
