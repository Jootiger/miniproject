from django import forms

class InfoSearchForm(forms.Form):
    search_word = forms.CharField(label='Search Word')

class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()
