from rest_framework import status
from rest_framework.test import APIClient
from unittest.mock import patch
from .models import Question
import pytest

@pytest.mark.django_db
@patch('requests.get')  # Mock the requests.get function
def test_post_question(mock_get):
    # Mock the response from the API
    mock_response = [{'id': 1, 'question': 'Mocked question', 'answer': 'Mocked answer', 'created_at': '2023-10-11T12:00:00Z'}]
    mock_get.return_value.json.return_value = mock_response

    # Make a POST request to the question API
    client = APIClient()
    response = client.post('/api/', {'questions_num': 1}, format='json')

    # Check if the response is successful
    assert response.status_code == status.HTTP_200_OK

    # Check if the question is created in the database
    assert Question.objects.count() == 1

    # Check if the response matches the serialized question
    expected_data = {
        'question_id': 1,
        'text': 'Mocked question',
        'answer': 'Mocked answer',
        'created': '2023-10-11T12:00:00Z'
    }
    assert response.data == expected_data

@pytest.mark.django_db
@patch('requests.get')  # Mock the requests.get function
def test_post_question_existing_question(mock_get):
    # Mock the response from the API
    mock_response = [{'id': 1, 'question': 'Mocked question', 'answer': 'Mocked answer', 'created_at': '2023-10-11T12:00:00Z'}]
    mock_get.return_value.json.return_value = mock_response

    # Create an existing question in the database
    Question.objects.create(
        question_id=1,
        text='Existing question',
        answer='Existing answer',
        created='2023-10-10T12:00:00Z'
    )

    # Make a POST request to the question API
    client = APIClient()
    response = client.post('/api/', {'questions_num': 1}, format='json')

    # Check if the response is successful
    assert response.status_code == status.HTTP_200_OK

    # Check if a new question is created (not the existing one)
    assert Question.objects.count() == 2

    # Check if the response matches the serialized question
    expected_data = {
        'question_id': 1,
        'text': 'Mocked question',
        'answer': 'Mocked answer',
        'created': '2023-10-11T12:00:00Z'
    }
    assert response.data == expected_data
