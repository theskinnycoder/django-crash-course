from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Article(models.Model):
    title = models.CharField(
        max_length=100, blank=False, null=False)
    excerpt = models.CharField(max_length=200, blank=False, null=False)
    content = models.TextField(blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='articles', default=None)

    def __str__(self):
        return self.title
