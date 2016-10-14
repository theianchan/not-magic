# from peewee import *

# DATABASE = SqliteDatabase('notmagic.db')

# class DataModel(Model):
#   name = CharField(unique=True)
#   description = TextField(default='')

#   class Meta:
#     database = DATABASE

# def initialize():
#   DATABASE.connect()
#   DATABASE.create_tables([DataModel], safe=True)
#   DATABASE.close()
