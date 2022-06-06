import datetime

from django.test import TestCase
from django.utils import timezone

from .models import Question
#Models
#Viewa

class QuestionModelTests(TestCase):
    
    def test_was_published_recently_with_future_questions(self):
        """was_published_recently returns False for questions which pub_date is in the future"""
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(question_text="¿Quien es el mejor CD de platzi?",pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)
        
    def test_was_published_recently_with_present_questions(self):
        """was_published_recently returns True for questions which pub_date is in the present or less than 1 day ago"""
        time2 = timezone.now()
        present_question = Question(question_text="¿Quien es el mejor profe de platzi?",pub_date=time2)
        self.assertIs(present_question.was_published_recently(), True)
        
    def test_was_published_recently_with_past_questions(self):
        """was_published_recently returns False for questions which pub_date is in the past with more than 1 day ago"""
        time3 = timezone.now() - datetime.timedelta(days=30)
        past_question = Question(question_text="¿Quien es el profe más gracioso de platzi?",pub_date=time3)
        self.assertIs(past_question.was_published_recently(), False)