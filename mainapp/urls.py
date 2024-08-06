from . import views
from django.urls import path

app_name='mainapp'
urlpatterns = [
    
    path('',views.Home,name='Home'),

]