from django.shortcuts import render

# Create your views here.

def index_dlg(request):
    context = {}
    return render(request, 'pages/index.html', context)

def login_dlg(request):
    context = {}
    return render(request, 'pages/login.html', context)
    
