from django.shortcuts import render, redirect, get_object_or_404
from .models import Andamio, Alquiler, Cliente
from .forms import AlquilerForm, AndamioForm, ClienteForm, CustomUserCreationForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.http import Http404
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, permission_required
from rest_framework import serializers, viewsets
from .serializers import AndamioSerializer, AlquilerSerializer, ClienteSerializer


class AndamioViewset(viewsets.ModelViewSet):
    queryset = Andamio.objects.all()
    serializer_class = AndamioSerializer

class AlquilerViewset(viewsets.ModelViewSet):
    queryset = Alquiler.objects.all()
    serializer_class = AlquilerSerializer

class ClienteViewset(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer


def andamios(request):


    andamio = Andamio.objects.all()
    page = request.GET.get('page', 1)

    try:
        paginator = Paginator(andamio, 10)
        andamio = paginator.page(page)
    except:
        raise Http404
    data = {
        'andamio': andamio,
        'paginator': paginator
    }
    return render(request, 'teilur/andamios/listarandamios.html', data)

def home(request):
    return render(request, 'teilur/home.html')


def cliente(request):
    data = {
        'form': ClienteForm()
    }
    if request.method == 'POST':
        formulario = ClienteForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Se ha registrado satisfactoriamente "
        else:
            data["form"] = formulario
    return render(request, 'teilur/registration/register.html', data)

def usuariocreacion(request):
    data = {
        'form': CustomUserCreationForm()
    }

    if request.method == "POST":
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"],
                                password=formulario.cleaned_data["password1"])
            login(request, user)
            messages.success(request, "te has registrado correctamente ")
            return render(request, 'teilur/home.html')

        data["form"] = formulario

    return render(request, 'teilur/registration/register.html', data)


@permission_required('mariam.add_establecimiento')
def agregarandamio(request):
    data = {
        'form': AndamioForm()
    }
    if request.method == 'POST':
        formulario = AndamioForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "establecimiento registrado")
        else:
            data["form"] = formulario
    return render(request, 'mariam/establecimiento/agregar.html', data)


@permission_required('moduloprincipal.view.andamio')
def listarandamios(request):
    andamio = Andamio.objects.all()
    page = request.GET.get('page', 1)

    try:
        paginator = Paginator(andamio, 10)
        andamios = paginator.page(page)
    except:
        raise Http404
    data = {
        'entity': andamios,
        'paginator': paginator
    }
    return render(request, 'teilur/andamios/listarandamios.html', data)


@permission_required('moduloprincipal.change_andamio')
def modificarandamio(request, id):
    andamio = get_object_or_404(Andamio, id=id)

    data = {
        'form': AndamioForm(instance=andamio)
    }

    if request.method == 'POST':
        formulario = AndamioForm(data=request.POST, instance=andamio, files=request.FILES)

        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Andamio modificado correctamente")
            return redirect(to="listarandamios")

        data["form"] = formulario
    return render(request, 'teilur/andamios/modificarandamios.html', data)


@permission_required('moduloprincipal.delete_andamio')
def eliminarandamio(request, id):
    andamio = get_object_or_404(Andamio, id=id)
    Andamio.delete()
    messages.success(request, "Andamio eliminado correctamente")
    return redirect(to="listarandamios")