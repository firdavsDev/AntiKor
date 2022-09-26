import logging

from aiogram.types import Message
from config import OWNER_ID

logging.basicConfig(level=logging.INFO)
log = logging.getLogger('Sended to Admin!')

#send msg to admin
async def send_to_admin(msg: Message) -> bool:
    """
    Simple broadcaster
    :return: Count of messages
    """
    try:
        await msg.bot.send_message(chat_id=OWNER_ID, text="Yangi xabar mavjud! 👇")
        await msg.forward(chat_id=OWNER_ID, protect_content=True)
    finally:
        log.info(f"{msg} messages successful sent")
    return True

