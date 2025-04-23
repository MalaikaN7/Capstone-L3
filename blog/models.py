from django.db import models


class Post(models.Model):
    """
    Represents a blog post.

    :ivar title: The title of the blog post.
    :vartype title: str
    :ivar body: The main content/body of the blog post.
    :vartype body: str
    :ivar signature: A short signature or author line for the post.
    :vartype signature: str
    :ivar date: The date and time the post was created.
    :vartype date: datetime
    """
    title = models.CharField(max_length=200)
    body = models.TextField()
    signature = models.CharField(max_length=140, default="~ By Malaika Nkosi")
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """
        Returns the string representation of the post.

        :return: The title of the blog post.
        :rtype: str
        """
        return self.title
