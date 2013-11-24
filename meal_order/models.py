__author__ = 'allen.zhang'

#coding=utf8
from mongoengine import Document
from mongoengine.fields import *
import datetime as dt

class User(Document):
    email = StringField(unique=True)
    password = StringField(max_length=255)


class Token(Document):
    user_id = StringField()
    token_string = StringField(max_length=255)

class Restaurant(Document):
    name = StringField(max_length=255)
    number = IntField()

class Category(Document):
    name = StringField()

class Food(Document):
    name = StringField(max_length=255)
    category_id = StringField()
    restaurant_id = StringField()
    price = IntField()
    number = IntField()


class Bill(Document):
    time = DateTimeField(default=dt.datetime.now)
    cost = IntField()
    user_id = StringField()
    food_id_list = ListField()


class History(Document):
    user_id = StringField()
    cost = IntField()
    time = DateTimeField(default=dt.datetime.now)