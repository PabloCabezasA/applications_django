# -*- encoding: utf-8 -*-
from django.shortcuts import render,render_to_response
from django.http import Http404, HttpResponseRedirect
from django.template import RequestContext

# Create your views here.

def index(request):
    return render_to_response('index_page.html', context_instance=RequestContext(request))