from django.conf.urls import patterns, include, url

import views

urlpatterns = patterns('',
    url(r'^login/$', 'django.contrib.auth.views.login',
        {'template_name': 'auth/login.html'}, name='login'),

    url(r'^logout/$', 'django.contrib.auth.views.logout',
        {'next_page': '/'}, name='logout'),
    url(r'^register/$', views.register, name='register')
)
