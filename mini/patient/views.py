from django.shortcuts import render,get_object_or_404,get_list_or_404
from django.http import HttpResponse
from patient.models import Info

# Create your views here.	# Create your views here.
def file_list_all(request):
    files=Info.objects.order_by('pid')
    context={}
    context['files']=files

    return render(request,'patient/file_list.html',context)

def file_download(request):
    return HttpResponse('파일 다운로드')
    
def file_list(request,patient_pid):
    # files=get_object_or_404(Info)
    # files=Info.objects.get(pk=patient_pid)
    # files=Info.objects.order_by('id')
    # files=Info.objects.all()
    files=get_list_or_404(Info,pid=patient_pid)
    context={}
    context['files']=files

    return render(request,'patient/file_list.html',context)