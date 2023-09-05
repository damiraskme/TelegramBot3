import logging
import os
from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from download_tiktok import *
from download_youtube import *
from messages.addition import basic_func
from messages.addition.bot_states import start_state, download_states


bot = basic_func.bot
dp = basic_func.dp


async def downloadVoiceMessage(message: types.Message, state: FSMContext):
    await download_states.download_audio.set()
    await message.answer("Send the audio file")

async def downloadVoiceSend(message: types.Message, state: FSMContext):
    voiceMessage = bot.download_file(message.audio)
    await bot.send_audio(voiceMessage, message.from_user.id)

def setup(dp: Dispatcher):
    dp.register_message_handler(downloadVoiceMessage, state=start_state.audio_message, commands=["audio"])
    dp.register_message_handler(downloadVoiceSend, state="*", content_types= types.Audio)
