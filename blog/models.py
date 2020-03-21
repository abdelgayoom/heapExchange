from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils import timezone
from ckeditor_uploader.fields import RichTextUploadingField
from ckeditor.fields import RichTextField


class Posts(models.Model):
    title = models.CharField(max_length=20)
    subject = RichTextUploadingField()
    date_post = models.DateTimeField(default=timezone.now, editable=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'pk': self.pk})


class Comments(models.Model):
    posts = models.ForeignKey(Posts, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = RichTextField(config_name='special')
    date_comment = models.DateTimeField(auto_now_add=True, editable=False)

    def __str__(self):
        return self.comment

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'pk': self.posts.pk})
