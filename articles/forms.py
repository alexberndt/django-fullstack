from django import forms 
from . import models 


class CreateArticleForm(forms.ModelForm):
    
    # define meta data 
    class Meta:
        model = models.Article
        fields = ['title', 'body', 'slug', 'thumb']
