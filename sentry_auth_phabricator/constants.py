from __future__ import absolute_import, print_function

from django.conf import settings

CLIENT_ID = getattr(settings, 'PHABRICATOR_CLIENT_ID', None)

CLIENT_SECRET = getattr(settings, 'PHABRICATOR_CLIENT_SECRET', None)

PHABRCIATOR_DOMAIN = getattr(settings, 'PHABRICATOR_DOMAIN')

ACCESS_TOKEN_URL = 'https://{0}/oauthserver/token/'.format(PHABRCIATOR_DOMAIN)
AUTHORIZE_URL = 'https://{0}/oauthserver/auth/'.format(PHABRCIATOR_DOMAIN)