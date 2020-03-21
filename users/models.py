from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=100, blank=True, null=True)
    image = models.ImageField(upload_to='profile_images', default='default.jpg', blank=True, null=True)

    def __str__(self):
        return f'{self.user.username} profile'

    # change image size when uploaded by the user
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (76, 92)
            img.thumbnail(output_size)
            img.save(self.image.path)
