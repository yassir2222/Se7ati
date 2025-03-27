from django.db import models
from datetime import datetime

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
    date_naissance = models.DateField(null=True, blank=True, verbose_name="Date de naissance")
    genre = models.CharField(
        max_length=30,
        verbose_name="Genre",
        choices=[
            ('homme', 'Homme'),
            ('femme', 'Femme'),
            ('non-specifie', 'Non spécifié'),  # Ou "Non spécifié"
        ],
    )
    taille = models.FloatField(null=True, blank=True, verbose_name="Taille (en cm)")
    poids = models.FloatField(null=True, blank=True, verbose_name="Poids (en kg)")
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
    
    
class ChatMessage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    response = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Chat by {self.user.username} at {self.created_at}" 
    
    
class MesureGlycemie (models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    valeur = models.FloatField()
    date_mesure  = models.DateTimeField(default=datetime.now)
    
    def __str__(self):  
        return f"Suivi Glycémie : {self.valeur} mmol/L le {self.date_mesure.strftime('%d-%m-%Y %H:%M')}"  