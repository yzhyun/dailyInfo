# news/models.py
from django.db import models


class Article(models.Model):
    user_id = models.CharField(max_length=255)
    keyword = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    link = models.URLField()
    content = models.TextField(default='', null=True)
    published = models.DateTimeField(auto_now_add=True)  # 날짜와 시간 저장

    def __str__(self):
        return f"{self.title} ({self.published})"
