from __future__ import absolute_import, print_function

from sentry.auth.provider import MigratingIdentityId
from sentry.auth.providers.oauth2 import (
    OAuth2Callback, OAuth2Provider, OAuth2Login
)

from .views import PhabricatorConfigureView

from .constants import (
    AUTHORIZE_URL, ACCESS_TOKEN_URL, CLIENT_ID, CLIENT_SECRET
)

class PhabricatorOAuth2Callback(OAuth2Callback):
    client_id = CLIENT_ID
    client_secret = CLIENT_SECRET

    def __init__(self, access_token_url=None, **config):
        super(PhabricatorOAuth2Callback, self).__init__(access_token_url=access_token_url, **config)

    def get_token_params(self, code, redirect_uri):
        return {
            "grant_type": "token",
            "code": code,
            "redirect_uri": redirect_uri,
            "client_id": self.client_id,
            "client_secret": self.client_secret,
        }


class PhabricatorOAuth2Provider(OAuth2Provider):
    name = 'Phabricator'
    access_token_url = ACCESS_TOKEN_URL
    authorize_url = AUTHORIZE_URL
    client_id = CLIENT_ID
    client_secret = CLIENT_SECRET

    def __init__(self, **config):
        super(PhabricatorOAuth2Provider, self).__init__(**config)

    def get_configure_view(self):
        return PhabricatorConfigureView.as_view()

    def get_auth_pipeline(self):
        return [
            OAuth2Login(
                authorize_url=self.authorize_url,
                client_id=self.client_id,
                scope='whoami',
            ),
            PhabricatorOAuth2Callback(
                access_token_url=self.access_token_url,
            ),
        ]

    def get_setup_pipeline(self):
        return self.get_auth_pipeline()

    def get_refresh_token_url(self):
        return ACCESS_TOKEN_URL

    def build_identity(self, state):
        data = state['data']
        return {
            'id': '',
            'email': '',
            'name': '',
            'data': self.get_oauth_data(data),
        }