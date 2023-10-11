from rest_framework import serializers

from src.api.models import Question


class QuestionSerializer(serializers.ModelSerializer):

    model = Question
    fields = ['question_id', 'text', 'answer', 'created']

