#!/usr/bin/python
# -*- coding: UTF-8 -*-
__author__ = 'florije'

from django.conf.urls import patterns, url

from todo import views

# Uncomment the next two lines to enable the admin:

urlpatterns = patterns(
    '',
    url(r'^$', views.todolist, name='todo'),
    url(r'^addtodo/$', views.addTodo, name='add'),
    url(r'^todofinish/(?P<id>\d+)/$', views.todofinish, name='finish'),
    url(r'^todobackout/(?P<id>\d+)/$', views.todoback,  name='backout'),
    url(r'^updatetodo/(?P<id>\d+)/$', views.updatetodo, name='update'),
    url(r'^tododelete/(?P<id>\d+)/$', views.tododelete, name='delete'),

)