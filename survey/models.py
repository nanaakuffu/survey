from django.db import models
from recipient.models import Recipient
from question.models import Question
from answer.models import Answer
from django_mysql.models import JSONField


# Create your models here.
class Survey(models.Model):
    recipient = models.ForeignKey(Recipient, on_delete=models.CASCADE)
    survey_id = models.IntegerField()
    date_sent = models.DateField()
    hasresponded = models.IntegerField()
    date_responded = models.DateField()
    file_name = models.CharField(max_length=50)

    def __str__(self):
        return self.recipient


class Response(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
    recipient = models.ForeignKey(Recipient, on_delete=models.CASCADE)
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)
    choice = models.CharField(max_length=1, default=0)

    def __str__(self):
        return self.survey


class QuestionsAndAnswers(models.Model):
    question_text = models.CharField(max_length=200)
    answers = JSONField()

    class Meta:
        managed = False
        db_table = 'survey_vw'


class Analytics(models.Model):
    question_text = models.CharField(max_length=200)
    responses = JSONField()

    class Meta:
        managed = False
        db_table = 'analytics_vw'
