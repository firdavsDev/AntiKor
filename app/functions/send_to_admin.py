from email import message
import logging

from aiogram.types import Message
from config import OWNER_ID


logging.basicConfig(level=logging.INFO)
log = logging.getLogger('Sended to Admin!')

#send msg to admin
async def send_to_admin(msg: Message, data:dict, user) -> bool:
    """
    Simple broadcaster
    :return: Count of messages
    """
    try:
        region = data.get("region")
        structure = data.get("structure")
        
        text = "Янги хабар мавжуд! 👇\n"
        text += "Қуйидаи маълумотлар қабул қилинди:\n\n"

        if region:
            text += f"Вилоят - {region}\n"
        else:
            text += f"Тузилма - {structure}\n"

        await msg.bot.send_message(chat_id=OWNER_ID, text=text)
        await msg.forward(chat_id=OWNER_ID)
    finally:
        log.info(f"{msg} messages successful sent")
    return True

