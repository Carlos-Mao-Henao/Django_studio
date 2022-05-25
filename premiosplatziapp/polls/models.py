from ast import mod
from secrets import choice
from tkinter import CASCADE
from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    #every time when we find a class who finnisg with "field" It's a datatype that we can use for a attribute 
    pub_date = models.DateTimeField("date published")

class Choices(models.Model):
        question = models.ForeignKey(Question, on_delete=CASCADE)
        choice_text = models.CharField(max_length=200)
        votes = models.IntegerField(default=0)