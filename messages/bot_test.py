import logging
import time
import os
import json

from aiogram import types, Router, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

from addition import keyboards as kb
from addition import basic_func
from addition.bot_states import start_state

router_test = Router()
bot = basic_func.bot
dp = basic_func.dp

@router_test.message(Command("test"))
async def testMsg(message: types.Message):
    await message.answer("test", reply_markup=kb.youtube_kb)


