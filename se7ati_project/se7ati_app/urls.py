from django.urls import path
from . import views



urlpatterns = [
    path('', views.home, name='home'),
    path('doctor', views.Dr_home, name='Dr_home'),
    path('register/doctor/', views.doctor_register, name='doctor_register'),
    path('register/patient/', views.patient_register, name='patient_register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('pharmacy/', views.chercher_pharmacies_view, name='chercher_pharmacies_view'),
    path('get-quartiers/', views.get_quartiers, name='get_quartiers'),
    path('edit_profile/', views.edit_profile, name='edit_profile'), 
    path('edit_profile/<int:user_id>/update', views.edit_profile_update, name='edit_profile_update'),  # AJAX endpoint for quartiers
    path('chat/', views.chat_home, name='chat_home'),
    path('chat/<int:user_id>/', views.chat_with_user, name='chat_with_user'),
    path('diabetes_predicton/', views.diabetes_predicton, name='diabetes_predicton'),
    path('chat_bot/', views.chat_bot, name='chat_bot'),
    path('glucoseLevel/', views.glucose_view, name='glucoseLevel'),
    path('glucoseLevel/glucose_last_week', views.glucose_last_week, name='glucose_last_week'),
    path('glucoseLevel/add/', views.add_glucose, name='add_glucose'),
    path('glucose_last_30day/', views.glucose_last_30day, name='glucose_last_30day'),
    path('glucose_last_90day/', views.glucose_last_90day, name='glucose_last_90day'),
    path('glucoseLevel/glucose_Yesterday', views.glucose_Yesterday, name='glucose_Yesterday'),
    path('glucose_Today/glucose_Today', views.glucose_Today, name='glucose_Today'),
    path('test', views.debug_redirect_uri, name='debug_redirect_uri'),
    path('glucoseLevel/get-analysis/', views.get_data, name='get_analysis'),
    path('searchDoctor/', views.search_doctor, name='search_doctor'),
 
    path('chat_doctor/', views.chat_doctor, name='chat_doctor'),
    path('chat_patient/',views.room,name = "room"),
    path('chat_patient/send/', views.send_message , name = "send_message"),
    path('getMessages/<str:room>/', views.get_maessage , name = "get_message")
 
]