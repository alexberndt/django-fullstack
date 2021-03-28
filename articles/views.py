from django.shortcuts import render, redirect
from .models import Article
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from . import forms


def article_list(request):

    articles = Article.objects.all().order_by('date') # use name of field in Article
    data = {'articles': articles}

    return render(request, 'articles/article_list.html', data)


def article_detail(request, slug):
    
    article = Article.objects.get(slug=slug)
    data = {'article': article}
    
    return render(request, 'articles/article_detail.html', data)


@login_required(login_url="/accounts/login/")
def article_create(request):

    if request.method == "POST":
        form = forms.CreateArticleForm(request.POST, request.FILES)

        if form.is_valid():
            
            # first give instance of saved form, without actually saving yet 
            instance = form.save(commit=False)
            
            # attach current logged in author 
            instance.author = request.user 
            instance.save()

            return redirect('articles:list')

    else:
        form = forms.CreateArticleForm()
    
    data = {"form": form}
    
    return render(request, 'articles/article_create.html', data)