from django.conf.urls import patterns, include, url
from django.contrib import admin

from index import urls as index_urls

urlpatterns = patterns('',
    # Admin UI urls
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),

    # Login, logout urls
    url(r'^login/$', 'django.contrib.auth.views.login',
        {'template_name': 'auth/login.html'}, name='login'),

    url(r'^logout/$', 'django.contrib.auth.views.logout',
        {'next_page': '/'}, name='logout'),

    # Other urls, see urls in index app
    url('', include(index_urls), name="index"),
)
