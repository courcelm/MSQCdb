from django.conf.urls import patterns, url
from MSQCdb.MSQCdb_app.views import *

from django.conf.urls import *

urlpatterns = patterns('',
    url(r'^timelineDataJSON/(?P<seriesId>\d+)/.*$', timelineDataJSON),                       
    url(r'^histoDataJSON/(?P<seriesId>\d+)/.*$', histoDataJSON),
    url(r'^chartView/(?P<chartId>.*)/(?P<position>.*)$', chartView),
    url(r'^timelineView/(?P<chartId>.*)/(?P<position>.*)$', timelineView),
    url(r'^histoView/(?P<chartId>.*)/(?P<position>.*)$', histoView),
    url(r'^reportView/(?P<reportId>.*)$', reportView),
    url(r'^fieldOptions/(?P<modelName>.*)$', fieldOptions),
    url(r'^reservationJSON/$', reservationJSON),
    url(r'^reservationCalendar/$', reservationCalendar),
    url(r'^reservationPerUser/(?P<year>\d+)/.*$', reservationPerUser),
)