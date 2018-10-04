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
    global api_key, base_url,  catg_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['SOURCES_API_BASE_URL']
    NEWS_url = app.config['NEWS_API_BASE_URL']
    catg_url = app.config['CATG_API_BASE_URL']


def get_source(source_name):
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
    get_articles_url = base_url.format(id, api_key)
    with urllib.request.urlopen(get_articles_url) as url:
        get_articles_data = url.read()
        get_articles_response = json.loads(get_articles_data)

        get_articles_results = None

        if get_articles_response['article']:
            get_articles_list = get_articles_response['article']
            get_articles_results = process_articles(get_articles_list)

    return get_articles_results


def process_articles(articles):
    '''
    Function  that processes the news result and transform them to a list of Objects
    Args:
        news_list: A list of dictionaries that contain news details
    Returns :
        news_results: A list of news objects
    '''
    articles_results = []
    for article in artyicles:
        id = articles.get('id')
        title = articles.get('title')
        sammary = articles.get('descriptrion')
        link = articles.get('url')
        place = articles.get('title')
        urlToImage = urlToImage
        publishedAt = publishedAt

        articles_object = Article(
            id, title, link, description, urlToImage,  publishedAt)
        articles_results.append(artcle_object)

    return articles_results


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
        sammary = news.get('descriptrion')
        link = news.get('url')
        place = news.get('title')
        urlToImage = urlToImage
        publishedAt = publishedAt

        news_object = news(
            id, title, link, url, description, urlToImage,  publishedAt)
        news_results.append(artcle_object)

    return news_results
