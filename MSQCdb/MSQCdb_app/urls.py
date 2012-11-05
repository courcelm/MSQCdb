from django.conf.urls import patterns, url
from MSQCdb.MSQCdb_app.views import *

from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(r'^chartDataJSON', chartDataJSON),                       
    url(r'^chartView/(?P<chartId>.*)$', chartView),
    url(r'^fieldOptions/(?P<modelName>.*)$', fieldOptions),
)