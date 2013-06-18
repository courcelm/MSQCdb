import os
import sys
import django.core.handlers.wsgi

sys.path.append('/home/django/py/MSQCdb')
os.environ['DJANGO_SETTINGS_MODULE'] = 'MSQCdb.settings'

_application = django.core.handlers.wsgi.WSGIHandler()

def application(environ, start_response):
    environ['SCRIPT_NAME'] = ''
    environ['PATH_INFO'] = environ['SCRIPT_NAME'] + environ['PATH_INFO']
    return _application(environ, start_response)

