from django.urls import path
from . import views
app_name='patient'
urlpatterns = [
    path('', views.file_list_all, name='file_list_all'),
    path('file/', views.file_list_all, name='file_list'),
    path('file/download/', views.file_download, name='file_download'),
    path('<int:patient_pid>/file/', views.file_list, name='file_list'),
    path('<int:patient_pid>/file/download/', views.file_download, name='file_download'),
]