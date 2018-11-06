from django.urls import path

from hospital import views

app_name='hospital'

urlpatterns = [
    path('file/', views.file_list, name='file_list'),
    path('file/download/', views.file_download, name='file_download'),
    path('file/add/', views.file_edit, name='file_add'),
]