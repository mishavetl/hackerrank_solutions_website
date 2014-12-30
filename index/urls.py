from django.conf.urls import patterns, include, url

import views

urlpatterns = patterns('',
    url('^$', views.index, name="index"),
    url('^solution/(?P<id>\w{0,50})/', views.solution, name="solution"),
    url('^add_solution/', views.add_solution, name="add_solution"),
)
