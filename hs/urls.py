from django.conf.urls import patterns, include, url
from django.contrib import admin

from index import urls as index_urls

urlpatterns = patterns('',
    # Admin UI urls
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),

    # Phileo liking widget urls
    url(r'^likes/', include('phileo.urls')),

    # Login, logout urls
    url(r'^auth/', include('login.urls')),

    # Other urls, see urls in index app
    url('', include(index_urls), name="index"),
)
