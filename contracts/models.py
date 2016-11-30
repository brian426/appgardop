from django.db import models

class Contract(models.Model):
	STATES_CHOICES = (
		('ENA', 'Activo'),
		('DIS', 'Inactivo'),
	)
	namecontract = models.CharField(max_length=255,verbose_name='Contrato')
	description = models.CharField(max_length=255,verbose_name='Descripción de Contrato')
	state = models.CharField(max_length=3,verbose_name='Estado',choices=STATES_CHOICES)

	def __str__(self):
		return '%s' % (str(self.namecontract))

	class Meta:
		ordering = ('id',)
