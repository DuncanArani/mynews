from flask import render_template
from . import main
from ..requests import get_sources, get_articles

from ..models import Source

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

    title = "News Room"

    return render_template('index.html', title=title, sources=sources, sports_sources=sports_sources, technology_sources=technology_sources, entertainment_sources=entertainment_sources, general_sources=general_sources)

    # title = 'Home - Welcome to the number 1 news highlighting website online'

    # return render_template('index.html', business=business, sports=sports, technology=technology, entertainment = entertainmment, general=general)
