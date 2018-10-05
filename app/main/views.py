from flask import render_template
from . import main
from ..requests import get_sources, get_articles,get_news

from ..models import Sources

# Views


@main.route('/')
def index():
    ''',
    View root page function that returns the index page and its data
    '''

    # Getting top news
    sources = get_sources('business')
    sports_sources = get_sources('sports')
    technology_sources = get_sources('technology')
    entertainment_sources = get_sources('entertainment')
    general_sources = get_sources('general')
    articles_sources = get_sources('articles')
    news_sources = get_sources('news')

    title = "News Room"

    return render_template('index.html', title=title, sources=sources, sports_sources=sports_sources, technology_sources=technology_sources, entertainment_sources=entertainment_sources, general_sources=general_sources, article_sources=articles_sources, news_sources=news_sources)


@main.route('/sources/<id>')
def articles(id):
    '''
    view articles page
    '''
    articles = get_articles(id)
    title = f'NH | {id}'

    return render_template('index.html', title=title, articles=articles)


@main.route('/news/<id>')
def news(id):

    # view root page function that returns the news page and its data

    news = get_news(id)

    return render_template('index.html', news=articles)


@main.route('/categories/<category>')
def general(category):

    # view root page function that returns the categories page and its data

    news_categories_articles = category(category)

    return render_template('index.html', general=news_categories_articles)


@main.route('/categories/<category>')
def business(category):

    # view root page function that returns the categories page and its data

    news_categories_articles = category(category)

    return render_template('index.html', business=news_categories_articles)


@main.route('/categories/<category>')
def entertainment(category):

    # view root page function that returns the categories page and its data

    news_categories_articles =category(category)

    return render_template('index.html', entertainment=news_categories_articles)


# @main.route('/categories/<category>')
# def health(category):

#     #view root page function that returns the categories page and its data

#     news_categories_articles = get_category(category)

#     return render_template('health.html', health = news_categories_articles)
