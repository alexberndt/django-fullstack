from django.shortcuts import render
from .models import Article
from django.http import HttpResponse


def article_list(request):

    articles = Article.objects.all().order_by('date') # use name of field in Article
    data = {'articles': articles}

    return render(request, 'articles/article_list.html', data)


def article_detail(request, slug):
    
    article = Article.objects.get(slug=slug)
    data = {'article': article}
    
    return render(request, 'articles/article_detail.html', data)
    
    # return HttpResponse(slug)