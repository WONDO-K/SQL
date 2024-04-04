from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Article
from .forms import ArticleForm,CommentForm


# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)


def detail(request, pk):
    article = Article.objects.get(pk=pk)
    # 특정 게시글에 작성된 모든 댓글 조회 (Article -> Comment, 역참조)
    comments = article.comment_set.all()
    # DB의 모든 댓글을 조회(특정 게시글에 작성된 모든 댓글 조회가 아님)
    # comment.objects.all()
    comment_form = CommentForm()
    context = {
        'article': article,
        'comments' : comments,
        'comment_form' : comment_form,
    }
    return render(request, 'articles/detail.html', context)


@login_required
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm()
    context = {
        'form': form,
    }
    return render(request, 'articles/create.html', context)


@login_required
def delete(request, pk):
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect('articles:index')


@login_required
def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm(instance=article)
    context = {
        'form': form,
        'article': article,
    }
    return render(request, 'articles/update.html', context)

def comments_create(request,pk):
    # 게시글 조회 (어떤 게시글에 작성되어야 하는지 알아야 함)
    article = Article.objects.get(pk=pk)
    comment_from = CommentForm(request.POST)
    if comment_from.is_valid():
        comment = comment_from.save(commit=False)
        comment.article = article
        comment.save()
        return redirect('article:detail',article.pk)
    context = {
        'article' : article,
        'comment_form' : comment_from,
    }
    return render(request, 'articles/detail.html',context)

def comments_delete(request,article_pk,comment_pk):
    comment = comment.objects.get(pk=comment_pk)
    comment.delete()
    return redirect('articles:deatil',article_pk)