from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Info
# Create your views here.	# Create your views here.
def file_list(request,patient_id):
    files=Info.objects.get(pk=patient_id).order_by('id')
    context={}
    context['files']=files

    return render(request,'patient/file_list.html',context)

def file_download(request, patient_id):
    context={}
    if patient_id:
        files = get_object_or_404(Info,pk=patient_id)
        context['files']=files
    else:
        return render(request, 'patient/file_list.html',context)
    return HttpResponse('파일 다운로드')