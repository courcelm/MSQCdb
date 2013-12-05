from django.conf.urls import patterns, url
from MSQCdb.MSQCdb_app.views import *

from django.conf.urls import *

urlpatterns = patterns('',
    url(r'^chartDataJSON/(?P<seriesId>\d+)/.*$', chartDataJSON),                       
    url(r'^chartView/(?P<chartId>.*)/(?P<position>.*)$', chartView),
    url(r'^reportView/(?P<reportId>.*)$', reportView),
    url(r'^fieldOptions/(?P<modelName>.*)$', fieldOptions),
    url(r'^reservationJSON/$', reservationJSON),
    url(r'^reservationCalendar/$', reservationCalendar),
    url(r'^reservationPerUser/(?P<year>\d+)/.*$', reservationPerUser),
)