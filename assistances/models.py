from django.db import models
from employees.models import Employee

# Create your models here.

class Assistance(models.Model):
	date = models.DateTimeField(verbose_name='Fecha de asistencia',null=True)
	dayNumber = models.IntegerField(verbose_name='Número de día')
	day = models.CharField(max_length=100,verbose_name='Día')
	attended = models.BooleanField(default=False,verbose_name='¿Asistió?')
	checkInTime = models.TimeField(verbose_name='Hora de entrada',null=True) 
	departureTime = models.TimeField(verbose_name='Hora de salida',null=True) 
	delay = models.BooleanField(default=False,verbose_name='¿Tardanza?')
	minutesLate = models.IntegerField(verbose_name='Minutos de retraso',null=True)
	registrationDate = models.DateTimeField(verbose_name='Fecha y hora de registro',null=True)
	modifitacionDate = models.DateTimeField(verbose_name='Fecha y hora de modificación',null=True)
	employee = models.ForeignKey(Employee,verbose_name='Id de Empleado')

	def __str__(self):
		return '%s' % (self.employee.userprofile.name)

	class Meta:
		ordering = ('id',)