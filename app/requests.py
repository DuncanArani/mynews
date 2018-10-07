# from main import main
import urllib.request
import json
import app
from .models import Sources, Articles

# Getting the url key
api_key = None

# Getting base url
news_a_base_url = None
news_s_base_url = None
news_h_base_url = None


def configure_request(app):
    global api_key, news_a_base_url, news_s_base_url, news_h_base_url
    news_s_base_url = app.config['NEWS_SOURCE_BASE_URL']
    news_a_base_url = app.config['NEWS_ARTICLE_BASE_URL']
    news_h_base_url = app.config['NEWS_TOPHEADLINES_BASE_URL']
    api_key = app.config['NEWS_KEY']



def get_sources(category):
    '''
    using base_url to get data from the sources
    '''
    get_sources_url = news_s_base_url.format(category, api_key)
    with urllib.request.urlopen(get_sources_url) as url:
        sources_data = url.read()
        sources_response = json.loads(sources_data)
        sources_results = None

        if sources_response['sources']:
            sources_result_list = sources_response['sources']
            sources_results = process_results(sources_result_list)

    return sources_results


def process_results(sources_list):
    '''
    getting instance of the list of sources
    '''
    sources_result = []
    for source in sources_list:
        id = source.get('id')
        name = source.get('name')
        descript = source.get('description')
        url = source.get('url')
        cat = source.get('category')
        # date = news.get('date')

        sources_object = Sources(id, name, descript, url, cat)
        sources_result.append(sources_object)
    return sources_result


'''
Using the base url everything we can get article of specific sources articles
'''


def get_articles(id):
    '''
    getting a article_base url to get artciles with id from the source
    '''

    get_articles_url = news_a_base_url.format(id, api_key)
    print(get_articles_url)
    with urllib.request.urlopen(get_articles_url) as url:
        articles_data = url.read()
        articles_response = json.loads(articles_data)

        articles_results = None

        if articles_response['articles']:
            articles_result_list = articles_response['articles']
            articles_results = process_articles(articles_result_list)
    return articles_results


def process_articles(articles_list):
    '''
    getting instance of the list of articles
    '''
    articles_result = []

    print(articles_result)
    for article in articles_list:
        id = article.get('id')
        name = article.get('name')
        author = article.get('author')
        title = article.get('title')
        description = article.get('description')
        url = article.get('url')
        image = article.get('urlToImage')
        date = article.get('publishedAt')

        if image:

            articles_object = Articles(
                id, name, author, title, description, url, image, date)
            articles_result.append(articles_object)

    return articles_result
