from django.db import models
from question.models import Question

# Create your models here.


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.TextField()
    choice = models.CharField(max_length=5)
    needs_recommendation = models.IntegerField()

    class Meta:
        db_table = 'answers'
        order_with_respect_to = 'question'

    def __str__(self):
        return self.answer
