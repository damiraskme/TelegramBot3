import logging

from aiogram import types, Router, F
from aiogram.fsm.context import FSMContext
from aiogram.filters import Command
from aiogram.types import FSInputFile

from addition.download_youtube import *
from addition import basic_func
from addition.bot_states import start_state, youtube_states
from addition import keyboards as kb


bot = basic_func.bot
dp = basic_func.dp
router_youtube = Router()

youtube_links = {}

@router_youtube.message(Command("youtube"), start_state.function_choice)
async def download_youtubemp4_link(message: types.Message, state: FSMContext):
    await state.set_state(youtube_states.youtube_download)
    await message.reply("Send the link of the video", reply_markup=types.ReplyKeyboardRemove())

@router_youtube.message(youtube_states.youtube_download)
async def download_youtube_answer(message: types.Message, state: FSMContext):
    youtube_links[message.from_user.id] = message.text
    await state.set_state(youtube_states.youtube_choice)
    await message.reply("Choose between MP3 or MP4", reply_markup=kb.youtube_kb)

@router_youtube.callback_query(youtube_states.youtube_choice, F.data == "mp4_button")
async def download_youtubemp4(message: types.Message, state: FSMContext):
    try:
        downloadYoutube(youtube_links[message.from_user.id], message.from_user.id)
    except:
        logging.error(f"Error {state.get_state()}")
        logging.error(f"Can't find {youtube_links[message.from_user.id]} link")
        logging.error(f"Wrong link")
    youtube_title = getTitle(youtube_links[message.from_user.id])
    youtube_video = FSInputFile(path=f"addition/videos/youtube_for_{message.from_user.id}.mp4")
    try:
        youtube_links.clear()
        await state.set_state(start_state.function_choice)
        await bot.send_video(chat_id=message.from_user.id, video=youtube_video, caption=f"{youtube_title}")
        await bot.send_message(text="Want to do something else or cancel with /cancel")

    except FileNotFoundError:
        logging.error(f"Error {state.get_state()}")
        logging.error(f"Can't find {youtube_links[message.from_user.id]} file")

        # Check if file exists and if True: delete the file
    deleteYoutube(message.from_user.id)

@router_youtube.callback_query(youtube_states.youtube_choice, F.data == "mp3_button")
async def download_youtubemp3(message: types.Message, state: FSMContext):
    try:
        downloadYoutubemp3(youtube_links[message.from_user.id], message.from_user.id)
    except:
        logging.error(f"Error {state.get_state()}")
        logging.error(f"Can't find {youtube_links[message.from_user.id]} link")
        logging.error(f"Wrong link")
    youtube_title = getTitle(youtube_links[message.from_user.id])
    youtube_video = FSInputFile(path=f"addition/videos/youtube_for_{message.from_user.id}.mp3")
    try:
            # Send the MP3 file to the user
            youtube_links.clear()
            await state.set_state(start_state.function_choice)
            await bot.send_audio(chat_id=message.from_user.id, audio=youtube_video, caption=f"{youtube_title}")
            await bot.send_message(text="Want to do something else or cancel with /cancel")

    except FileNotFoundError:
        logging.error(f"Error {state.get_state()}")
        logging.error(f"Can't find {youtube_links[message.from_user.id]} file")

        # Check if file exists and if True: delete the file
    deleteYoutube(message.from_user.id)
