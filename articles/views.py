from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  TemplateView, UpdateView)

from .models import Article


class ArticleListView(ListView):
    model = Article
    context_object_name = 'articles'
    ordering = ['-created_at']


class ArticleDetailView(DetailView):
    model = Article
    context_object_name = 'article'


class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Article
    fields = ['title', 'excerpt', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class ArticleUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Article
    fields = ['title', 'excerpt', 'content']
    context_object_name = 'article'

    def test_func(self):
        article = self.get_object()
        return self.request.user == article.author


class ArticleDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Article
    success_url = reverse_lazy('articles:list')
    context_object_name = 'article'

    def test_func(self):
        article = self.get_object()
        return self.request.user == article.author


class AboutView(TemplateView):
    template_name = 'articles/about.html'
