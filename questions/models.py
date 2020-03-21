from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse


class Questions(models.Model):
    TAG_CHOICE = (
        ('Programming', 'Programming'),
        ('Web development', 'Web development'),
        ('Hacking', 'Hacking'),
        ('Electrical Engineering', 'Electrical Engineering'),
        ('Electronic Engineering', 'Electronic Engineering'),
        ('Android Development', 'Android Development'),
        ('Machine Learning', 'Machine Learning'),
        ('Bug bounty', 'Bug bounty'),
        ('others', 'others')
    )
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, choices=TAG_CHOICE)
    body = models.TextField()
    date_asked = models.DateTimeField(auto_now_add=True, editable=False)

    def __str__(self):
        return f'{self.title}'

    def get_absolute_url(self):
        return reverse('questions:detail', kwargs={'pk': self.pk})


class Answers(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_user')
    questions = models.ForeignKey(Questions, on_delete=models.CASCADE, related_name='answers')
    body = models.TextField()
    date_answered = models.DateTimeField(default=timezone.now, editable=False)

    def __str__(self):
        return f'{self.body}'

    def get_absolute_url(self):
        return reverse('questions:detail', kwargs={'pk': self.questions.pk})