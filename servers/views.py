# Create your views here.
# -*- coding: utf-8 -*-
from django.db.models import Q
import re
from servers.models import Server,Conditions,Registrar
from servers.forms import ServerSearchForm,ServerForm,RegistrarForm

from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response,get_object_or_404
from django.core.urlresolvers import reverse
from django.views.generic import *


def search(request):
   form = ServerSearchForm()
   if request.method == 'GET':
       servers_list = Server.objects.all()
       return render_to_response(
           'servers/search.html', {'form':form, 'servers_list':servers_list}, RequestContext(request))
   elif request.method == 'POST':
        form = ServerSearchForm(request.POST)
        servers_list = Server.objects.all()
   if form.is_valid():
          servers_list = Server.objects.filter(
                  Q(domain_name__contains=form.cleaned_data['domain_name']),
                  Q(company_name__contains=form.cleaned_data['company_name']))
   return render_to_response(
       'servers/search.html',
       {'form':form, 'servers_list':servers_list},
       RequestContext(request))

#-------------サーバ
#リスト表示
class ServerListView(ListView):
    model = Server
    queryset=Server.objects.order_by('id_number')
    context_object_name='latest_server_list'
    template_name = 'servers/index.html'
    print Server.objects.order_by('id_number').query

#詳細表示
class ServerDetailView(DetailView):
    model = Server
    template_name = 'servers/detail.html'

#編集
class ServerUpdateView(UpdateView):
    model = Server
    form_class = ServerForm
    template_name = 'servers/server_form.html'
    success_url = '/ssms/servers'

#新規作成
class ServerCreateView(CreateView):
    model = Server
    form_class = ServerForm
    #template_name = 'servers/poll_form.html'
    template_name = 'servers/server_form.html'
    success_url = '/ssms/servers'

#-------------レジストラ
#新規作成
class RegistrarCreateView(CreateView):
    model = Registrar
    form_class = RegistrarForm
    template_name = 'servers/conditions_form.html'
    success_url = '/ssms/servers/new_registrar/'

#-------------弊社担当者
#新規作成
# class Sainet_chargeCreateView(CreateView):
#     model = Sainet_charge
#     form_class = Sainet_chargeForm
#     template_name = 'servers/conditions_form.html'
#     success_url = '/servers/new_sainet_charge/'
