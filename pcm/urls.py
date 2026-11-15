
from django.urls import path
from . import views

app_name = 'pcm'

urlpatterns = [
    path('', views.beranda, name='beranda'),
]
