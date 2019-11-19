from __future__ import absolute_import

import six
from django import forms
from sentry.auth.view import AuthView, ConfigureView
from sentry.models import AuthIdentity

class PhabricatorConfigureView(ConfigureView):
    def dispatch(self, request, auth_provider):
        return self.render('sentry_auth_github/configure.html')