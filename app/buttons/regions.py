from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup
from config import regions


def region_buttons(lang):
    buttons = []
    two_buttons = []
    all_regions = regions['uz'] if lang == 'uz' else regions['ru']
    for name in all_regions:
        two_buttons.append(KeyboardButton(name))
        if len(two_buttons) == 2:
            buttons.append(two_buttons)
            two_buttons = []

    if len(all_regions) % 2 != 0:
        buttons.append(two_buttons)
    return ReplyKeyboardMarkup(buttons, resize_keyboard=True, one_time_keyboard=True)

