from django.urls import path
from . import views

urlpatterns = [
    path('', views.ar_cube, name='ar_cube'),
]