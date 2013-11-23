__author__ = 'allen.zhang'

#coding=utf8
from django.db import models


class User(models.Model):
    email = models.EmailField(db_index=True)
    password = models.CharField(max_length=255)


class Token(models.Model):
    user = models.ForeignKey(User,related_name="tokens")
    token_string = models.CharField(max_length=128,db_index=True)

class Restaurant(models.Model):
    name = models.CharField(max_length=255,db_index=True)
    number = models.IntegerField()

class Category(models.Model):
    name=models.CharField(max_length=255,db_index=True)

class Food(models.Model):
    name = models.CharField(max_length=255,db_index=True)
    category = models.ForeignKey(Category,related_name="category")
    restaurant = models.ForeignKey(Restaurant,related_name="restaurant")
    price = models.IntegerField()
    number = models.IntegerField()


class Bill(models.Model):
    time = models.DateTimeField(auto_now_add=True,db_index=True)
    user = models.ForeignKey(User,related_name="bills")
    food = models.ManyToManyField(Food,related_name="food")


class History(models.Model):
    user = models.ForeignKey(User,related_name="history")
    name = models.CharField(max_length=255)
    cost = models.IntegerField()
    time = models.DateTimeField(auto_now_add=True)