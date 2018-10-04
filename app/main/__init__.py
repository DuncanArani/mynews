from flask import Flask
from flask import Blueprint
main = Blueprint('main',__name__)
from . import views,errors
from flask import render_template,request,redirect,url_for
# Initializing application
app = Flask(__name__)

from app.main import views #allow us to create views.

@app.route('/')
def index():
    return render_template('index.html')