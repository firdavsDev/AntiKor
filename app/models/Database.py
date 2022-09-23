from peewee import (BigIntegerField, CharField, ForeignKeyField, Model,
                    SqliteDatabase, TextField)

db = SqliteDatabase('application_bot.db')


class Users(Model):
    LANGUAGE_CHOICES = (
        ("uz", "O'zbekcha"), 
        ("ru", "Русский")
    )
    
    chat_id = BigIntegerField(primary_key=True)
    lang = CharField(choices = LANGUAGE_CHOICES, null = True)
    
    class Meta:
        database = db


class Application(Model):
    user_id = ForeignKeyField(Users, backref='applications')
    msg = TextField()
    class Meta:
        database = db

class Answer(Model):
    application_id = ForeignKeyField(Application, backref='answers')
    msg = TextField()

    class Meta:
        database = db


db.connect()
db.create_tables([Users, Application, Answer])
