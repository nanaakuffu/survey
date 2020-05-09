from django import forms

class QuestionForm(forms.Form):
    question_text = forms.Textarea()
    recommendation = forms.Textarea()