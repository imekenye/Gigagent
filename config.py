import os

class Config:
    
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://studiopx:@localhost/gigagent'
    SECRET_KEY = os.environ.get('SECRET_KEY')
    UPLOADED_PHOTOS_DEST = 'app/static/photos'
    CSRF_ENABLED = True
    #  email configurations


class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")


class DevConfig(Config):

    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://studiopx:12345@localhost/gigagent'
  
    DEBUG = True


config_options = {
'development':DevConfig,
'production':ProdConfig
}