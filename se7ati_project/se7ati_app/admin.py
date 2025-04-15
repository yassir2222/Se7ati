from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

<<<<<<< HEAD
from .models import Ville, Quartier, Patient, User, Doctor,ChatMessage
=======
from .models import Ville, Quartier, Patient, User, Doctor,ChatMessage,MesureGlycemie,Message,Room
>>>>>>> df65bc42646209401f820253ff6c76c734627aed

# Personnaliser l'administration des utilisateurs
@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'user_type', 'is_staff')
    list_filter = ('user_type', 'is_staff', 'is_superuser', 'is_active')
    fieldsets = BaseUserAdmin.fieldsets + (
        ('User Type', {'fields': ('user_type',)}),
    )
    add_fieldsets = BaseUserAdmin.add_fieldsets + (
        ('User Type', {'fields': ('user_type',)}),
    )
    search_fields = ('username', 'email', 'first_name', 'last_name')

@admin.register(Ville)
class VilleAdmin(admin.ModelAdmin):
    list_display = ('id', 'nom')  
    search_fields = ('nom',)
    
@admin.register(Quartier)
class QuartierAdmin(admin.ModelAdmin):
    list_display = ('id', 'nom_quartier', 'ville')
    search_fields = ('nom_quartier', 'ville__nom')
    list_filter = ('ville',)
    
@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('user', 'date_naissance', 'genre', 'taille', 'poids')
    search_fields = ('user__username', 'user__email')

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('user', 'specialization', 'license_number')
    search_fields = ('user__username', 'user__email', 'specialization')
<<<<<<< HEAD
    list_filter = ('specialization',)
=======
>>>>>>> df65bc42646209401f820253ff6c76c734627aed
    
@admin.register(ChatMessage)
class ChatMessageAdmin(admin.ModelAdmin):
    list_display = ('user', 'message', 'response', 'created_at')
    search_fields = ('user__username', 'message', 'response')  
<<<<<<< HEAD
    list_filter = ('created_at',)  
    ordering = ('created_at',)   


=======
    ordering = ('created_at',)   

@admin.register(MesureGlycemie)
class MesureGlycemieAdmin(admin.ModelAdmin):
    list_display = ('user', 'valeur' ,'date_mesure')
    search_fields = ('user',)  
    ordering = ('date_mesure',)

admin.site.register(Message)  
admin.site.register(Room)   
      
>>>>>>> df65bc42646209401f820253ff6c76c734627aed
