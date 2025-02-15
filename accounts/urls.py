from . import views
from django.urls import path
from django.contrib.auth import views as auth_views 

urlpatterns = [
    path('register/', views.register, name= 'register'),
    path('login/', views.login, name= 'login'),
    path('logout/', views.logout, name= 'logout'),
    path('page/', views.page, name= 'page'),
    path('settings/', views.settings, name= 'settings'),
    path('update_pix/', views.update_pix, name='update_pix'),

    
    # because of the email activation , i have to create a url for the activation link
    path('activate/<uidb64>/<token>/', views.activate, name= 'activate'),
    #path('edit-profile/<str:pk>/', views.edit_profile, name='edit_profile'),
]