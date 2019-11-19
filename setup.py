from setuptools import setup

install_requires = [
    'sentry>=9.0.0',
]

setup(
    name='sentry_auth_github',
    version='0.1',
    description='Enable authentication with phabricator for sentry',
    url='https://github.com/chenyuy/sentry-auth-phabricator',
    authro='Chenyu Yang',
    author_email='realchenyuy@gmail.com',
    license='MIT',
    packages=['sentry_auth_phabricator'],
    zip_safe=False,
    install_requires=install_requires,
    include_package_data=True,
    entry_points={
        'sentry.apps': [
            'auth_phabricator = sentry_auth_phabricator',
        ],
    },
)