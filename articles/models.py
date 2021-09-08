from django.db import models


class Article(models.Model):
    title = models.CharField(
        max_length=100, blank=False, null=False)
    excerpt = models.CharField(max_length=200, blank=False, null=False)
    content = models.TextField(blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
