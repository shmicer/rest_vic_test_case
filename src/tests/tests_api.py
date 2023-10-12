from unittest.mock import patch

import pytest
from rest_framework import status
from rest_framework.test import APIClient

from .models import Question


@pytest.mark.django_db
@patch('requests.get')
def test_post_question(mock_get):
    mock_response = [{'id': 1,
                      'question': 'Mocked question',
                      'answer': 'Mocked answer',
                      'created_at': '2023-10-11T12:00:00Z'
                      }
                     ]
    mock_get.return_value.json.return_value = mock_response

    client = APIClient()
    response = client.post('/api/', {'questions_num': 1}, format='json')

    assert response.status_code == status.HTTP_200_OK

    assert Question.objects.count() == 1

    expected_data = {
        'question_id': 1,
        'text': 'Mocked question',
        'answer': 'Mocked answer',
        'created': '2023-10-11T12:00:00Z'
    }
    assert response.data == expected_data


@pytest.mark.django_db
@patch('requests.get')
def test_post_question_existing_question(mock_get):
    mock_response = [{'id': 1,
                      'question': 'Mocked question',
                      'answer': 'Mocked answer',
                      'created_at': '2023-10-11T12:00:00Z'
                      }]
    mock_get.return_value.json.return_value = mock_response

    Question.objects.create(
        question_id=1,
        text='Existing question',
        answer='Existing answer',
        created='2023-10-10T12:00:00Z'
    )

    client = APIClient()
    response = client.post('/api/', {'questions_num': 1}, format='json')

    assert response.status_code == status.HTTP_200_OK

    assert Question.objects.count() == 2

    expected_data = {
        'question_id': 1,
        'text': 'Mocked question',
        'answer': 'Mocked answer',
        'created': '2023-10-11T12:00:00Z'
    }
    assert response.data == expected_data
