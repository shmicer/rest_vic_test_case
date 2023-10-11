from django.db import models


class Question(models.Model):
    question_id = models.IntegerField(unique=True)
    text = models.TextField()
    answer = models.TextField()
    created = models.DateTimeField()