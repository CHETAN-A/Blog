from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.list, name='list' ),
    url(r'^create/$', views.create ),
    url(r'^(?P<slug>[\w-]+)/delete/$', views.delete ),
    url(r'^(?P<slug>[\w-]+)/edit/$', views.update , name="update"),
    url(r'^(?P<slug>[\w-]+)/$', views.detail,name="detail" ),
]