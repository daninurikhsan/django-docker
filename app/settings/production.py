from app.settings.base import *

DEBUG = False
ALLOWED_HOSTS = ['127.0.0.1', 'localhost']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.environ.get('MYSQL_DATABASE_NAME'),
        'USER': os.environ.get('MYSQL_DATABASE_USER'),
        'PASSWORD': os.environ.get('MYSQL_DATABASE_PASSWORD'),
        'HOST': os.environ.get('MYSQL_DATABASE_HOST'),
        'PORT': os.environ.get('MYSQL_DATABASE_PORT'),
        'default-character-set': 'utf8',
        'OPTIONS': {
            'use_unicode' : True,
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES', innodb_strict_mode=1",
        },
    }
}