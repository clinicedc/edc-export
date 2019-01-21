#!/usr/bin/env python
import django
import logging
import sys

from django.conf import settings
from django.test.runner import DiscoverRunner
from os.path import abspath, dirname, join

APP_NAME = 'edc_export'


class DisableMigrations:

    def __contains__(self, item):
        return True

    def __getitem__(self, item):
        return None


installed_apps = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.messages',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.staticfiles',
    'django_crypto_fields.apps.AppConfig',
    'django_revision.apps.AppConfig',
    'edc_appointment.apps.AppConfig',
    'edc_timepoint.apps.AppConfig',
    'edc_protocol.apps.AppConfig',
    'edc_metadata.apps.AppConfig',
    'edc_identifier.apps.AppConfig',
    'edc_device.apps.AppConfig',
    'edc_registration.apps.AppConfig',
    'edc_visit_schedule.apps.AppConfig',

    f'{APP_NAME}.apps.AppConfig',
]

DEFAULT_SETTINGS = dict(
    BASE_DIR=join(dirname(dirname(abspath(__file__))), 'edc-export'),
    ALLOWED_HOSTS=['localhost'],
    DEBUG=True,
    # AUTH_USER_MODEL='custom_user.CustomUser',
    ROOT_URLCONF=f'{APP_NAME}.urls',
    STATIC_URL='/static/',
    INSTALLED_APPS=installed_apps,
    DATABASES={
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
        },
    },
    TEMPLATES=[{
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ]
        },
    }],
    MIDDLEWARE=[
        'django.middleware.security.SecurityMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    ],

    LANGUAGE_CODE='en-us',
    TIME_ZONE='UTC',
    USE_I18N=True,
    USE_L10N=True,
    USE_TZ=True,

    APP_NAME=f'{APP_NAME}',
    SITE_ID=10,
    EDC_BOOTSTRAP=3,
    VERBOSE_MODE=None,
    DASHBOARD_URL_NAMES={
        'subject_dashboard_url': 'edc_export:subject_dashboard_url',
    },

    DEFAULT_FILE_STORAGE='inmemorystorage.InMemoryStorage',
    MIGRATION_MODULES=DisableMigrations(),
    PASSWORD_HASHERS=('django.contrib.auth.hashers.MD5PasswordHasher', ),
    AUTH_PASSWORD_VALIDATORS=[
        {
            'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
        },
        {
            'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        },
        {
            'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
        },
        {
            'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
        },
    ],
)

if not DEFAULT_SETTINGS.get('DEBUG'):
    DEFAULT_SETTINGS.update(KEY_PATH=join(
        DEFAULT_SETTINGS.get('BASE_DIR'), 'crypto_fields'))


def main():
    if not settings.configured:
        settings.configure(**DEFAULT_SETTINGS)
    django.setup()
    failures = DiscoverRunner(failfast=True).run_tests(
        [f'{APP_NAME}.tests'])
    sys.exit(failures)


if __name__ == "__main__":
    logging.basicConfig()
    main()
