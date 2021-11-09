from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView

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


class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Article
    fields = ['title', 'excerpt', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('articles:detail', kwargs={'pk': self.object.id})


class ArticleUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Article
    fields = ['title', 'excerpt', 'content']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f'Update {self.object.title}'
        return context

    def test_func(self):
        article = self.get_object()
        return self.request.user == article.author

    def get_success_url(self):
        return reverse_lazy('articles:detail', kwargs={'pk': self.object.id})


class ArticleDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Article
    success_url = reverse_lazy('articles:list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f'Delete {self.object.title}'
        return context

    def test_func(self):
        article = self.get_object()
        return self.request.user == article.author


class AboutView(TemplateView):
    template_name = 'articles/about.html'
