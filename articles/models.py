from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    thumb = models.ImageField(default='default.jpg', blank=True)
    # add in thumbnail, 
    # add author later


    # WHENEVER YOU CHANCE A MODEL
    # python manage.py makemigrations 
    # python manage.py migrate

    # Defines how an article will look in admin and shell
    def __str__(self):
        return self.title 

    
    # return a short version of the article body
    def snippet(self):
        snippet = self.body[:50]
        if len(self.body) > 50:
            snippet += " ..."
        return snippet