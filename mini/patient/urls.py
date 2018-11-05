from django.urls import path

from . import views

app_name='patient'

urlpatterns = [
    path('file/', views.file_list, name='file_list'),
    path('file/download/', views.file_download, name='file_download'),
]
