from django.contrib import admin
from hospital.models import *
# Register your models here.
class InfoAdmin(admin.ModelAdmin):
    list_display = ('name', 'modifyDate')
    list_filter = ('modifyDate',)
    search_fileds = ('name', 'content')
    perpopulated_fields = {'pid': ('name',)}

admin.site.register(Info, InfoAdmin)
