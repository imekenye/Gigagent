from flask import  render_template,redirect,request,url_for,abort,flash
from . import main
from .. import db
from flask_login import login_required
from ..models import User
@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''

    title = 'Home - Welcome to Gigagent'

    return render_template('index.html', title=title)