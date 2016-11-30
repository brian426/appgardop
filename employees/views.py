from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from django.views.generic.edit import UpdateView
from django.contrib.auth.models import User
from django.contrib import messages
from userprofiles.models import Userprofile
from employees.models import Employee
from employees.models import Scheduleemployee
from positions.models import Position
from django import forms

def signin(request):
    if request.user.is_authenticated():
        return redirect('/')
    else:
        if request.method == 'POST':
            email = request.POST.get('email', None)
            password = request.POST.get('password', None)
            user = authenticate(email=email, password=password)
            login(request, user)
            employee = Employee.objects.get(userprofile=user)
            return redirect('/') 

    context = {}
    return render(request, 'sign/signin.html', context)

def getall(request):
    employees = Employee.objects.all()
    context = {
        "employees" : employees,
    }
    return render(request,"employee/employee.html",context)

def create_employee_form(request):
    positions = Position.objects.all()
    context = {
        "positions" : positions,
    }
    return render(request,"employee/create_employee.html",context)

def search_mail_employee(request):
    print('Entre al searcf_mail_employee')
    context = {}
    if request.method == 'POST':
        print('POST')
        email = request.POST.get('email', None)
        userprofile = Userprofile()

        userprofile = Userprofile.objects.get(email = email)
        print('id de user:')
        print(userprofile.id)
        
        request.session['email']=email
        print("no se encuentra mail de empleado")
        
    return render(request, 'employee/create_employee.html', context)

def create_employee(request):
    name = request.POST.get('name', None)
    lastname = request.POST.get('lastname', None)
    nroDocument = request.POST.get('nroDocument', None)
    documentType = request.POST.get('documentType', None)
    email = request.POST.get('email', None)
    password = request.POST.get('password', None)
    password2 = request.POST.get('password2', None)

    celphone = request.POST.get('celphone',None)
    phone = request.POST.get('phone',None)
    position_id = request.POST.get('position',None)
    position = Position.objects.get(pk=position_id)

    if password and password2 and password != password2:
        raise forms.ValidationError("Passwords don't match")
    else:
        if request.method == 'POST':
            userprofile=Userprofile.objects.create_user(email=email,
                                                        name=name,
                                                        lastname=lastname,
                                                        nroDocument=nroDocument,
                                                        documentType=documentType,
                                                        password=password,)
            userprofile.save()
            employee = Employee.objects.create(userprofile=userprofile,
                                                celphone=celphone,
                                                phone=phone,
                                                position=position,)
            employees = Employee.objects.all()
            context = {
                "employees" : employees,
            }
            return render(request,"employee/employee.html",context)
    context = {}
    return render(request, 'employee/create_employee.html', context)

def update_employee_form(request,pk):
    userprofile = Userprofile.objects.get(pk=pk)

    employee = Employee.objects.get(userprofile=userprofile)
    request.session['userprofile_id'] = userprofile.id
    request.session['employee_id'] = employee.id
    context = {
        "userprofile" : userprofile,
        "employee" : employee,
    }
    return render(request,"employee/update_employee.html",context)

def update_employee(request):
    
    email = request.POST.get('email',None)
    name = request.POST.get('name',None)
    lastname = request.POST.get('lastname',None)
    nroDocument = request.POST.get('nroDocument',None)
    documentType = request.POST.get('documentType',None)
    state =  request.POST.get('state',None)
    
    print('Nuevo estado: ')
    print(state)

    celphone = request.POST.get('celphone',None)
    phone = request.POST.get('phone',None)
    position = request.POST.get('position',None)

    employee_id = request.session.get("employee_id")
    employee = Employee.objects.get(id=employee_id)
    userprofile_id = request.session.get("userprofile_id")
    userprofile = Userprofile.objects.get(id=userprofile_id)

    userprofile.email=email
    userprofile.name=name
    userprofile.lastname=lastname
    userprofile.nroDocument=nroDocument
    userprofile.documentType=documentType

    if state == '1':
        userprofile.is_active=True
    else:
        if state == '0':
           userprofile.is_active=False

    userprofile.save()

    employee.userprofile = userprofile
    employee.celphone=celphone
    employee.phone=phone
    employee.position=position
    employee.save()

    employees = Employee.objects.all()
    context = {
        "employees" : employees,
    }
    return render(request,"employee/employee.html",context)


def delete_employee(request,pk):
    userprofile = Userprofile.objects.get(pk=pk)
    Employee.objects.get(userprofile=userprofile).delete()
    userprofile.delete()
    employees = Employee.objects.all()
    context = {
        "employees" : employees,
    }
    return render(request,"employee/employee.html",context)

def search_schedule(request):
    employees = Employee.objects.all()
    context = {
        "employees" : employees,
    }
    return render(request,"employee/search_schedule.html",context)

def schedule_employee(request,pk):
    employee = Employee.objects.get(pk=pk)
    schedules = Scheduleemployee.objects.all().filter(employee=employee)
    request.session['employee_id'] = employee.id
    context = {
        "employee" : employee,
        "schedules" : schedules,
    }
    return render(request,"employee/schedule_employee.html",context)

def create_schedule_form(request,pk):
    employee = Employee.objects.get(pk=pk)
    request.session['employee_id'] = employee.id
    context = {
        "employee" : employee,
    }
    return render(request,"employee/create_schedule.html",context)

def create_schedule(request):
    employee_id = request.session.get("employee_id")
    employee = Employee.objects.get(id=employee_id)
    day = request.POST.get('day', None)
    entryTime = request.POST.get('entryTime', None)
    departureTime = request.POST.get('departureTime', None)

    schedules = Scheduleemployee.objects.all().filter(employee=employee)

    repeat = False
    context = {}

    for s in schedules:
        if s.day == day:
            repeat = True
        else:
            repeat = False

    if repeat:
        messages.error(request,'Horario repetido, elija uno diferente.')        
    else:
        if request.method == 'POST':
            scheduleemployee = Scheduleemployee.objects.create(day=day,
                                                                entryTime=entryTime,
                                                                departureTime=departureTime,
                                                                employee=employee)
            schedules = Scheduleemployee.objects.all().filter(employee=employee)
        messages.success(request,'Horario guardado con éxito.')
    request.session['employee_id'] = employee.id
    context = {
        "employee" : employee,
        "pk" : employee_id,
    }
    return render(request, "employee/create_schedule.html" ,context)

def update_schedule_form(request,pk):
    schedule = Scheduleemployee.objects.get(pk=pk)
    employee = schedule.employee
    request.session['schedule_id'] = schedule.id
    request.session['employee_id'] = employee.id
    context = {
        "schedule" : schedule,
        "employee" : employee,
    }
    return render(request, "employee/update_schedule.html" ,context)
    
def update_schedule(request):
    schedule_id = request.session.get("schedule_id")
    schedule = Scheduleemployee.objects.get(pk=schedule_id)
    employee_id = request.session.get("employee_id")
    employee = Employee.objects.get(id=employee_id)
    day = request.POST.get('day', None)
    entryTime = request.POST.get('entryTime', None)
    departureTime = request.POST.get('departureTime', None)

    schedules = Scheduleemployee.objects.all().filter(employee=employee)

    repeat = False
    context = {}
    nextUrl = None

    for s in schedules:
        if s.day == day:
            repeat = True
        else:
            repeat = False

    if repeat:
        nextUrl = "employee/update_schedule.html"
        messages.error(request,'Horario repetido, elija uno diferente.')        
    else:
        if request.method == 'POST':
            schedule.day = day
            schedule.entryTime = entryTime
            schedule.departureTime = departureTime
            schedule.save()
            nextUrl = "employee/schedule_employee.html"
            """Vuelvo a llenar la lista de horarios porque ha sido actualizada"""
            schedules = Scheduleemployee.objects.all().filter(employee=employee)
    request.session['employee_id'] = employee.id
    context = {
        "schedule" : schedule,
        "employee" : employee,
        "pk" : employee_id,
        "schedules" : schedules,
    }
    return render(request, nextUrl ,context)