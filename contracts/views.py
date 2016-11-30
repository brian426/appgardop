from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from userprofiles.models import Userprofile
from contracts.models import Contract
from django import forms

def getall(request):
    contracts = Contract.objects.all()
    context = {
        "contracts" : contracts,
    }
    return render(request,"contract/contract.html",context)

def create_contract(request):
    namecontract = request.POST.get('namecontract', None)
    description = request.POST.get('description', None)
    state = request.POST.get('state', None)

    if request.method == 'POST':
        contrac = Contract.objects.create(namecontract=namecontract,
                                        description=description,
                                        state=state)
        contracts = Contract.objects.all()
        context = {
            "contracts" : contracts,
        }
        return render(request,"contract/contract.html",context)

    context = {}
    return render(request, 'contract/create_contract.html', context)

def update_contract_form(request,pk):
    contract = Contract.objects.get(pk=pk)
    request.session['contract_id'] = contract.id
    context = {
        "contract" : contract,
    }
    return render(request,"contract/update_contract.html",context)

def update_contract(request):
    
    namecontract = request.POST.get('namecontract',None)
    description = request.POST.get('description',None)
    state = request.POST.get('state',None)

    contract_id = request.session.get("contract_id")
    contract = Contract.objects.get(id=contract_id)

    contract.namecontract=namecontract
    contract.description=description
    contract.state=state
    contract.save()

    contracts = Contract.objects.all()
    context = {
        "contracts" : contracts,
    }
    return render(request,"contract/contract.html",context)


def delete_contract(request,pk):
    contract = Contract.objects.get(pk=pk)
    contract.delete()
    contracts = Contract.objects.all()
    context = {
        "contracts" : contracts,
    }
    return render(request,"contract/contract.html",context)