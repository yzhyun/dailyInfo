# news/scraper.py
import requests
from bs4 import BeautifulSoup

def scrape_articles(keyword):
    url = f"https://news.google.com/search?q={keyword}&hl=ko&gl=KR&ceid=KR%3Ako"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    articles = []
    for article in soup.find_all('article'):
        title = article.find('h3').get_text() if article.find('h3') else 'No title'
        link = article.find('a', href=True)['href']
        full_link = f'https://news.google.com{link}'
        articles.append({'title': title, 'link': full_link})

    return articles
