import contextlib
from models.Database import Users as Users_,\
Application as Application_,  Answer as Answers_ 



def Users():
    return list(Users_.select())


def Statistica():
    return Users_.select().count(), Application_.select().count(), Answers_.select().count(), Application_.select().where(Application_.answered==False).count()

def User(chat_id):
    with contextlib.suppress(Exception):
        user, _ = Users_.get_or_create(chat_id=chat_id)
        return user


def Applications(user_id):
    with contextlib.suppress(Exception):
        return Application_.create(user_id=user_id)

def Answers(app_id, msg=None):
    with contextlib.suppress(Exception):
        return Answers_.create(application_id=app_id, msg=msg)
