# -*- coding: utf-8 -*-
import os

gettext = lambda s: s

urlpatterns = []

DJANGO_SETTINGS_MODULE = 'djnetaxept.test_utils.cli' # this module
ROOT_URLCONF = DJANGO_SETTINGS_MODULE

def configure(**extra):
    from django.conf import settings
    os.environ['DJANGO_SETTINGS_MODULE'] = DJANGO_SETTINGS_MODULE
    defaults = dict(
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': ':memory:',
            }
        },
        SITE_ID = 1,
        USE_I18N = True,
        EMAIL_BACKEND = 'django.core.mail.backends.locmem.EmailBackend',
        INSTALLED_APPS = [
            'djnetaxept',
            'south'
        ],
        LANGUAGE_CODE = "en",
        LANGUAGES = (
            ('en', gettext('English')),
        ),
        ROOT_URLCONF = ROOT_URLCONF,
    )
    defaults.update(extra)
    settings.configure(**defaults)