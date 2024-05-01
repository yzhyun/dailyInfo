# news/urls.py
from django.urls import path
from .views import scrape, rss

urlpatterns = [
    path('scrape/<str:keyword>/', scrape, name='scrape'),
    path('rss/<str:keyword>/'   , rss, name='rss'),


]
