from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse

from .models import File

# Create your views here.
def file_list(request):
    files=File.objects.all().order_by('id')

    context={}
    context['files']=files
    
    return render(request,'patient/file_list.html',context)

def file_download(request, file_id=None):
    if file_id:
        file = get_object_or_404(File,pk=file_id)
    else:
        return render(request, 'patient/file_list.html',context)

    return HttpResponse('파일 다운로드')

def file_edit(request):
    if file_id:
        file = get_object_or_404(File,pk=file_id)
    else:
        return render(request, 'hospital/file_list.html',context)
    return HttpResponse('파일 추가/수정')