from django import forms
from .models import Service

class ReservationForm(forms.Form):
    nom = forms.CharField(label='Nom', max_length=100, widget=forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-input'}))
    service = forms.ModelChoiceField(label='Service', queryset=Service.objects.all(), widget=forms.Select(attrs={'class': 'form-input'}))
    message = forms.CharField(label='Message', widget=forms.Textarea(attrs={'class': 'form-input', 'rows': 4}),required=False)