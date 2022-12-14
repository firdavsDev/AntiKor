from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from config import regions
from language import ru, uz


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
    return ReplyKeyboardMarkup(buttons, resize_keyboard=True, one_time_keyboard=True, selective=True)

def structure_types(lang):
    bio_quality = uz.uz['bio_quality'] if lang == 'uz' else ru.ru['bio_quality']
    university = uz.uz['university'] if lang == 'uz' else ru.ru['university']
    agro = uz.uz['agro'] if lang == 'uz' else ru.ru['agro']
    chigirtka = uz.uz['chigirtka'] if lang == 'uz' else ru.ru['chigirtka']
    
    return  ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text=bio_quality),
        ], 
        [
            KeyboardButton(text=university),

        ], 
        [
            KeyboardButton(text=agro),
        ], 
        [
            KeyboardButton(text=chigirtka),
        ],
    ],
    resize_keyboard=True,  one_time_keyboard=True, selective=True
)


