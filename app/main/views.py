from flask import  render_template,redirect,request,url_for,abort,flash
from . import main
from .. import db
from flask_login import login_required
from ..models import User
from forms import ArtistSearchForm

@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''

    title = 'Home - Welcome to Gigagent'

    return render_template('index.html', title=title)


@app.before_request
def before_request():
    g.user = current_user
    if g.user.is_authenticated:
        g.user.last_seen = datetime.utcnow()
        db.session.add(g.user)
        db.session.commit()
        g.search_form = ArtistSearchForm()