from django.conf.urls import url
from django.urls import path

from hospital.views import *

app_name = 'hospital'

urlpatterns = [
    #hospital/
    path('', InfoLV.as_view(), name='index'),
    #hospital/patient
    path('patient/', InfoLV.as_view(), name='patient_list'),
    #hospital/patient/detail
    path('patient/<int:pid>', InfoDV.as_view(), name='patient_detail'),
    #/search/
    path('search/', SearchFormView.as_view(), name='search'),
    path('append/', InfoCreateView.as_view(), name = 'append'),
]
