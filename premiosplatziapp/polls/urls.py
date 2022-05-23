from django.urls import path
#we import the "path" funtion  

from . import views
# the "." means we are going to import something from this path archive (polls)

urlpatterns = [
    path("", views.index, name="index")
]
