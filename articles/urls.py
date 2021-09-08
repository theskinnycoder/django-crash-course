from django.urls import path

from .views import (about, article_create, article_delete, article_details,
                    article_update, articles_index)

app_name = 'articles'
urlpatterns = [
    path('', articles_index, name='index'),
    path('about/', about, name='about'),
    path('articles/<int:id>', article_details, name='details'),
    path('articles/create', article_create, name='create'),
    path('articles/<int:id>/delete', article_delete, name='delete'),
    path('articles/<int:id>/update', article_update, name='update'),
]
