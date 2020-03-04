from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils import timezone


class Posts(models.Model):
    title = models.CharField(max_length=20)
    subject = models.TextField()
    date_post = models.DateTimeField(default=timezone.now())
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'pk': self.pk})