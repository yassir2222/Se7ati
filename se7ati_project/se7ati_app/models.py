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