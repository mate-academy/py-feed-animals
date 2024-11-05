from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


profile_btn = KeyboardButton(text="Profile")

mainMenu = ReplyKeyboardMarkup(keyboard=[[profile_btn]], resize_keyboard=True)
