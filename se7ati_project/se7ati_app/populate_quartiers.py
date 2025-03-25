from se7ati_app.models import Ville, Quartier

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