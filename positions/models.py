from django.db import models

from django.db import models
from contracts.models import Contract

class Position(models.Model):
	STATES_CHOICES = (
		('ENA', 'Activo'),
		('DIS', 'Inactivo'),
	)
	contract = models.ForeignKey(Contract, verbose_name='Contrato' )
	code = models.CharField(max_length=10,verbose_name='Código')
	nameposition = models.CharField(max_length=255,verbose_name='Cargo')
	description = models.CharField(max_length=255,verbose_name='Descripción de Cargo')
	state = models.CharField(max_length=3,verbose_name='Estado',choices=STATES_CHOICES)
	registrationdate = models.DateTimeField(auto_now=False, auto_now_add=False, verbose_name='Fecha y hora de registro',blank=True)
	modificationdate = models.DateTimeField(auto_now=False, auto_now_add=False, verbose_name='Fecha y hora de modificación',blank=True)

	def __str__(self):
		return '%s' % (str(self.nameposition))

	class Meta:
		ordering = ('id',)
