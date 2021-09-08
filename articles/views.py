from django.shortcuts import redirect, render
from django.urls import reverse

from .forms import ArticleForm
from .models import Article


def articles_index(request):
    articles = Article.objects.all()
    return render(request, 'articles/index.html', {'articles': articles})


def article_details(request, id):
    article = Article.objects.get(pk=id)
    context = {'article': article, 'title': article.title}
    return render(request, 'articles/details.html', context)


def article_create(request):
    form = ArticleForm()
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save()
            return redirect(reverse('articles:details', args=[article.id]))
    context = {'form': form, 'title': 'New Article'}
    return render(request, 'articles/form.html', context)


def article_update(request, id):
    article = Article.objects.get(pk=id)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect(reverse('articles:details', args=[article.id]))
    else:
        form = ArticleForm(instance=article)
    context = {
        'form': form,
        'article': article,
        'title': f'Update {article.title}'
    }
    return render(request, 'articles/form.html', context)


def article_delete(request, id):
    article = Article.objects.get(pk=id)
    if request.method == 'POST':
        article.delete()
        return redirect(reverse('articles:index'))
    context = {
        'article': article,
        'title': f'Delete {article.title}'
    }
    return render(request, 'articles/confirm_delete.html', context)


def about(request):
    return render(request, 'articles/about.html', {'title': 'About'})
