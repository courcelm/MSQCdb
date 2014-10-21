import os
import sys
from django.core.wsgi import get_wsgi_application

sys.path.append('/home/django/py/MSQCdb')
os.environ['DJANGO_SETTINGS_MODULE'] = 'MSQCdb.settings'

_application = get_wsgi_application()

def application(environ, start_response):
    environ['SCRIPT_NAME'] = ''
    environ['PATH_INFO'] = environ['SCRIPT_NAME'] + environ['PATH_INFO']
    return _application(environ, start_response)


