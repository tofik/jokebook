from django.conf.urls.defaults import *


urlpatterns = patterns('book.views',
                       url(r'^list/$', 'list'),
                       url(r'^new/$', 'new'),
                       url(r'^details/(\d+)/$', 'details'),
                       )
