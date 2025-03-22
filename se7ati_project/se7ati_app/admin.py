from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Ville , Quartier

@admin.register(Ville)
class VilleAdmin(admin.ModelAdmin):
    list_display = ('id', 'nom')  
    search_fields = ('nom',)
    
    
@admin.register(Quartier)
class QuartierAdmin(admin.ModelAdmin):
    list_display = ('id', 'nom_quartier', 'ville')
    search_fields = ('nom_quartier', 'ville__nom')
    list_filter = ('ville',)