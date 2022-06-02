from django.urls import path
#we import the "path" funtion  

from . import views
# the "." means we are going to import something from this path archive (polls)

app_name = "polls"
urlpatterns = [
    #ex: /polls/
    path("", views.index, name="index"),
    #ex: /polls/5/
    path("<int:question_id>/detail/elmao", views.detail, name="detail"),
    #ex: /polls/5/results
    path("<int:question_id>/results/", views.results, name="results"),
    #ex: /polls/5/vote
    path("<int:question_id>/vote/", views.vote, name="vote"),
]
