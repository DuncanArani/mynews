from flask import render_template
from . import main  # importing data from main
from ..requests import get_sources, get_articles
from ..models import Sources, Articles


@main.route('/')
def index():
    '''
    root direcroy holdng all the sources views
    '''
    general = get_sources('general')
    business = get_sources('business')
    entertainment = get_sources('entertainment')
    technology = get_sources('technology')
    science = get_sources('science')

    # for i in real_news:
    #     print(i.name)
    title = "hello world"
    return render_template('index.html', title=title, general=general, business=business, entertainment=entertainment, technology=technology, science=science)


@main.route('/articles/<id>')
def articles(id):
    '''
    view all article based of each source through the everything Api
    '''

    articles = get_articles(id)

    return render_template('article.html', articles=articles)