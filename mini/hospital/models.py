from django.db import models

# Create your models here.
class File(models.Model):
    file_name=models.CharField('파일명',max_length=100)
    file_file=models.FileField()