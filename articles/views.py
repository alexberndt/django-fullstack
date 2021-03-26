from django.shortcuts import render
from .models import Article


def article_list(request):

    articles = Article.objects.all().order_by('date') # use name of field in Article
    data = {'articles': articles}

    return render(request, 'articles/article_list.html', data)