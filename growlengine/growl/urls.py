from django.conf.urls import patterns, url

from growl import views

urlpatterns = patterns('',
    url(r'^$', views.bootstrap, name='bootstrap')
)