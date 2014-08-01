__author__ = 'pablo'
from django.conf.urls import patterns, include, url
from myweb import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^accountform/$', views.create_account_account, name='create_account_account'),    
)
