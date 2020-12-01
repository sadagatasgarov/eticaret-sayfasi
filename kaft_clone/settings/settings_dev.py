import os
from .settings_base import BASE_DIR, INSTALLED_APPS
# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, '../db.sqlite3'),
    }
}

# print(os.path.join(BASE_DIR, '../db.sqlite3'))


if os.environ.get('DJANGO_DEBUG') == 'True':
    INSTALLED_APPS += [
        'django_extensions'
    ]
