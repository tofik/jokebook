from django.conf.urls.defaults import *


urlpatterns = patterns('book.views',
                       url(r'^list/$', 'list'),
                       url(r'^new/$', 'new'),
                       url(r'^details/(\d+)/$', 'details'),
                       url(r'^vote_plus/(\d+)/$', 'vote_plus'),
                       url(r'^vote_minus/(\d+)/$', 'vote_minus'),
                       url(r'^top/$', 'top'),                       
                       )
