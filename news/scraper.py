# news/scraper.py
import feedparser
import requests
from bs4 import BeautifulSoup


def scrape_articles(keyword):
    url = f"https://news.google.com/rss/search?q={keyword}&hl=ko&gl=KR&ceid=KR:ko"  #구글
    feed = feedparser.parse(url)
    articles = []
    cnt = 0
    for entry in feed.entries:
        title = entry.title
        link = entry.link
        published = entry.published
        articles.append({'title': title, 'link': link, 'published': published})
        #링크의 내용을 따라 본문을 가져와야 함.
        #html의 내용을 가져와서 저장하고 ai로 간추리는 방식을 선택하자

        cnt += 1
        if cnt == 10:
            break
    return articles

    #
    # count = 0
    # for article in soup.find_all('article'):
    #     title_element = article.find('h3', class_='ipQwMb ekueJc RD0gLb')
    #     title = title_element.get_text() if title_element else 'No title'
    #
    #     link_element = article.find('a', href=True)
    #     if link_element:
    #         link = link_element['href']
    #         full_link = f'https://news.google.com{link}'
    #         article_response = requests.get(full_link, headers=headers, allow_redirects=True)
    #         article_soup = BeautifulSoup(article_response.text, 'html.parser')
    #         content_element = article_soup.find('div', class_='article-body')  # Check correct class or tag
    #         content = content_element.get_text() if content_element else 'No content'
    #
    #         articles.append({'title': title, 'link': full_link, 'content': content})
    #         count += 1
    #         if count == 10:
    #             break
    # for article in articles:
    #     print(article['title'])
    #     print(article['link'])
    #     print(article['content'])

    return articles


def get_summery(keyword):
    url = f"https://news.google.com/rss/search?q={keyword}&hl=ko&gl=KR&ceid=KR:ko"
    feed = feedparser.parse(url)
    for entry in feed.entries:
        print(entry.title)
        print(entry.link)
        print(entry.published)
        print('-' * 10)
    articles = []
    return articles
