from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .forms import ArticleForm
from .models import Article


def article_list(request):
    articles = Article.objects.all().order_by('-created_at')
    return render(request, 'articles/article_list.html', {'articles': articles})


def article_detail(request, pk):
    article = Article.objects.get(pk=pk)
    context = {'article': article, 'title': article.title}
    return render(request, 'articles/article_detail.html', context)


@login_required
def article_create(request):
    form = ArticleForm()
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.save()
            return redirect('articles:detail', pk=article.id)
    context = {'form': form, 'title': 'New Article'}
    return render(request, 'articles/article_form.html', context)


@login_required
def article_update(request, pk):
    article = Article.objects.get(pk=pk)
    if article.author != request.user:
        return redirect('articles:detail', pk=pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('articles:detail', pk=article.id)
    else:
        form = ArticleForm(instance=article)
    context = {
        'form': form,
        'article': article,
        'title': f'Update {article.title}'
    }
    return render(request, 'articles/article_form.html', context)


@login_required
def article_delete(request, pk):
    article = Article.objects.get(pk=pk)
    if article.author != request.user:
        return redirect('articles:detail', pk=pk)
    if request.method == 'POST':
        article.delete()
        return redirect('articles:list')
    context = {
        'article': article,
        'title': f'Delete {article.title}'
    }
    return render(request, 'articles/article_confirm_delete.html', context)


def about(request):
    return render(request, 'articles/about.html', {'title': 'About'})
