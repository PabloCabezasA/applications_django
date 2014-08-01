# -*- encoding: utf-8 -*-
from django.shortcuts import render,render_to_response
from django.http import Http404, HttpResponseRedirect
from django.template import RequestContext
from myweb.forms import AccountAccountForm
from myweb.models import AccountAccount
# Create your views here.

def index(request):
    cuentas = AccountAccount.objects.all()
    return render_to_response('myweb/Account_Account_tree.html',{'cuentas':cuentas}, context_instance=RequestContext(request))


def create_account_account(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = AccountAccountForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            form.save()
            # process the data in form.cleaned_data as required            
            # redirect to a new URL:
            return HttpResponseRedirect('/myweb/accountform/')
    # if a GET (or any other method) we'll create a blank form
    else:
        form = AccountAccountForm()
    return render(request, 'myweb/Account_Account_form.html', {'form': form})    