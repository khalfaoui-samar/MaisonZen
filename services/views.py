from django.shortcuts import render, redirect
from .forms import ReservationForm
from .models import Service

def service_list(request):
    services = Service.objects.all()
    return render(request, 'services/service_list.html', {'services': services})

def service_list(request):
    services = Service.objects.all()
    return render(request, 'services/service_list.html', {'services': services})

def reservation(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            # Ici tu peux traiter les données, par exemple :
            nom = form.cleaned_data['nom']
            email = form.cleaned_data['email']
            service = form.cleaned_data['service']
            message = form.cleaned_data['message']
            
            # Pour l'instant, on va juste afficher une page de confirmation
            return render(request, 'services/reservation_success.html', {'nom': nom})
    else:
        form = ReservationForm()

    return render(request, 'services/reservation.html', {'form': form})
