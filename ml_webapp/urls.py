from django.contrib import admin
from django.urls import path, re_path, include
from . import views

urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^articles/', include('articles.urls')),
    re_path(r'^about/$', views.about),
    re_path(r'^$', views.homepage),
]
