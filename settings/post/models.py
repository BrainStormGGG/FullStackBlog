from django.contrib.auth.models import User
from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=100)
    annotation = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    content = models.TextField()
    img = models.ImageField(upload_to='img')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-date']