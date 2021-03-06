import datetime
from urllib import response

from django.test import TestCase
from django.utils import timezone
from django.urls import reverse

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
        
def create_question(question_text, days):
    """_
    Create a question with the given "question_text", and published the given numbre of days offset to now (negative
    for questions published in the past, positive for questions that have yet to be published)
    """
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(question_text=question_text, pub_date=time)

class QuestionIndexViewTest(TestCase):
    
    def test_no_questions(self):
        """If no question exit, an appropiate message is displayed"""
        response = self.client.get(reverse("polls:index"))
        self.assertEqual(response.status_code, 200) 
        self.assertContains(response, "No polls available.")
        self.assertQuerysetEqual(response.context["latest_question_list"], [])
    
    def test_future_question(self):
        """Questions with a pub_date in the future aren't displayed on the index page"""
        create_question("future question", days=30)
        response = self.client.get(reverse("polls:index"))
        self.assertContains(response, "No polls available.")
        self.assertQuerysetEqual(response.context["latest_question_list"], [])
    
    def test_past_question(self):
        """Questions with a pub_date in the past are displayed on the index page"""
        question = create_question("past question", days=-10)
        response = self.client.get(reverse("polls:index"))
        self.assertQuerysetEqual(response.context["latest_question_list"], [question])
        
    def test_future_question_and_past_question(self):
        """
        even if both past and future question exist, only past questions are displayed
        """
        past_question = create_question(question_text="past question", days=-30)
        future_question = create_question(question_text="future question", days=30)
        response = self.client.get(reverse("polls:index"))
        self.assertQuerysetEqual(response.context["latest_question_list"],[past_question])
        
    def test_two_past_questions(self):
        """
        The questions index page may display multiple questions.
        """
        past_question1 = create_question(question_text="past question 1", days=-30)
        past_question2 = create_question(question_text="past question 2", days=-40)
        response = self.client.get(reverse("polls:index"))
        self.assertQuerysetEqual(response.context["latest_question_list"],[past_question1, past_question2])
    
    def test_two_future_questions(self):
        """
        The questions indez page aren't may display multiple questions whit pub_date in the future.
        """
        future_question1 = create_question(question_text="future question 1", days=30)
        future_question2 = create_question(question_text="future question 2", days=40)
        response = self.client.get(reverse("polls:index"))
        self.assertQuerysetEqual(response.context["latest_question_list"],[])
        
#def test_no_publish_future_questions(self):
#    """If the pub_date It's a future day """
#    response = self.client.get(reverse("polls:index"))
#    time = timezone.now() + datetime.timedelta(days=30)
#    future_question = Question(question_text="¿Quien es el mejor CD de platzi?",pub_date=time)
#   self.assertNotIn(future_question, response.context["latest_question_list"])        
        
    
class QuestionDetailViewTest(TestCase):
    def test_future_question(self):
        """
        The detail view of a question with a pub_date in the future returns a 404 error not found
        """
        future_question = create_question(question_text="future question", days=30)
        url = reverse("polls:detail", args=(future_question.pk,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)
    
    def test_past_question(self):
        """
        The detail view of a question with a pub_date in the past displays the question's text
        """
        past_question = create_question(question_text="past question", days=-30)
        url = reverse("polls:detail", args=(past_question.pk,))
        response = self.client.get(url)
        self.assertContains(response, past_question.question_text)
