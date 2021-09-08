from django.urls import reverse_lazy
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView

from .models import Article


class ArticleListView(ListView):
    model = Article
    context_object_name = 'articles'
    ordering = ['-created_at']


class ArticleDetailView(DetailView):
    model = Article

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.object.title
        return context


class ArticleCreateView(CreateView):
    model = Article
    fields = ['title', 'excerpt', 'content']

    def get_success_url(self):
        return reverse_lazy('articles:detail', kwargs={'pk': self.object.id})


class ArticleUpdateView(UpdateView):
    model = Article
    fields = ['title', 'excerpt', 'content']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f'Update {self.object.title}'
        return context

    def get_success_url(self):
        return reverse_lazy('articles:detail', kwargs={'pk': self.object.id})


class ArticleDeleteView(DeleteView):
    model = Article
    success_url = reverse_lazy('articles:list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f'Delete {self.object.title}'
        return context


class AboutView(TemplateView):
    template_name = 'articles/about.html'
