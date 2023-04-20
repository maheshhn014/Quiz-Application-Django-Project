from django.urls import path
from auth_app import views

urlpatterns = [
    
    path('registration/', views.authregistration, name = 'registration'),
    path('login', views.authlogin, name = 'login'),
    path('logout/', views.authlogout, name = 'logout'),
    
]
