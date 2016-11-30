from django.db import models
from userprofiles.models import Userprofile
from positions.models import Position

class Employee(models.Model):
	userprofile = models.OneToOneField(Userprofile, verbose_name='usuario')
	code = models.CharField(max_length=12,verbose_name='Código',null=True)
	celphone = models.IntegerField(verbose_name='Celular',null=True)
	phone = models.IntegerField(verbose_name='Teléfono',null=True)
	position = models.ForeignKey(Position, verbose_name='Cargo' )
	def __str__(self):
		return '%s' % (self.userprofile.name)

	class Meta:
			ordering = ('id',)

class Scheduleemployee(models.Model):
	day = models.CharField(max_length=100,verbose_name='Día')
	entryTime = models.TimeField(verbose_name='Hora de ingreso',null=True) 
	departureTime = models.TimeField(verbose_name='Hora de salida',null=True) 
	employee = models.ForeignKey(Employee,verbose_name='Empleado')

	def __str__(self):
		return '%s' % (self.employee.userprofile.name)

	class Meta:
			ordering = ('id',)