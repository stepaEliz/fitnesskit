from django.urls import path
from .views import LessonView


urlpatterns = [
    path('lessons/', LessonView.as_view()),
]
