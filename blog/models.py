from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    signature = models.CharField(max_length=140, default="~ By Malaika Nkosi")
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
