import contextlib
from models.Database import Users as Users_


def Users():
    return list(Users_.select())


def User(chat_id):
    with contextlib.suppress(Exception):
        Users_.create(chat_id=chat_id)

