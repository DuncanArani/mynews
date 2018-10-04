import urllib.request
import json
from .models import Source
# news = news


# Getting api key
api_key = None
# Getting the news base url
base_url = None
news_url = None
catg_url = None


def configure_request(app):
    global api_key, base_url, news_url, catg_url, articles_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['SOURCES_API_BASE_URL']
    news_url = app.config['NEWS_API_BASE_URL']
    catg_url = app.config['CATG_API_BASE_URL']
    articles_url = app.config['ARTICLES_API_BASE_URL']


def get_sources(source_name):
    get_source_url = base_url.format(source_name, api_key)
    with urllib.request.urlopen(get_source_url) as url:
        get_source_data = url.read()
        get_source_response = json.loads(get_source_data)

        get_source_results = None

        if get_source_response['sources']:
            get_source_list = get_source_response['sources']
            get_source_results = process_sources(get_source_list)

    return get_source_results


def process_sources(sources):
    '''
    Function  that processes the news result and transform them to a list of Objects
    Args:
        news_list: A list of dictionaries that contain news details
    Returns :
        news_results: A list of news objects
    '''
    sources_results = []
    for source in sources:
        id = source.get('id')
        title = source.get('title')
        description = source.get('descriptrion')
        link = source.get('url')
        type = source.get('category')
        place = source.get('country')

        sources_object = Source(id, title, description, link, type, place)
        sources_results.append(sources_object)

    return sources_results


def get_articles(id):
    '''
    Function that processes the articles and returns a list of articles objects
    '''
    get_articles_url = articles_url.format(id, api_key)

    with urllib.request.urlopen(get_articles_url) as url:
        articles_results = json.loads(url.read())

        articles_object = None
        if articles_results['articles']:
            articles_object = process_articles(
                articles_results['articles'])

    return articles_object


def process_articles(articles_list):
    '''
    '''
    articles_object = []
    for article_item in articles_list:
        id = article_item.get('id')
        author = article_item.get('author')
        title = article_item.get('title')
        description = article_item.get('description')
        url = article_item.get('url')
        image = article_item.get('urlToImage')
        date = article_item.get('publishedAt')

        if image:
            articles_result = Articles(
                id, author, title, description, url, image, date)
            articles_object.append(articles_result)

    return articles_object


def get_news(news_sammary):
    get_news_url = base_url.format(news_sammary, api_key)
    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        get_news_results = None

        if get_news_response['news']:
            get_news_list = get_news_response['news']
            get_news_results = process_news(get_news_list)

    return get_news_results


def process_news(news):
    '''
    Function  that processes the news result and transform them to a list of Objects
    Args:
        news_list: A list of dictionaries that contain news details
    Returns :
        news_results: A list of news objects
    '''
    news_results = []
    for news in news:
        id = news.get('id')
        title = news.get('name')
        sammary = news.get('description')
        link = news.get('url')
        place = news.get('title')
        
        urlToImage = urlToImage
        publishedAt = publishedAt

        news_object = news(id, title, link,sammary, urlToImage,  publishedAt)
        news_results.append(articles_object)

    return news_results
