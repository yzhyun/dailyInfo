# news/views.py
from django.http import HttpResponse
from .models import Article
from .scraper import scrape_articles

def scrape(request, keyword):
    articles = scrape_articles(keyword)
    for article in articles:
        Article.objects.create(title=article['title'], link=article['link'])
    return HttpResponse(f"Scraping successful! Scraped {len(articles)} articles.")