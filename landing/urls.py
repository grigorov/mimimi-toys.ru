from django.conf.urls import patterns, include, url

urlpatterns = patterns('landing.views',
    url(r'^$', 'index', name='index'),
    url(r'^add_order/$', 'add_order', name='add_order'),
)
