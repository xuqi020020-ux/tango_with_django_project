from django.urls import path
from . import views

app_name = 'rango'

urlpatterns = [
    path('about/', views.about, name='about'),
]
