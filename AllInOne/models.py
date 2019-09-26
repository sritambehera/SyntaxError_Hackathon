from django.db import models


class Paper(models.Model):
	file =models.FileField(upload_to ='media')

# Create your models here.
