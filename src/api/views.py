import os

import requests
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


API_SOURCE = os.environ.get('API_SOURCE')

class QuestionAPIView(APIView):
    def post(self, request, *args, **kwargs):
        questions_num = request.data.get('questions_num', 1)
        response = requests.get(f'{API_SOURCE}{questions_num}')
        data = response.json()[0]
        return Response(data, status=status.HTTP_201_CREATED)



