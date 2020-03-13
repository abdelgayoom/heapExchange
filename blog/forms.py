from django import forms
from .models import Comments


class CommentsCreationForm(forms.ModelForm):

    class Meta:
        model = Comments
        fields = ['comment']


class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    email = forms.EmailField()


