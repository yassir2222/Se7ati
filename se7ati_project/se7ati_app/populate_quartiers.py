from se7ati_app.models import Ville, Quartier,MesureGlycemie

try:
    casablanca = Ville.objects.get(nom="Casablanca")
except Ville.DoesNotExist:
    casablanca = Ville.objects.create(nom="Casablanca")
    print("La ville de Casablanca a été créée.")

quartiers_data = [
    "Aïn Chock",
    "Aïn Sebaâ",
    "Al Azhar Panorama",
    "Al Fida",
    "Annasi",
    "Beauséjour",
    "Belvédère",
    "Bourgogne",
    "Centre Ville",
    "Derb Ghallef",
    "Hay Hassani",
    "Hay Mohammadi",
    "Lissasfa",
    "Maarif",
    "Oulfa",
    "Sidi Bernoussi",
    "Sidi Maarouf",
    "Sidi Moumen",
    "Sidi Othmane",
]

quartiers_a_creer = []
for nom_quartier in quartiers_data:
     if not Quartier.objects.filter(nom_quartier=nom_quartier, ville=casablanca).exists():
          quartiers_a_creer.append(Quartier(nom_quartier=nom_quartier, ville=casablanca))

if quartiers_a_creer: #Verifie qu'il y a des éléments à créer
    Quartier.objects.bulk_create(quartiers_a_creer)
    print(f"{len(quartiers_a_creer)} quartiers ont été ajoutés à Casablanca.")
else:
    print("Tous les quartiers existent déjà pour Casablanca.")

print("Opération terminée.")


from se7ati_app.models import Ville, Quartier  # Remplacez mon_app par le nom de votre application

# 1. Récupérer ou créer la ville de Marrakech
try:
    marrakech = Ville.objects.get(nom="Marrakech")
except Ville.DoesNotExist:
    marrakech = Ville.objects.create(nom="Marrakech")
    print("La ville de Marrakech a été créée.")

# 2. Liste des quartiers à ajouter
quartiers = [
    "MEDINA",
    "GRAND GUELIZ",
    "DAOUDIAT",
    "HAY  CHARAF",
    "HAY DAR  ESAADA",
    "HAY AL IZDIHAR",
    "HAY AL FADL",
    "SIDI GHANEM AZZOUZIA",
    "TARGA",
    "HAY HASSANI",
    "AÏN ITTI",
    "NAKHIL SUD",
    "SIDI YOUSSEF",
    "LAMHAMID",
]


quartiers_a_creer = []
for nom_quartier in quartiers:
    if not Quartier.objects.filter(nom_quartier=nom_quartier, ville=marrakech).exists():
        quartiers_a_creer.append(Quartier(nom_quartier=nom_quartier, ville=marrakech))

if quartiers_a_creer:
    Quartier.objects.bulk_create(quartiers_a_creer)
    print(f"{len(quartiers_a_creer)} quartiers ont été ajoutés à Marrakech.")
else:
    print("Tous les quartiers existent déjà pour Marrakech.")

print("Opération terminée.")




from datetime import datetime
from se7ati_app.models import MesureGlycemie
from django.contrib.auth.models import User

# Exemple de données pour les mesures de glycémie (10 valeurs en mg/dL sur la semaine dernière)
donnees = [
    {'valeur': 102, 'date_mesure': datetime(2025, 3, 19, 8, 0)},  # 19 mars à 08:00
    {'valeur': 203, 'date_mesure': datetime(2025, 3, 19, 14, 30)}, # 19 mars à 14:30
    {'valeur': 150, 'date_mesure': datetime(2025, 3, 20, 9, 0)},  # 20 mars à 09:00
    {'valeur': 170, 'date_mesure': datetime(2025, 3, 20, 16, 15)}, # 20 mars à 16:15
    {'valeur': 130, 'date_mesure': datetime(2025, 3, 21, 7, 45)},  # 21 mars à 07:45
    {'valeur': 185, 'date_mesure': datetime(2025, 3, 21, 13, 0)},  # 21 mars à 13:00
    {'valeur': 115, 'date_mesure': datetime(2025, 3, 22, 10, 30)}, # 22 mars à 10:30
    {'valeur': 145, 'date_mesure': datetime(2025, 3, 22, 19, 45)}, # 22 mars à 19:45
    {'valeur': 120, 'date_mesure': datetime(2025, 3, 23, 8, 15)},  # 23 mars à 08:15
    {'valeur': 160, 'date_mesure': datetime(2025, 3, 23, 18, 0)},  # 23 mars à 18:00
]
utilisateur = User.objects.first() 

# Insérer ces données dans la base de données
for donnee in donnees:
    MesureGlycemie.objects.create(
        user= utilisateur,  # Assure-toi de spécifier un utilisateur valide
        valeur=donnee['valeur'],
        date_mesure=donnee['date_mesure']
    )
