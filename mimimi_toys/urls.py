from django.conf.urls import patterns, include, url
from django.contrib import admin
from mimimi_toys.settings import DEBUG
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = patterns('',
    url(r'^$', include('landing.urls')),
    url(r'^page/', include('django.contrib.flatpages.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^redactor/', include('redactor.urls')),
)

if DEBUG:
    urlpatterns += staticfiles_urlpatterns()
