from flask import render_template
from . import main
from ..requests import get_source
from ..models import Source

# Views
@main.route('/')
def index():

    ''',
    View root page function that returns the index page and its data
    '''

    # Getting top news highlights
    business = get_source('business')
    sports = get_source('sports')
    technology = get_source('technology')
    general = get_source('general')

    # title = 'Home - Welcome to the number 1 news highlighting website online'

    

    
    return render_template('index.html', business = business, sports =sports, technology = technology, general =general )


