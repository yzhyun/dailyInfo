# news/urls.py
from django.urls import path
from .views import scrape

urlpatterns = [
    path('scrape/<str:keyword>/', scrape, name='scrape'),

]
