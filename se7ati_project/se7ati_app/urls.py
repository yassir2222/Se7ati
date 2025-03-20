from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/doctor/', views.patient_register, name='register'),
    path('register/patient/', views.doctor_register, name='register'),

    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]
