from django import forms
from question.models import Question

# Create your models here.
class Answer(forms.Form):
    question = forms.IntegerField()
    answer = forms.Textarea()
    choice = forms.Select()
    needs_recommendation = forms.BooleanField()