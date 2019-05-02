from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_whooshalchemy
from ... import config

app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=True
db = SQLAlchemy(app)

class ArtistSearchForm(Form):
    search = StringField('search', validators=[DataRequired()])