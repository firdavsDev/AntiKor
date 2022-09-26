from peewee import (BigIntegerField, CharField, ForeignKeyField, Model,
                    SqliteDatabase, TextField, BooleanField)

db = SqliteDatabase('application_bot.db')


class Users(Model):    
    chat_id = BigIntegerField(primary_key=True, unique=True)
    lang = CharField(null = True)
    class Meta:
        database = db


class Application(Model):
    user_id = ForeignKeyField(Users, backref='applications')
    msg = TextField(null= True)
    region = CharField(null = True)
    answered = BooleanField(default=False)

    class Meta:
        database = db

class Answer(Model):
    application_id = ForeignKeyField(Application, backref='answers')
    msg = TextField(null=True)

    class Meta:
        database = db

db.connect()
db.create_tables([Users, Application, Answer])
