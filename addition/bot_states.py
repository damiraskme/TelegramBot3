from aiogram.fsm.state import State, StatesGroup

class start_state(StatesGroup):
    function_choice = State()
    tiktok = State()
    youtube = State()
    note = State()
    audio_message = State()

class note_states(StatesGroup):
    note_add_1 = State()
    note_add_2 = State()

class youtube_states(StatesGroup):
    youtube_download = State()
    youtube_choice = State()
    youtube_mp4 = State()

class download_states(StatesGroup):
    download_audio = State()

class calendar_states(StatesGroup):
    calendar_get = State()
    calendar_change = State()
