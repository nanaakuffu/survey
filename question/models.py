from django.db import models

# Create your models here.


class Question(models.Model):
    question_text = models.TextField()
    recommendation = models.TextField()

    class Meta:
        db_table = 'questions'

    def __str__(self):
        return self.question_text
