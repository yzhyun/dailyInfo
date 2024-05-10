# news/scraper.py
import feedparser
import requests
from datetime import datetime
from bs4 import BeautifulSoup


def clean_article_body(body_text):
    # BeautifulSoup 객체를 생성하여 HTML을 파싱합니다.
    print(body_text)
    soup = BeautifulSoup(body_text, 'html.parser')

    # for element in soup.select('div.advertisement, script'):
    #     element.decompose()  # 광고와 스크립트 태그를 찾아 제거합니다.
    #for element in soup.select('div.advertisement, script, iframe, style, noscript'):
    #    element.decompose()
    #article_body = soup.find('div', class_='article-content')  # or soup.find('article')

    # 각 부모 태그의 <br> 태그 개수를 저장할 딕셔너리 생성
    br_counts = {}

    # 모든 <br> 태그를 찾아 각 부모 태그의 개수를 세기
    br_tags = soup.find_all('br')
    for br_tag in br_tags:
        parent_tag = br_tag.parent
        if parent_tag in br_counts:
            br_counts[parent_tag] += 1
        else:
            br_counts[parent_tag] = 1
    try:
        # 가장 많은 <br> 태그를 포함한 부모 태그 찾기
        most_used_parent = max(br_counts, key=br_counts.get)
        most_used_parent_class = most_used_parent.get('class')

        # 해당 태그의 텍스트 가져오기
        most_used_parent_text = most_used_parent.get_text(strip=True)

    except ValueError:
        most_used_parent_text = ""

    return most_used_parent_text


def scrape_articles(keyword):
    url = f"https://news.google.com/rss/search?q={keyword}&hl=ko&gl=KR&ceid=KR:ko"  #구글
    feed = feedparser.parse(url)
    articles = []
    cnt = 0

    for entry in feed.entries:

        title = entry.title
        link = entry.link
        published_date = datetime.strptime(entry.published, '%a, %d %b %Y %H:%M:%S %Z')
        #published = entry.published
        response = requests.get(link, allow_redirects=True)
        # 리디렉션된 URL 확인
        redirected_url = response.url

        # URL에서 웹페이지의 HTML을 가져옵니다.
        response = requests.get(redirected_url)
        content = clean_article_body(response.text)

        articles.append({'title': title, 'link': redirected_url, 'published': published_date, 'content': content
                        , 'keyword': keyword})
        #링크의 내용을 따라 본문을 가져와야 함.
        #html의 내용을 가져와서 저장하고 ai로 간추리는 방식을 선택하자
        #ai 토큰 수를 줄여야 하는데 가능할지 테스트 필요

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
