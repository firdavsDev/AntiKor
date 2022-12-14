import asyncio
import contextlib
import logging
from aiogram.utils import exceptions

from models import Chats

logging.basicConfig(level=logging.INFO)
log = logging.getLogger('broadcast')


def get_chats():
    """
    Return users list
    """
    yield from Chats.Users()


async def send_message(user_id: int, msg) -> bool:

    try:
        await msg.copy_to(chat_id=user_id, reply_markup=msg.reply_markup)
    except exceptions.BotBlocked:
        pass
    except exceptions.ChatNotFound:
        pass
    except exceptions.RetryAfter as e:
        await asyncio.sleep(e.timeout)
        await msg.copy_to(chat_id=user_id, reply_markup=msg.reply_markup)
    except exceptions.UserDeactivated:
        pass
    except exceptions.MigrateToChat as e:
        with contextlib.suppress(Exception):
            await msg.copy_to(chat_id=e.migrate_to_chat_id, reply_markup=msg.reply_markup)
    except exceptions.TelegramAPIError:
        pass
    else:
        return True
    return False

#send all user msg
async def broadcaster(msg) -> str:
    """
    Simple broadcaster
    :return: Count of messages
    """
    sends = 0
    error_sends = 0
    try:
        for user_id in get_chats():
            if await send_message(user_id=user_id, msg=msg):
                sends += 1
            else:
                error_sends += 1
            await asyncio.sleep(.05)  # 20 messages per second (Limit: 30 messages per second)
    finally:
        log.info(f"{sends} messages successful sent.\n{error_sends} messages notsuccessful sent.")

    return f"Юборилди: {sends}\nЮборилмади: {error_sends}"
