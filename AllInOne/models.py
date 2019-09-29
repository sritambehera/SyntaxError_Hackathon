from django.db import models
from django.forms import ModelForm
from django.conf import settings




class Material(models.Model):
	material =models.FileField(upload_to ='documents/')


class Branch(models.Model):
	branch = models.CharField(max_length = 50)


class Semester(models.Model):
	semester = models.IntegerField( choices =  list(zip(range(1,11), range(1,11))), unique = True)


