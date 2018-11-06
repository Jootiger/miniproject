from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy


class HomeView(TemplateView):
    template_name = "base.html"

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

