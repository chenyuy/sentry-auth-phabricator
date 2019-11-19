from __future__ import absolute_import

from django.apps import AppConfig


class Config(AppConfig):
    name = "sentry_auth_phabricator"

    def ready(self):
        from sentry.auth import register

        from .provider import PhabricatorOAuth2Provider

        register('phabricator', PhabricatorOAuth2Provider)
