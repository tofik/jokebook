from django.conf.urls.defaults import *


urlpatterns = patterns('book.views',
                       url(r'^list/$', 'list'),
                       url(r'^new/$', 'new'),
                       url(r'^details/(\d+)/$', 'details'),
                       url(r'^vote/(?P<direction>plus)/(?P<joke_id>\d+)/$','vote'),
                       url(r'^vote/(?P<direction>minus)/(?P<joke_id>\d+)/$','vote'),
                       url(r'^top/$', 'top'),                       
                       )
