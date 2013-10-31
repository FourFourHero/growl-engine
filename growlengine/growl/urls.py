from django.conf.urls import patterns, url

from growl import views

urlpatterns = patterns('',
    url(r'^bootstrap/', views.bootstrap, name='bootstrap'),
    url(r'^train/inject/', views.train_inject_skill, name='train_inject_skill'),
    url(r'^train/train/', views.train_train_skill, name='train_train_skill'),
    url(r'^train/cancel/', views.train_cancel_train_skill, name='train_cancel_train_skill'),
)