# news/views.py
from django.http import HttpResponse
from .models import Article
from .scraper import *

def scrape(request, keyword):
    articles = scrape_articles(keyword)
    for article in articles:
        Article.objects.create(title=article['title'], link=article['link'], published=article['published'])
    return HttpResponse(f"Scraping successful! Scraped {len(articles)} articles.")

def rss(request, keyword):
    articles = get_google_rss(keyword)
    for article in articles:
        Article.objects.create(title=article['title'], link=article['link'])

    return HttpResponse(f"Scraping successful! Scraped {len(articles)} articles.")