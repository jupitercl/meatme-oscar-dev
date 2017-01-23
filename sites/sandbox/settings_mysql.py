import pymysql
pymysql.install_as_MySQLdb()

from settings import *  # noqa

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'meatmedb',
        'USER': 'meatmedbuser',
        'PASSWORD': 'mmdbpass',
        'HOST': 'localhost',
        'PORT': '',
    }
}
