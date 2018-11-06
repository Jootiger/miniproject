from django.shortcuts import render,get_object_or_404,get_list_or_404,redirect
from django.http import HttpResponse
from patient.models import Info
from patient.forms import FileForm
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

# def file_download(request, patient_id):
#     context={}
#     if patient_id:
#         files = get_object_or_404(Info,pk=patient_id)
#         context['files']=files
#     else:
#         return render(request, 'patient/file_list.html',context)
#     return HttpResponse('파일 다운로드')

def file_edit(request, file_id=None):
    if file_id:
        files=get_object_or_404(Info,pk=file_id)
    else:
        files=Info()
    
    if request.method == 'POST':
        form=FileForm(request.POST,instance=files)
        if form.is_valid():
            files=form.save(commit=False)
            files.save()
            return redirect('patient:file_list')
    else:
        form=FileForm(instance=files)
        return render(request, 'patient/file_edit.html',dict(form=form, file_id=file_id))