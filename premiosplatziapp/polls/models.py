from ast import mod
from datetime import datetime
from secrets import choice
from tkinter import CASCADE
from django.db import models
from django.utils import timezone

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    #every time when we find a class who finnisg with "field" It's a datatype that we can use for a attribute 
    pub_date = models.DateTimeField("date published")
    
    def __str__(self) :
        return self.question_text
    
    def was_published_recently(self):
        return self.pub_date >= timezone.now() -  datetime.timedelta(days=1) 

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
        
    def __str__(self):
        return self.choice_text
    
    
        
        
    
   