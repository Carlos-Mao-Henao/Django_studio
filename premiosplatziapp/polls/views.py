from django.shortcuts import render
# Create a Http reponse
from django.http import HttpResponse

from .models import Question

def index(request):
    latest_question_list = Question.objects.all()
    return render(request, "polls/index.html", {
        "latest_question_list": latest_question_list
    })
#We create de Http response in this funtion


def detail(request, question_id):
    return HttpResponse(f"Estás viendo la pregunta número {question_id}")


def results(request, question_id):
    return HttpResponse(f"Estás viendo los resultados de la pregunta número {question_id}")

def vote(request, question_id):
    return HttpResponse(f"Estás votando a la pregunta número {question_id}")

