from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils.text import slugify

# Create your models here.
class Info(models.Model):
    name = models.CharField('NAME', max_length=50)
    pid = models.IntegerField('Patient ID', unique=True, blank=True, null=True)
    description = models.CharField('DESCRIPTION', max_length=100, blank=True, null=True)
    content = models.TextField('CONTENT')
    createDate = models.DateTimeField('Create Date', auto_now_add=True)
    modifyDate = models.DateTimeField('Modify Date', auto_now=True)
    owner = models.ForeignKey(User, null=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'info'
        verbose_name_plural = 'infos'
        db_table = 'hospital_patients'
        ordering = ('-modifyDate',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('hospital:info_detail', args=(self.slug,))

    def get_preivous_info(self):
        return self.get_previous_by_modifyDate()

    def get_next_info(self):
        return self.get_next_by_modifyDate()

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name, allow_unicode=True)
        super(Info, self).save(*args, **kwargs)
