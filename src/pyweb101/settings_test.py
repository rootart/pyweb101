from settings import *

DEBUG = True
TEMPLATE_DEBUG = True

LOCAL_INSTALLED_APPS = ('django_coverage', 'django_nose')
INSTALLED_APPS += LOCAL_INSTALLED_APPS

SOUTH_TESTS_MIGRATE = False
SOUTH_DATABASE_ADAPTER='south.db.psycopg2'
SKIP_SOUTH_TESTS = True

TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(PROJECT_DIR, 'pyweb101_test.db'),
        'USER': '', 
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

SECRET_KEY = '(%^c!d(u01y&amp;uf^l1&amp;09)z-@ecll6jd^va6(s-ael&amp;c+q58h=5'

if DEBUG:
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'



