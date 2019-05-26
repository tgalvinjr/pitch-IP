import os

class Config:
    SECRET_KEY = 'alvin'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://alvin:alvin123@localhost/pitch'
    UPLOADED_PHOTOS_DEST = 'app/static/photos'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'tgalvin.jr@gmail.com'
    MAIL_PASSWORD = 'alvin123'
    # simple mde  configurations
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True
class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://alvin:alvin123@localhost/pitch'

class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://alvin:alvin123@localhost/pitch_test'

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://alvin:alvin123@localhost/pitch'
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig,
'test':TestConfig
}
