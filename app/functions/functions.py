from language import ru, uz
from models.Chats import Answers, Applications, User
from models.Database import Application


async def set_lang(user_id, lang=None) -> str:
    user = User(user_id)
    user.lang = lang
    user.save()
    return uz.uz['start'] if user.lang == 'uz' else ru.ru['start']



async def set_answer(user_id, answer=None) -> str:
    user = User(user_id)
    app = Application.select().where(user_id == user.get_id()).order_by(Application.id.desc()).get()
    app.answered = True
    app.save()
    Answers(app.get_id(), answer.text)
    return   uz.uz['user_msg_sent'].format(str(answer.text)) if user.lang == 'uz' else ru.ru['user_msg_sent'].format(str(answer.text)), uz.uz['sended_to_user_notf'] if user.lang == 'uz' else ru.ru['sended_to_user_notf']


async def set_application(data:dict, user)-> bool:
    try:
        region = data.get("region")
        msg = data.get("msg")
        #save to databse
        Applications(user.get_id(), msg=msg, region=region)
        return True
    except Exception:
        return False

