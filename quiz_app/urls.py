from django.urls import path
from quiz_app import views

app_name = "quiz_app"

urlpatterns = [
    
    path('profile/', views.profile, name='profile'),
    path('quiz_questions/<int:category_id>/', views.quiz_questions, name='quiz_questions'),
    path('leader/', views.leader, name='leader'),
    
]
