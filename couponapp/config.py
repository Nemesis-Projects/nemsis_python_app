WTF_CSRF_ENABLED = True
SECRET_KEY = 'your-secret-key-here'

OPENID_PROVIDERS = [
    {'name': 'Google', 'url': 'https://www.google.com/accounts/o8/id'},
    {'name': 'Yahoo', 'url': 'https://me.yahoo.com'},
    {'name': 'AOL', 'url': 'http://openid.aol.com/<username>'},
    {'name': 'Flickr', 'url': 'http://www.flickr.com/<username>'},
    {'name': 'MyOpenID', 'url': 'https://www.myopenid.com'}]

GOOGLE_LOGIN_CLIENT_ID = " 347912272374-r4336hago8i0aqclpskajqfopcnad63i.apps.googleusercontent.com "
GOOGLE_LOGIN_CLIENT_SECRET = "gUXLorTIx3UrAiOjTEL8eSNU"

OAUTH_CREDENTIALS={
        'google': {
            'id': GOOGLE_LOGIN_CLIENT_ID,
            'secret': GOOGLE_LOGIN_CLIENT_SECRET
        }
}

import os
basedir = os.path.abspath(os.path.dirname(__file__))