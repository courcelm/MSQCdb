from django.conf.urls import patterns, url
from MSQCdb.MSQCdb_app.views import *

from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(r'^chartDataJSON', chartDataJSON),                       
    url(r'^chartView', chartView),
)