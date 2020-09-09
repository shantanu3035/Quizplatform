"""

from django.contrib import admin
from django.urls import path, include
from .views import homepage, QuestionListView

urlpatterns = [
    #path('', homepage, name="quiz-home"),
    path('',homepage, name='quizapp-home'),
    path('<int:class_number>', QuestionListView.as_view(), name="qbank"),
]

"""