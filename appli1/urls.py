
from django.contrib import admin
from django.urls import path

from .views import index, article


urlpatterns = [
    path('', index, name="appli1-index"),
    path('article-<int:numero_article>/', article, name="appli1-article"),
]
