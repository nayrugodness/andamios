from django.contrib.auth.forms import UserCreationForm, User
from .validators import MaxSizeFileValidator
from django.forms import ValidationError
from django import forms
from .models import Andamio, Alquiler, Cliente

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'


class AndamioForm(forms.ModelForm):
    nombre = forms.CharField(min_length=6, max_length=20)
    photo = forms.ImageField(required=False, validators=[MaxSizeFileValidator(max_file_size=2)])


    def clean_name(self):
        nombre = self.cleaned_data["name"]
        exist = Andamio.objects.filter(nombre__iexact=nombre).exists()

        if exist:
           raise ValidationError("Este andamio ya existe ")
           return  nombre

    class Meta:
        model = Andamio
        fields = '__all__'

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email", "password1", "password2"]


class AlquilerForm(forms.ModelForm):

    def reserva(self):
        codigo = self.cleaned_data["id"]
        exist = Alquiler.objects.filter(nombre__iexact=codigo).exists()

        if exist:
            raise ValidationError("Este andamio ya está reservado ")
            return codigo

    class Meta:
        model = Andamio
        fields = '__all__'