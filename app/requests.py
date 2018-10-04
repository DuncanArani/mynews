import urllib.request,json
from .models import Source
# Highlights = Highlights


# Getting api key
api_key = None
# Getting the highlights base url
base_url = None
highlights_url = None
catg_url = None


def configure_request(app):
    global api_key, base_url,  catg_url
    api_key = app.config['HIGHLIGHTS_API_KEY']
    base_url = app.config['SOURCES_API_BASE_URL']
    highlights_url = app.config['HIGHLIGHTS_API_BASE_URL']
    catg_url = app.config['CATG_API_BASE_URL']


def get_source(source_name):
    get_source_url = base_url.format(source_name,api_key)
    with urllib.request.urlopen(get_source_url) as url:
        get_source_data = url.read()
        get_source_response = json.loads(get_source_data)

        get_source_results = None

        if get_source_response['sources']:
            get_source_list = get_source_response['sources']
            get_source_results = process_sources(get_source_list)


    return get_source_results