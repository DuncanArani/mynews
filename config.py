import os


class Config:
    '''
    General configuration parent class
    '''
    NEWS_SOURCE_BASE_URL = 'https://newsapi.org/v2/sources?category={}&apiKey={}'
    NEWS_ARTICLE_BASE_URL = 'https://newsapi.org/v2/everything?sources={}&apiKey={}'
    NEWS_TOPHEADLINES_BASE_URL = ''

    NEWS_KEY = os.environ.get('NEWS_KEY')
    SECRET_KEY = os.environ.get('SECRET_KEY')


class ProdConfig(Config):

    '''
    Production  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''

    pass


class DevConfig(Config):

    DEBUG = True


config_options = {
    'development': DevConfig,
    'production': ProdConfig
}