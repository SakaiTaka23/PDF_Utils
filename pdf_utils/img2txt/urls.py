from django.urls import path

from . import views

app_name = 'img2txt'

urlpatterns = [
    path('showall/', views.showall, name='showall'),
    path('upload/', views.upload, name='upload'),
    path('show_uploaded/<str:task_id>',
         views.show_uploaded, name='show_uploaded'),
    path('download/zip/', views.download_zip, name='download_zip'),
]
