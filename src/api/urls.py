from django.urls import path
from .views import QuestionAPIView

urlpatterns = [
    path('quiz/', QuestionAPIView.as_view(), name='question-api'),
]