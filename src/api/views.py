import os

import requests
from .models import Question
from .serializers import QuestionSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import AllowAny


API_SOURCE = os.environ.get('API_SOURCE')

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
        return Response(data)
        # for _ in data:
        #     return Response({
        #         'id': _['id'],
        #         'text': _['question'],
        #         'answer': _['answer'],
        #         'created': _['created_at'],
        #     }, status=status.HTTP_201_CREATED)



