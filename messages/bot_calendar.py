import logging

from aiogram import types, Router, F
from aiogram.fsm.context import FSMContext
from aiogram.filters import Command

from addition.bot_states import start_state, calendar_states
from addition import basic_func
from addition.bot_states import start_state
from addition.days_func import *


bot = basic_func.bot
dp = basic_func.dp
router_calendar = Router()

pattern_add = r"^(current|streak)\s+(add)$"
pattern_set = r"^(current|streak)\s+(set)\s+(\d+)$"
pattern_date = r"^(date)\s+(set)$"
    
@router_calendar.message(Command("calendar"), start_state.function_choice)
async def CalendarStart(message: types.Message, state: FSMContext):
    admin_id = basic_func.get_admin()
    if (message.from_user.id == admin_id):
        values = getJson()
        start = values["start"]
        end = values["end"]
        current = values["current"]
        streak = values["streak"]
        await message.reply(text=f"Hello {message.from_user.full_name}")
        await message.answer(f"{start}" + "\n" + f"{end}" + "\n" + f"{current}" + "\n" + f"{streak}")
        await state.set_state(calendar_states.calendar_get)
    else:
        await message.answer(text=f"no")

@router_calendar.message(calendar_states.calendar_get, F.text.regexp(pattern=pattern_add))
async def CalendarAdd(message: types.Message, state: FSMContext):
    first_word = message.text.split()[0]
    print(message.text, first_word)
    addJson(first_word)
    values = getJson()
    start = values["start"]
    end = values["end"]
    current = values["current"]
    streak = values["streak"]
    await message.answer(f"{start}" + "\n" + f"{end}" + "\n" + f"{current}" + "\n" + f"{streak}")


@router_calendar.message(calendar_states.calendar_get, F.text.regexp(pattern=pattern_set))
async def CalendarSet(message: types.Message, state: FSMContext):
    first_word = message.text.split()[0]
    second_word = message.text.split()[1]
    amount = int(message.text.split()[2])
    print(message.text, first_word, second_word, amount)
    setJson(first_word, amount)
    values = getJson()
    start = values["start"]
    end = values["end"]
    current = values["current"]
    streak = values["streak"]
    await message.answer(f"{start}" + "\n" + f"{end}" + "\n" + f"{current}" + "\n" + f"{streak}")

@router_calendar.message(calendar_states.calendar_get, F.text.regexp(pattern=pattern_date))
async def CalendarDate(message: types.Message, state: FSMContext):
    setDates()
    values = getJson()
    start = values["start"]
    end = values["end"]
    current = values["current"]
    streak = values["streak"]
    await message.answer(f"{start}" + "\n" + f"{end}" + "\n" + f"{current}" + "\n" + f"{streak}")

