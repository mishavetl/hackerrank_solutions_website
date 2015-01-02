from django.conf.urls import patterns, include, url

from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm

import views

urlpatterns = patterns('',
    url('^$', views.about, name="about"),
    url('^archive/$', views.index, name="archive"),
    url('^archive/solution/(?P<id>\w{0,50})/$', views.solution, name="solution"),
    url('^add_solution/$', views.add_solution, name="add_solution"),
    url('^register/', CreateView.as_view(
            template_name='auth/register.html',
            form_class=UserCreationForm,
            success_url='/'), name="register"),
)
