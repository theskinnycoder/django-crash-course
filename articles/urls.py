from django.urls import path

from .views import (about, article_create, article_delete, article_detail,
                    article_update, article_list)

app_name = 'articles'
urlpatterns = [
    path('', article_list, name='list'),
    path('articles/<int:pk>', article_detail, name='detail'),
    path('articles/create', article_create, name='create'),
    path('articles/<int:pk>/delete', article_delete, name='delete'),
    path('articles/<int:pk>/update', article_update, name='update'),
    path('about/', about, name='about'),
]
