from django.conf import settings
from django.conf.urls.defaults import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
                       # Application urls
                       url(r"^book/", include("book.urls")),
                       
                       # Admin urls
                       (r'^admin/', include(admin.site.urls)),
                       (r'^admin/doc/', include('django.contrib.admindocs.urls')),
                       )


if settings.DEBUG:
    urlpatterns += patterns("django.views",
                            url(r"^static/(?P<path>.*)", 
                                "static.serve", 
                                { "document_root": settings.MEDIA_ROOT,
                                  'show_indexes': True })   
                            )
