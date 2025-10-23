from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('learning-advisor/', views.learning_advisor, name='learning_advisor'),
    path('learning-advisor/<int:path_id>/', views.learning_path_detail, name='learning_path_detail'),
    path('generate/', views.generate, name='generate'),
    path('hackathons/', views.hackathons, name='hackathons'),
    path('it-profiles/', views.it_profiles, name='it_profiles'),
]
