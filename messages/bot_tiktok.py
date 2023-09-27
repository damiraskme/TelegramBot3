import logging

from aiogram import types, Router, F
from aiogram.filters import Command
from aiogram.types import FSInputFile
from aiogram.fsm.context import FSMContext

from addition import basic_func
from addition.download_tiktok import *
from addition.bot_states import start_state

bot = basic_func.bot
dp = basic_func.dp
router_tiktok = Router()

@router_tiktok.message(Command("tiktok"), start_state.function_choice)
async def download_tiktok_answer(message:types.Message, state: FSMContext):
    await state.set_state(start_state.tiktok)
    await message.reply("Send link of the tiktok")

@router_tiktok.message(start_state.tiktok)
async def download_tiktok(message:types.Message, state: FSMContext):
    try:
        downloadVideo(message.text, message.from_user.id)
        tiktok_video = FSInputFile(path=f"addition/videos/file_{message.from_user.id}.mp4")
            # Send the MP4 file to the user
        await state.set_state(start_state.function_choice)
        await bot.send_video(chat_id=message.from_user.id, video=tiktok_video, caption="Your tiktok video file")
        await message.answer(text="Want to do something else or cancel with /cancel")
        # Check if file exists and if True: delete the file
        deleteTiktok(message.from_user.id)
    except:
        logging.error(f"Error {state.get_state()}")
        logging.error(f"Can't find file_{message.from_user.id}.mp4 link")
        logging.error(f"Wrong link")

