import logging
import time
import os
import json

from aiogram import types, Router, F
from aiogram.filters import Command
from aiogram.types import FSInputFile
from aiogram.fsm.context import FSMContext

from addition import basic_func
from addition.bot_states import download_states

bot = basic_func.bot
dp = basic_func.dp
router_download = Router()

@router_download.message(Command("down"))
async def downloadStart(message: types.Message, state: FSMContext):
    await message.answer("Send your video or audio file")
    await state.set_state(download_states.download_audio)

@router_download.message(download_states.download_audio, F.video_note)
async def downloadNote(message: types.Message, state: FSMContext):
    id = message.from_user.id
    file = await bot.get_file(message.video_note.file_id)
    file_path = file.file_path
    try:
        await bot.download_file(file_path, f"addition/videos/media_note_{id}.mp4")
    except:
        logging.error("Error")
        logging.error(f"video_note_{id}.mp4")
    video = FSInputFile(path=f"addition/videos/media_note_{id}.mp4")
    await bot.send_video(video=video, caption="Your video note", chat_id=id)
    deleteFile(id, "mp4")

@router_download.message(download_states.download_audio, F.voice)
async def downloadNote(message: types.Message, state: FSMContext):
    id = message.from_user.id
    file = await bot.get_file(message.voice.file_id)
    file_path = file.file_path
    logging.info(msg=f"{file_path}")
    try:
        await bot.download_file(file_path, f"addition/videos/media_note_{id}.mp3")
    except:
        logging.error("Error")
        logging.error(f"video_note_{id}.mp4")
    audio = FSInputFile(path=f"addition/videos/media_note_{id}.mp3")
    await bot.send_audio(audio=audio, caption="Your audio file", chat_id=id)
    deleteFile(id, "mp3")

def deleteFile(id: int, ext: str):
    try:
        if (os.path.isfile(f"addition/videos/media_note_{id}.{ext}")):
            os.remove(f"addition/videos/media_note_{id}.{ext}")
            logging.info("File deleted")
    except FileNotFoundError:
        logging.info("Error")
