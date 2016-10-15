from django.conf.urls import patterns, include, url
from django.contrib import admin
from api import views

urlpatterns = patterns('',
    url(r'^admin/$', include(admin.site.urls)),
    url(r'^home/$', views.home),
    url(r'^adduser/$', views.add_user),
    url(r'^delete/$', views.deleteuser),
    url(r'^userdetails/$', views.users),
    url(r'^addnewuser/$', views.adduser),
    url(r'^update_or_delete/$', views.update_or_delete)
)
