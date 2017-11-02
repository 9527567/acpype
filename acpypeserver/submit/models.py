from django.db import models
from django.forms import ModelForm

my_choices1 = [('bcc', "bcc (default)"), ('gasteiger', "gasteiger"), ('user', "user")]
my_choices2 = [('gaff', "GAFF (default)"), ('amber', "AMBER")]

class Submition(models.Model):
	molecule_file = models.FileField(upload_to='',null=True)
	charge_method = models.CharField(max_length=20,choices=my_choices1, blank=False, default='bcc')
	net_charge = models.IntegerField(default=0, null=True)
	multiplicity = models.PositiveIntegerField(default=1, null=True)
	atom_type = models.CharField(max_length=20,choices=my_choices2, blank=False, default='gaff')
	
		