# news/models.py
from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=255)
    link = models.URLField()
    content = models.TextField(default='')
    published = models.TextField(default='')

    def __str__(self):
        return f"{self.title} ({self.published})"
