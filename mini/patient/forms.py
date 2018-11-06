# /cms/templates/forms.py
from django.forms import ModelForm
from patient.models import Info

class FileForm(ModelForm):
    class Meta:
        model = Info
        fields = ('name', 'pid', 'description', 'content', 'owner',)
