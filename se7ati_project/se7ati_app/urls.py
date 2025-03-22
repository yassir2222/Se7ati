from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/doctor/', views.patient_register, name='register'),
    path('register/patient/', views.doctor_register, name='register'),

    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('pharmacy/', views.chercher_pharmacies_view, name='chercher_pharmacies_view'),
    path('file/', views.serve_csv, name='serve_csv'),
    path('get-quartiers/', views.get_quartiers, name='get_quartiers'),  # AJAX endpoint for quartiers
    path('chat/', views.chat_home, name='chat_home'),
    path('chat/<int:user_id>/', views.chat_with_user, name='chat_with_user'),
]
