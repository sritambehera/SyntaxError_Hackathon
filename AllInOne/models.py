from django.db import models
from django.forms import ModelForm
from django.conf import settings




class Paper(models.Model):
	file =models.FileField(upload_to ='documents/')
	branch = models.CharField(max_length = 50)
	semester = models.IntegerField( choices =  list(zip(range(1,7), range(1,7))), unique = True)
