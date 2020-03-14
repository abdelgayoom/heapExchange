from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Questions(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    body = models.TextField()
    date_asked = models.DateTimeField(auto_now_add=True, editable=False)

    def __str__(self):
        return f'{self.title}'


class Answers(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='asked_user')
    questions = models.ForeignKey(Questions, on_delete=models.CASCADE, related_name='questions')
    body = models.TextField()
    date_answered = models.DateTimeField(default=timezone.now, editable=False)

    def __str__(self):
        return f'{self.body}'


