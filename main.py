import logging
from aiogram import Bot, Dispatcher, executor, types
import aiogram.utils.markdown as md
import time
from aiogram.types import InputFile
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from download_tiktok import *
from download_youtube import *
import os
import json
import asyncio
import sys

API_TOKEN = '5839152810:AAGz-Tq96UL0b-pIpuIxQCkCNkVIlRRvIy0'
logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot, storage = MemoryStorage())

en_dict = ['a', 'b', 'c', 'd', 'e', 'f', 
'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 
'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
ru_dict = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 
'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 
'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']

user_names_dictionary = {}
youtube_dictionary = {}
class function_form(StatesGroup):
    function_choice = State()
    tiktok = State()
    youtube_1 = State()
    youtube_2 = State()
    reminder = State()

@dp.message_handler(state='*', commands=['start'])
async def send_start(message: types.Message, state: FSMContext):
    logging.info(f'{message.from_user.mention}')
    user_names_dictionary.update({f'{message.from_user.mention}': {message.from_user.id}})
    with open(f'databese.txt', 'a') as dictionary_string:
        dictionary_string.write(str(user_names_dictionary))
        dictionary_string.write('\n')
    logging.info(f'{message.from_user.full_name} {message.from_user.id} {time.asctime}')
    await state.finish()
    await function_form.function_choice.set()
    await message.reply(f"Hi {message.from_user.mention}")
    await message.answer('\nChoose from:\nDownload tiktok video /tiktok\nDownload youtube video /youtube\nThird option or cancel with /cancel')
    
@dp.message_handler(state='*', commands=['cancel'])
async def cancel_form(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    logging.info('Cancelling state %r', current_state)
    await state.finish()
    await message.reply('Cancelled', reply_markup=types.ReplyKeyboardRemove())

@dp.message_handler(state='*', commands=['help'])
async def send_help(message: types.Message, state: FSMContext):
    await message.reply(f'No help {message.from_user.mention}')

@dp.message_handler(state=function_form.function_choice, commands=['tiktok'])
async def download_tiktok_answer(message:types.Message, state: FSMContext):
    await function_form.tiktok.set()
    await message.answer('Send tiktok link')
@dp.message_handler(state=function_form.tiktok)
async def download_tiktok(message:types.Message, state: FSMContext):
    downloadVideo(message.text)
    with open(f'tiktok_videos/video_{random_number_tiktok1}_{random_number_tiktok2}.mp4', 'rb') as tiktok_video:
        # Send the MP4 file to the user
        await function_form.function_choice.set()
        await bot.send_video(message.from_user.id, tiktok_video, caption='Your tiktok video file')
        await message.answer('Want to do something else or cancel with /cancel')
        # Check if file exists and if True: delete the file
    if (os.path.isfile(f'tiktok_videos/video_{random_number_tiktok1}_{random_number_tiktok2}.mp4')):
        os.remove(f'tiktok_videos/video_{random_number_tiktok1}_{random_number_tiktok2}.mp4')
        print('File deleted')
    else:
        print('Error')

@dp.message_handler(state=function_form.function_choice, commands=['youtube'])
async def download_youtube_answer(message: types.Message, state: FSMContext):
    await function_form.youtube_1.set()
    await message.answer('Send youtube link')
@dp.message_handler(state=function_form.youtube_1)
async def download_youtube_answer_2(message: types.Message, state: FSMContext):
    #async with state.proxy() as data:
    #    data['link'] = message.text
    youtube_link = message.text
    youtube_dictionary['link'] = str(youtube_link)
    await function_form.youtube_2.set()
    await message.answer('Send resolution of video in form of: \n"144, 240, 360, 480, 720 and 1080"')
@dp.message_handler(state=function_form.youtube_2)
async def download_youtube(message: types.Message, state: FSMContext):
    youtube_dictionary['res'] = str(message.text)
    await state.update_data(youtube_res=str(message.text))
    downloadYoutube(youtube_dictionary['link'], youtube_dictionary['res'])
    with open(f'videos/youtube_{random_youtube_1}_{random_youtube_2}.mp4', 'rb') as youtube_video:
        # Send the MP4 file to the user
        await function_form.function_choice.set()
        await bot.send_video(message.from_user.id, youtube_video, caption='Your youtube video file')
        await message.answer('Want to do something else or cancel with /cancel')
        # Check if file exists and if True: delete the file
    if (os.path.isfile(f'videos/youtube_{random_youtube_1}_{random_youtube_2}.mp4')):
        os.remove(f'videos/youtube_{random_youtube_1}_{random_youtube_2}.mp4')
        print('File deleted')
    else:
        print('Error')

#@dp.message_handler(state=function_form.function_choice, commands=['reminder'])


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)