# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from servers.models import Server
from servers.views import ServerListView, ServerDetailView, ServerCreateView, ServerUpdateView, RegistrarCreateView
#import views

urlpatterns = patterns('',
                       #/servers/一覧表示
                       url(r'^$', ServerListView.as_view(), name='server-list'),
                       #ＩＤ順
                       url(r'^id_number/$',
                           ServerListView.as_view(
                               queryset=Server.objects.order_by('id_number'), )),
                       #ドメイン順
                       url(r'^domain_name/$',
                           ServerListView.as_view(
                               queryset=Server.objects.order_by('domain_name'), )),
                       #会社順aaaa
                       url(r'^company_name/$',
                           ServerListView.as_view(
                               queryset=Server.objects.order_by('company_name'), )),
                       #担当者順
                       url(r'^sainet_charge/$',
                           ServerListView.as_view(
                               queryset=Server.objects.order_by('sainet_charge'), )),
                       #詳細ページ
                       # url(r'^(?P<pk>\d+)/$',
                       # 	DetailView.as_view(
                       # 		model=Server,
                       # 		template_name='servers/detail.html')),
                       url(r'^(?P<pk>\d+)/$', ServerDetailView.as_view(), ),

                       #新規作成ページ
                       # url(r'^new/$',
                       # 	CreateView.as_view(
                       # 		model=Server,
                       # 		template_name='servers/create.html',
                       # 		success_url='/servers')),
                       url(r'^new/$', ServerCreateView.as_view(), ),

                       #編集ページ
                       # url(r'^Update/(?P<pk>\d+)/$',
                       # 	UpdateView.as_view(
                       # 		model=Server,
                       # 		template_name='servers/update.html',
                       # 		success_url='/servers')),
                       url(r'^Update/(?P<pk>\d+)/$', ServerUpdateView.as_view(), ),

                       #ヘルプページ
                       url(r'^help/$',
                           TemplateView.as_view(
                               template_name='servers/help.html')),
                       #検索ページ
                       url(r'^search/$', 'servers.views.search'),

                       #レジストラ
                       url(r'^new_registrar/$', RegistrarCreateView.as_view(), ),

                       # #担当者
                       # url(r'^new_sainet_charge/$', Sainet_chargeCreateView.as_view(),),
)