from settings import *  # noqa

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'meatmedb',
        'USER': 'meatmedbuser',
        'PASSWORD': 'mmdbpass',
        'HOST': '127.0.0.1',
        'PORT': '',
    }
}
