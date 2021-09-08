from django.urls import path

from .views import (AboutView, ArticleCreateView, ArticleDeleteView,
                    ArticleDetailView, ArticleListView, ArticleUpdateView)

app_name = 'articles'
urlpatterns = [
    path('', ArticleListView.as_view(), name='list'),
    path('articles/<int:pk>', ArticleDetailView.as_view(), name='detail'),
    path('articles/create', ArticleCreateView.as_view(
        extra_context={'title': 'New Article'}), name='create'),
    path('articles/<int:pk>/delete', ArticleDeleteView.as_view(), name='delete'),
    path('articles/<int:pk>/update', ArticleUpdateView.as_view(), name='update'),
    path(
        'about/', AboutView.as_view(extra_context={'title': 'About'}), name='about'),
]
