====================
django-json-settings
====================

django-json-settings is a small Django application that allows you to provide
specific local settings in JSON format, generally for production or other
non-developer environments (although it could also be used for settings that
vary on a per-developer basis).

This presumes you are deploying into a virtualenv, and it imposes a few
assumptions about how that virtualenv should be structured, based on standard
UNIX naming.

What it does
============

When deployed in a virtualenv, and called from your settings.py,
django-json-settings looks for a file called::

    <sys.prefix>/etc/settings.json

This file is then read and it's contents placed into the standard django
settings.

You do this by putting::

    from json_settings import *
    
In your settings.py at an appropriate point.

Additional magic settings
=========================

In addition to this, django-json-settings will set three new values (if they aren't already defined)::

    VAR_DIRECTORY to <sys.prefix>/var
    STATIC_ROOT to <VAR_DIRECTORY>/static
    MEDIA_ROOT to <VAR_DIRECTORY>/media

These are quite useful things to have configured.

How to use it
=============

Obviously first you should add a dependency to your setup.py on django-json-settings, and then install it.

Then add a call to "from json_settings import *" in your settings.py at the
right point. Generally you should structure your settings.py so that you have
3 types of setting:

 1. Things that are definitely going to need to be set in production. For example, ADMINS, ALLOWED_HOSTS, SECRET_KEY, STATIC_ROOT
 2. Things you might want to change in production, but might want to leave alone, for example LOGGING
 3. Things you don't want to change in production, ever. For example, MIDDLEWARE_CLASSES
 
You should put the json_settings import statement after all of those in 2, but before those in 3.
 
This means whoever is deploying the software gets lots of choice about the
environment, but can't accidentally hose things that are really core
application configuration.
 
Here is an example settings.py::

    import sys
    import os
    
    DEBUG = True
    ADMINS = (
    )

    ALLOWED_HOSTS = []
    TIME_ZONE = 'Europe/London'

    SECRET_KEY = '*ivd!%8j-=7r36ng^)rmeto(wj)#9)ylzd_hhrzv#x%+a)gs8x'

    SESSION_COOKIE_AGE = 3600

    LANGUAGE_CODE = 'en-us'
    
    STATIC_ROOT = 'static/'
    MEDIA_ROOT = 'media/'

    from json_settings import *

    TEMPLATE_DEBUG = DEBUG
    MANAGERS = ADMINS

    SITE_ID = 1
    
    ...
    

Testing local settings
======================

You can use a different settings file by setting an environment variable
JSON_SETTINGS::

    JSON_SETTINGS=example.json ./manage.py runserver

If you want to try some settings out.

Error Handling
==============

If the settings.json file is invalid then your application will terminate
with an error.

If the file is absent then this is only an error if it was provided using the
JSON_SETTINGS environment variable. A missing file is otherwise assumed to be
ok (so you can put development defaults in your settings.py and not have a
local settings file at all).



