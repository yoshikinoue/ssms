# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.views.generic import *
from django.contrib import admin
admin.autodiscover()

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ssms.views.home', name='home'),
    # url(r'^ssms/', include('ssms.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
	url(r'^admin/', include(admin.site.urls)),
	url(r'^servers/', include('servers.urls')),
	#トップページ。スレッド一覧のページにリダイレクトする
	url(r'^$', RedirectView.as_view(url='./servers/')),
)
