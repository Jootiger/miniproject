from django.urls import path, include 
from django.views.generic.base import TemplateView
from login import views
from login.views import *

app_name = 'login'

urlpatterns = [
    path('', views.index_dlg, name='index_dlg'),
    path('login', views.login_select, name='login_select'),
    path('login/hospital/', views.login_hospital, name='login_hospital'),
    path('login/patient/', views.login_patient, name='login_patient'),
    path('register', views.register_select, name='register_select'),
    path('register/hospital/', PatientCreateView.as_view(), name="register_hospital"),
    path('register/patient/', HospitalCreateView.as_view(), name="register_patient"),
]