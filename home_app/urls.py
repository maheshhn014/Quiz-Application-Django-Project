from django.urls import path
from home_app import views

urlpatterns = [
    
    path('', views.home, name = 'home'),
    path('about/', views.about, name = 'about'),
    path('contact/', views.contact, name = 'contact'),
  
]
