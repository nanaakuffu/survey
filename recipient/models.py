from django.db import models


# Create your models here.
class Recipient(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    contact_number = models.CharField(max_length=15)
    institution = models.CharField(max_length=100)
    survey_link = models.CharField(max_length=200, null=True)

    class Meta:
        db_table = 'recipients'

    def __str__(self):
        return self.name
