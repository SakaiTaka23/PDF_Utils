from django.urls import path

from . import views

app_name = 'img2txt'

urlpatterns = [
    path('showall/', views.showall, name='showall'),
    path('upload/', views.upload, name='upload'),
]
