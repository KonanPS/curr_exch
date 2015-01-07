from django.conf.urls import patterns, include, url
from django.contrib import admin
import django.contrib.staticfiles
import views

#from django.conf.urls.defaults import *

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Curr_exch.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^curr_exch/$', views.cur_exchange),
)
