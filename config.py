import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    LOG_TO_STDOUT = os.environ.get('LOG_TO_STDOUT')
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    ADMINS = ['your-email@example.com']
    LANGUAGES = ['en', 'es']
    MS_TRANSLATOR_KEY = os.environ.get('MS_TRANSLATOR_KEY')
    ELASTICSEARCH_URL = os.environ.get('ELASTICSEARCH_URL')
    REDIS_URL = os.environ.get('REDIS_URL') or 'redis://'
    POSTS_PER_PAGE = 25
    # S3_BUCKET                 = os.environ.get("S3_BUCKET_NAME")
    # S3_KEY                    = os.environ.get("S3_ACCESS_KEY")
    # S3_SECRET                 = os.environ.get("S3_SECRET_ACCESS_KEY")

    S3_BUCKET                 = 'flask-toolio'
    S3_KEY                    = 'AKIAR372B6T2IJUY6LEZ'
    S3_SECRET                 = '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'
    S3_LOCATION               = 'http://{}.s3.amazonaws.com/'.format(S3_BUCKET)

    SECRET_KEY                = os.urandom(32)
    DEBUG                     = True
    PORT                      = 5000
