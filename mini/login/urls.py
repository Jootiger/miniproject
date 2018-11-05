from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index_dlg, name='index_dlg'),
    url(r'^login', views.login_dlg, name='login_dlg'),    
]