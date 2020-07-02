from django.urls import path
from . import views

app_name = 'weatherapp'
urlpatterns = [
    path('', views.index, name='index'),
    path('delete/<city_name>', views.delete, name='delete'),
]
