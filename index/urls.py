from django.conf.urls import patterns, include, url

import views

urlpatterns = patterns('',
    url('^$', views.about, name="about"),
    url('^archive/$', views.index, name="archive"),
    url('^archive/solution/(?P<id>\w{0,50})/$', views.solution, name="solution"),
    url('^add_solution/$', views.add_solution, name="add_solution"),
    # url('^register/', views.register, name="register")
)
