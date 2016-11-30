from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from django.views.generic.edit import UpdateView
from django.contrib.auth.models import User
from contracts.models import Contract
from positions.models import Position
from django import forms
from datetime import datetime

def getall(request):
    positions = Position.objects.all()
    context = {
        "positions" : positions,
    }
    return render(request,"position/position.html",context)

def create_position_form(request):
    contracts = Contract.objects.all()
    context = {
        "contracts" : contracts,
    }
    return render(request,"position/create_position.html",context)

def create_position(request):
    code = request.POST.get('code', None)
    nameposition = request.POST.get('nameposition', None)
    description = request.POST.get('description', None)
    state = request.POST.get('state', None)

    contract_id = request.POST.get('contract', None)
    contract = Contract.objects.get(pk=contract_id)

    if request.method == 'POST':
        position=Position.objects.create(contract=contract,
    										code=code,
                                            nameposition=nameposition,
                                            description=description,
                                            state=state,
                                            registrationdate=datetime.now(),
                                            modificationdate=datetime.now(),)
        position.save()
        positions = Position.objects.all()
        context = {
            "positions" : positions,
        }
        return render(request,"position/position.html",context)

def update_position_form(request,pk):
    position = Position.objects.get(pk=pk)
    contract = position.contract
    contracts = Contract.objects.all()
    
    request.session['position_id'] = position.id
    request.session['contract_id'] = contract.id
    context = {
        "position" : position,
        "contract" : contract,
        "contracts" : contracts,
    }
    return render(request,"position/update_position.html",context)

def update_position(request):
    """ Obtengo datos del formulario """
    code = request.POST.get('code',None)
    nameposition = request.POST.get('nameposition',None)
    description = request.POST.get('description',None)
    state = request.POST.get('state',None)
    contract_id = request.POST.get('contract', None)
    position_id = request.session.get("position_id")
    """ Creo los objetos necesarios para su modificacion """
    contract = Contract.objects.get(pk=contract_id)
    position = Position.objects.get(pk=position_id)

    """ Preparo los objetos con los datos del formulario """
    position.code=code
    position.nameposition=nameposition
    position.description=description
    position.state=state
    position.contract=contract
    position.modificationdate = datetime.now()

    """ Hago el update al objeto """
    position.save()

    """ Actualizo la lista total de objetos a mostrar """
    positions = Position.objects.all()
    context = {
        "positions" : positions,
    }
    return render(request,"position/position.html",context)

def delete_position(request,pk):
    position = Position.objects.get(pk=pk)
    position.delete()
    positions = Position.objects.all()
    context = {
        "positions" : positions,
    }
    return render(request,"position/position.html",context)