from django import forms

class RecipientForm(forms.Form):
    name = forms.CharField(max_length=50)
    email = forms.EmailField()
    contact = forms.CharField(max_length=10)
    institution = forms.CharField(max_length=100)