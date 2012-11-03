from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from MSQCdb import MSQCdb_app
import MSQCdb
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'MSQCdb.views.home', name='home'),
    # url(r'^MSQCdb/', include('MSQCdb.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',{'document_root': MSQCdb.settings.MEDIA_ROOT}),
    url(r'^MSQCdb/', include('MSQCdb.MSQCdb_app.urls')),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login', {'template_name': 'admin/login.html'}),
    url(r'^grappelli/', include('grappelli.urls')),

)
