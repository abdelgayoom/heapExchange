from django import forms
from .models import Answers


class AnswersCreationForm(forms.ModelForm):

    class Meta:
        model = Answers
        fields = ['body']