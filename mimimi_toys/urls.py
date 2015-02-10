from django.conf.urls import patterns, include, url
from django.contrib import admin
from mimimi_toys.settings import DEBUG
urlpatterns = patterns('',
    url(r'^$', include('landing.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

if DEBUG:
    urlpatterns += patterns('', (
        r'^static/(?P<path>.*)$',
        'django.views.static.serve',
        {'document_root': 'static'}
    ))