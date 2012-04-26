INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    ]

INSTALLED_APPS += [
    '{{ project_name }}.apps.core',
    ]

INSTALLED_APPS += [
    'debug_toolbar',
    'south',
    'django_coverage',
    ]
