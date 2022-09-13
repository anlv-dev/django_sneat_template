from django.urls import path
from . import views

app_name='testtemplates'
urlpatterns = [
    path('', views.index, name ='index'),   
]

