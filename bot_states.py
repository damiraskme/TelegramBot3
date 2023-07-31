from aiogram.dispatcher.filters.state import State, StatesGroup

class function_form(StatesGroup):
    function_choice = State()
    tiktok = State()
    youtube = State()
    note = State()

class note_states(StatesGroup):
    note_add_1 = State()
    note_add_2 = State()

class youtube_states(StatesGroup):
    youtube_download = State()
    youtube_choice = State()
    youtube_mp4 = State()
