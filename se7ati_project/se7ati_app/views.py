from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .forms import PatientSignUpForm , DoctorSignUpForm, LoginForm
from .models import Patient, Doctor, User ,Ville,Quartier
from django.http import HttpResponse, JsonResponse
from django.http import HttpResponse
from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST


import csv
import os
import re
from django.conf import settings
from .stream_chat_service import StreamChatService

def home(request):
    return render(request,'index.html')

def patient_register(request):
    if request.method == 'POST':
        form = PatientSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('login') 
    else:
        form = PatientSignUpForm()
    return render(request, 'registration/register.html', {'form': form})


def doctor_register(request):
    if request.method == 'POST':
        form = DoctorSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('login')  
        form = DoctorSignUpForm()
    return render(request, 'registration/register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if user.is_patient:
                return redirect('login')
            else:
                return redirect('login')
        else:
            print(form.errors)
    else:
        form = LoginForm()
    return render(request, 'registration/login.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                if user.user_type == 'patient':
                    return redirect('home')
                elif user.user_type == 'doctor':
                    return redirect('home')
                else:
                    return redirect('home')  # Fallback
        else:
            return render(request, 'registration/login.html', {'form': form})
    else:
        form = LoginForm()
    return render(request, 'registration/login.html', {'form': form})

def logout_view(request):
   # logout(request)
    return redirect('login') 


def chercher_pharmacies_view(request):
    return render(request, 'tools/pharmacies.html')

def get_quartiers(request):
    city_id = request.GET.get('city_id')
    if city_id:
        quartiers = Quartier.objects.filter(ville=Ville.objects.get(nom=city_id).id).values('id', 'nom_quartier')
        return JsonResponse(list(quartiers), safe=False)
    return JsonResponse([], safe=False)

data_pharmacie = {'name':'', 'address':'', 'district':'', 'phone':'','localisation':'', 'duty':''}  
def chercher_pharmacies_view(request):
    selected_city = request.POST.get('city', '')
    selected_district = request.POST.get('district', '')
    selected_duty = request.POST.get('duty_type', '')
    print(selected_city)
    print(selected_district)
    print(selected_duty)
    
    urlPart1 = ''
    urlPart2 = ''
    urlPart3 = ''
    Pharmacie_name = ''
    #construir l'url
    if (selected_city == 'Marrakech'):
        urlPart1 = 'https://www.syndicat-pharmaciens-marrakech.com/'
        if(selected_duty == 'jour'):
            urlPart2 = 'pharmacies-de-garde-marrakech/'
        else:
            urlPart2 = 'pharmacies-de-garde-marrakech-nuit/'    
        urlPart3 = convert_string(selected_district)     
    else:
        urlPart1 = 'https://www.pharmacies-garde-casablanca.com/pharmacies-garde-casablanca/' 
        urlPart2 = "quartier-"+convert_string(selected_district)
        if(selected_duty == 'jour'):
            urlPart3 = '/garde-jour'
        else:
            urlPart3 = '/garde-nuit' 
          
    url = urlPart1+urlPart2+urlPart3        
    
    response = requests.get(url)
    
    pharmacies_data = [] 
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text,'html.parser')
        articles = soup.find_all('article',class_='sec')
        global data_pharmacie
        for article in articles:
            Pharmacie_name_orig = format_pharmacy_name(article.get_text()) 
            Pharmacie_name = remove_after_garde(Pharmacie_name_orig)
           # print(Pharmacie_name)
            if (selected_city == 'Marrakech'):
                url = urlPart1+urlPart2+"pharmacie/"+Pharmacie_name
            else:
                url = urlPart1+urlPart2+"/"+Pharmacie_name+urlPart3
            response = requests.get(url)
            print(url)
            soup = BeautifulSoup(response.text,'html.parser')
            pharmacies = soup.find_all('li')
            localisation = soup.find_all('a',class_='direction')
            localisation = localisation[0].get('href')
            data_pharmacie['localisation'] = localisation
            for pharmacy in pharmacies:
                span_elements = pharmacy.find_all('span', class_='material-symbols-rounded')
                
                if span_elements:
                    pharmacy_text = pharmacy.get_text()
                    line = pharmacy_text.strip()
                    data_pharmacie['name'] = Pharmacie_name
                    print( Pharmacie_name_orig)
                    if line.startswith('pin_drop'):
                        data_pharmacie['address'] = line.replace('pin_drop', '').strip()
                    if line.startswith('flag'):
                        data_pharmacie['district'] = line.replace('flag', '').replace('Quartier :', '').strip()
                    if line.startswith('call'):
                        data_pharmacie['phone'] = line.replace('call', '').strip()
                    if(selected_duty == 'jour'):
                        data_pharmacie['duty'] = "Garde du Jour De 09h A 22h sans Interruption"
                    elif (selected_duty == 'nuit'):
                        data_pharmacie['duty'] = "Garde de Nuit De 22h A 09h sans Interruption"                        
                    
            
            print("####################################################")
            pharmacies_data.append(data_pharmacie.copy())
        
 
        csv_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'static', 'pharmacies_data.csv')
        save_to_csv(pharmacies_data, csv_path)
         
        
    else:
        print("ERREUR !! ")
        
    villes = Ville.objects.all().order_by('nom')    

    return render(request, 'tools/pharmacies.html', {'pharmacies': pharmacies_data, 'villes':villes})
   

def parse_pharmacy_data(text):
   
   
    lines = text.strip().split('\n')
    print(len(lines))
    lists = []
    name = ''
    address = ''
    district = ''
    phone = ''
    
    name = lines[0].replace('person', '').strip()
    address = lines[0].replace('pin_drop', '').strip()
    district = lines[0].replace('flag', '').replace('Quartier :', '').strip()
    phone = lines[0].replace('call', '').strip()
    data = {"name":name, "address": address, "district":district, "phone":phone}
    lists.append(data)

    return data

def remove_after_garde(input_string):
    garde_index = input_string.find('garde')
    
    if garde_index != -1:
        return input_string[:garde_index].strip()

    return input_string  

def save_to_csv(data, filepath):
   
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    
    
    fieldnames = ['name', 'address', 'district', 'phone','localisation','duty']
    
    with open(filepath, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for row in data:
            writer.writerow(row)
    
    print(f"Data saved to {filepath}")

def format_pharmacy_name(text):
    first_line = text.strip().split('\n')[0]
    text_with_hyphens = first_line.replace('. ', '-')
    text_with_hyphens = text_with_hyphens.replace(' ', '-')
    return text_with_hyphens.lower()

def convert_string(input_string):
    # Remplacer les caractères spéciaux par leur équivalent sans accent
    input_string = re.sub(r'[ÀÁÂÃÄÅ]', 'A', input_string)
    input_string = re.sub(r'[àáâãäå]', 'a', input_string)
    input_string = re.sub(r'[ÈÉÊË]', 'E', input_string)
    input_string = re.sub(r'[èéêë]', 'e', input_string)
    input_string = re.sub(r'[ÌÍÎÏ]', 'I', input_string)
    input_string = re.sub(r'[ìíîï]', 'i', input_string)
    input_string = re.sub(r'[ÒÓÔÕÖ]', 'O', input_string)
    input_string = re.sub(r'[òóôõö]', 'o', input_string)
    input_string = re.sub(r'[ÙÚÛÜ]', 'U', input_string)
    input_string = re.sub(r'[ùúûü]', 'u', input_string)
    input_string = re.sub(r'[Ç]', 'C', input_string)
    input_string = re.sub(r'[ç]', 'c', input_string)
    input_string = re.sub(r'[ŸÝ]', 'Y', input_string)
    input_string = re.sub(r'[ÿý]', 'y', input_string)
    
    # Remplacer les espaces et caractères spéciaux par des tirets
    input_string = re.sub(r'\s+', '-', input_string)
    
    # Convertir en minuscules
    input_string = input_string.lower()
    result_string = input_string
    
    return result_string

def about(request):
    return HttpResponse('About page')

def serve_csv(request):
    file_path = os.path.join('F:\Projet_Se7ati\se7ati_project\se7ati_app\static\Quartier_ville.csv')
    with open(file_path, 'r', encoding='utf-8') as file:
        data = file.read()
    response = HttpResponse(data, content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="Quartier_ville.csv"'
    return response

@login_required
def chat_home(request):
    """View for the main chat page"""
    # Get all users except the current user
    if request.user.user_type == 'doctor':
        # Doctors can see all patients and other doctors
        users = User.objects.exclude(id=request.user.id)
    else:
        # Patients can see all doctors and other patients
        users = User.objects.exclude(id=request.user.id)
    
    # Generate Stream Chat token if not already generated
    if not request.user.stream_chat_token:
        service = StreamChatService()
        token = service.generate_token(request.user.id)
        request.user.stream_chat_token = token
        request.user.save()
        
        # Upsert user to Stream Chat
        service.upsert_user(request.user)
    
    context = {
        'users': users,
        'stream_api_key': settings.STREAM_API_KEY,
        'user_token': request.user.stream_chat_token,
        'user_id': str(request.user.id)
    }
    
    return render(request, 'chat/chat_home.html', context)

@login_required
def chat_with_user(request, user_id):
    """View for chatting with a specific user"""
    try:
        other_user = User.objects.get(id=user_id)
    except User.DoesNotExist:
        return redirect('chat_home')
    
    # Generate Stream Chat token if not already generated
    if not request.user.stream_chat_token:
        service = StreamChatService()
        token = service.generate_token(request.user.id)
        request.user.stream_chat_token = token
        request.user.save()
        
        # Upsert user to Stream Chat
        service.upsert_user(request.user)
    
    # Create or get channel
    service = StreamChatService()
    channel = service.get_or_create_channel(request.user.id, other_user.id)
    
    context = {
        'other_user': other_user,
        'stream_api_key': settings.STREAM_API_KEY,
        'user_token': request.user.stream_chat_token,
        'user_id': str(request.user.id),
        'channel_id': channel.id
    }
    
    return render(request, 'chat/chat_with_user.html', context)
