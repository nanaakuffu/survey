from django.db import models

# Create your models here.
class Question(models.Model):
    question_text = models.TextField()
    recommendation = models.TextField()

    def __str__(self):
        return self.question_text