import os

from drf_spectacular.utils import (OpenApiExample,
                                   extend_schema, extend_schema_view)
import requests
from rest_framework import status

from .models import Question
from .serializers import QuestionSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import AllowAny


API_SOURCE = os.environ.get('API_SOURCE')


@extend_schema(
    summary='Enter a number of questions for receive a unique quiz question',
    request=QuestionSerializer,
    examples=[
        OpenApiExample(
            'Number of question example',
            description='Test example for the entering number of questions',
            value={
                "questions_num": 3,
            },
            status_codes=[str(status.HTTP_200_OK)],
        ),
    ],
)
class QuestionAPIView(APIView):
    authentication_classes = [SessionAuthentication]
    permission_classes = [AllowAny]
    def post(self, request, *args, **kwargs):
        questions_num = request.data.get('questions_num', 1)
        while True:
            response = requests.get(f'{API_SOURCE}{questions_num}')
            data = response.json()
            for item in data:
                if not Question.objects.filter(question_id=item['id']).exists():
                    Question.objects.create(
                        question_id=item['id'],
                        text=item['question'],
                        answer=item['answer'],
                        created= item['created_at']
                    )
                    break
            last_question = Question.objects.last()
            serializer = QuestionSerializer(last_question)
            return Response(serializer.data, status=status.HTTP_200_OK)



