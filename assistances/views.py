from django.shortcuts import render
from employees.models import Employee
from employees.models import Scheduleemployee
from assistances.models import Assistance
import datetime, locale


# Create your views here.
def redirect_assistance_taking(request):
	actionMsg = ''
	finded = 0
	request.session['actionMsg'] = actionMsg
	request.session['finded'] = finded
	return render(request,"assistance/assistance-taking.html")

def validate_code_employee(request):
	actionMsg = ''
	finded = 0
	context = {}
	if request.method == 'POST':
		code = request.POST.get('code', None)
		employee = Employee()
		try:
			employee = Employee.objects.get(code=code)

			locale.setlocale(locale.LC_ALL, 'Spanish_Spain.1252')
			now = datetime.datetime.now()
			dayName = now.strftime("%A")
			dayNumber = now.day
			
			assistance = Assistance.objects.create(date=now,
									dayNumber=dayNumber,
									day= dayName,
									attended=True,
									checkInTime=now,
									registrationDate=now,
									modifitacionDate=now,
									employee=employee)

			actionMsg = 'Bienvenido ' + employee.userprofile.name
			finded = 1
		except Employee.DoesNotExist:
			actionMsg = 'Usuario no encontrado'
			finded = 2

		print(actionMsg)
		print(finded)
		request.session['finded']=finded
		request.session['actionMsg']=actionMsg
	return render(request,"assistance/assistance-taking.html", context)

def search_assistances(request):
    employees = Employee.objects.all()
    context = {
        "employees" : employees,
    }
    return render(request,"assistance/search_assistances.html",context)

def employee_assistances(request,pk):
    employee = Employee.objects.get(id=pk)
    context = {
        "employee" : employee,
    }
    return render(request,"assistance/employee_assistances.html",context)
