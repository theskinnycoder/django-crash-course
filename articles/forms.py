from django.forms import models

from .models import Article


class ArticleForm(models.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'excerpt', 'content']
