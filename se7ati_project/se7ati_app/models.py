from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser): 
    USER_TYPE_CHOICES = (
        ('patient', 'Patient'),
        ('doctor', 'Doctor'),
    )
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES, default='patient')
    stream_chat_token = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.username

class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    medical_history = models.TextField(blank=True, null=True)
    def __str__(self):
        return self.user.username

class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    specialization = models.CharField(max_length=255)
    license_number = models.CharField(max_length=50)
    def __str__(self):
        return "DR "+self.user.username
    
class Ville(models.Model):
    nom = models.CharField(max_length=100, verbose_name="Nom de la ville")
    def __str__(self):
        return self.nom
    
    
class Quartier(models.Model):
    nom_quartier = models.CharField(max_length=100, verbose_name="Nom du quartier")
    ville = models.ForeignKey(Ville, on_delete=models.CASCADE, related_name="quartiers", verbose_name="Ville")
    def __str__(self):
        return f"{self.nom_quartier} ({self.ville.nom})"