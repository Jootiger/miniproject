from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Info(models.Model):
    name = models.CharField('NAME', max_length=50)
    pid = models.IntegerField('Patient ID', unique=True, blank=True, null=True)
    description = models.CharField('DESCRIPTION', max_length=100, blank=True, null=True)
    content = models.TextField('CONTENT')
    createDate = models.DateTimeField('Create Date', auto_now_add=True)
    modifyDate = models.DateTimeField('Modify Date', auto_now=True)
    owner = models.ForeignKey(User, null=True, on_delete=models.CASCADE, related_name='%(class)s_patient_models')
