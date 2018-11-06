from django.urls import path
from . import views
app_name='patient'
urlpatterns = [
    path('<int:patient_id>/file/', views.file_list, name='file_list'),
    path('<int:patient_id>/file/download/', views.file_download, name='file_download'),
]