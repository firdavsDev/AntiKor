from models.Chats import User, Applications, Answers
from language import uz, ru
from models.Database import Application
async def set_lang(user_id, lang=None) -> str:
    user = User(user_id)
    user.lang = lang
    user.save()
    return uz.uz['start'] if user.lang == 'uz' else ru.ru['start']


async def set_region(user_id, region=None) -> str:
    user = User(user_id)
    app = Applications(user.get_id())
    app.region = region
    app.save()
    return uz.uz['message'] if user.lang == 'uz' else ru.ru['message'], app


async def set_msg(user_id, msg=None) -> str:
    user = User(user_id)
    #update application msg
    app = Application.select().where(user_id == user.get_id()).order_by(Application.id.desc()).get()
    app.msg = msg
    app.save()
    return uz.uz['mes_sent'] if user.lang == 'uz' else ru.ru['mes_sent']

async def set_answer(user_id, answer=None) -> str:
    user = User(user_id)
    app = Application.select().where(user_id == user.get_id()).order_by(Application.id.desc()).get()
    app.answered = True
    app.save()
    Answers(app.get_id(), answer.text)
    return   uz.uz['user_msg_sent'].format(str(answer.text)) if user.lang == 'uz' else ru.ru['user_msg_sent'].format(str(answer.text)), uz.uz['sended_to_user_notf'] if user.lang == 'uz' else ru.ru['sended_to_user_notf']

