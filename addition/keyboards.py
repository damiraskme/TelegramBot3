from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton

youtube_kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="\U0001F3B5" + "MP3", callback_data="mp3_button")],
        [InlineKeyboardButton(text="\U0001F4F9" + "MP4", callback_data="mp4_button")]
    ])