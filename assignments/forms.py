from django import forms
from . models import Assignment

class SubmissionForm(forms.Form):
    file = forms.FileField(required=False)
    assignment = forms.ModelChoiceField(queryset=Assignment.objects.all(), widget=forms.Select, required=True)