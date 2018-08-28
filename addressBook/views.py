# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Address

# Create your views here.

@login_required(login_url="/accounts/login/")
def addressBook_view(request):
    allAddress = Address.objects.all()
    address = []
    for i in allAddress:
        if(i.owner == request.user.username):
            address.append(i)
    return render(request, 'addressBook/list.html', {'address':address})

@login_required(login_url="/accounts/login/")
def newAddress_view(request):
    if(request.method == 'POST'):
        newAddress = Address()
        newAddress.firstName = request.POST.get("firstname","")
        newAddress.lastName = request.POST.get("lastname","")
        newAddress.phoneNumber = request.POST.get("phone","")
        newAddress.emailAddress = request.POST.get("email","")
        newAddress.streetAddress = request.POST.get("streetaddress","")
        newAddress.owner = request.user.username
        newAddress.save()
    return render(request, 'addressBook/newAddress.html')