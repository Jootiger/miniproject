from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy


# Create your views here.

def index_dlg(request):
    context = {}
    return render(request, 'pages/index.html', context)

def login_select(request):
    context = {}
    return render(request, 'pages/login_select.html', context)

def login_hospital(request):
    context = {}
    return render(request, 'pages/login_hospital.html', context)

def login_patient(request):
    context = {}
    return render(request, 'pages/login_patient.html', context)

def register_select(request):
    context = {}
    return render(request, 'pages/register_select.html', context)

class PatientCreateView(CreateView):
    template_name = "pages/register_patient.html"
    form_class = UserCreationForm
    success_url = reverse_lazy("register_done")

class HospitalCreateView(CreateView):
    template_name = "pages/register_hospital.html"
    form_class = UserCreationForm
    success_url = reverse_lazy("register_done")

class UserCreateDone(TemplateView):
    template_name = "pages/register_done.html"