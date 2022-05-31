from multiprocessing.spawn import import_main_path
from django.contrib import admin
from .models import Question
from .models import Choice
admin.site.register(Question)
admin.site.register(Choice)
