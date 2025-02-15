from . import views
from django.urls import path

urlpatterns = [
    path('', views.Home, name= 'home'),
    path('save-location/', views.save_location, name='save_location'),
]


