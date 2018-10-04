import os


class Config:
    '''
    General configuration parent class
    '''
    # contains configurations that are used in both production and development stages. 
    NEWS_API_BASE_URL ='https://newsapi.org/v2/top-headlines -G \-d country=us \-d apiKey'
    NEWS_API_KEY = os.environ.get('NEWS_API_KEY')
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SOURCES_API_BASE_URL = 'https://newsapi.org/v2/sources?country=us&category={}&apiKey={}'
    NEWS_API_BASE_URL = 'https://newsapi.org/v2/top-headlines?sources={}&apiKey={}'
    CATG_API_BASE_URL = 'https://newsapi.org/v2/top-headlines?category={}&country=us&apiKey={}'
    # NEWS_API_KEY = os.environ.get('NEWS_API_KEY')
    # SECRET_KEY = os.environ.get('SECRET_KEY')



class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    #  contains configurations that are used in production stages of our application and inherits from the parent
    pass


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    #  contains configurations that are used in development stages of our application and inherits from the parent

    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}