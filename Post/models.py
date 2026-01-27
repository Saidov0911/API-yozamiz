from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=50, blank=False)
    body = models.TextField(max_length=1000, blank=False)
    published = models.DateTimeField(blank=False)
