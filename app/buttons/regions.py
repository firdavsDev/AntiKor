from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from language.uz import uz
from config import regions


def region_buttons(lang):
    buttons = []
    two_buttons = []
    for region in regions:
        name = region['uz'] if lang == uz else region['ru']
        two_buttons.append(InlineKeyboardButton(name))
        if len(two_buttons) == 2:
            buttons.append(two_buttons)
            two_buttons = []

    if regions.count() % 2 != 0:
        buttons.append(two_buttons)
    return InlineKeyboardMarkup(buttons)

