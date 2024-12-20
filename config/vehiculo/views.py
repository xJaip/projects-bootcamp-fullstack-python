from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages
from .models import Vehiculo
from .forms import VehiculoForm
from django.db.models import Case, When, Value, CharField


def index(request):
    return render(request, 'vehiculo/index.html')


@login_required
@permission_required('vehiculo.add_vehiculo')
def agregar_vehiculo(request):
    if not request.user.has_perm('vehiculo.add_vehiculo'):
        return redirect('index')
    
    if request.method == 'POST':
        form = VehiculoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = VehiculoForm()
    return render(request, 'vehiculo/agregar_vehiculo.html', {'form': form})

def listar_vehiculos(request):
    vehiculos = Vehiculo.objects.all()
    
    vehiculos = Vehiculo.objects.annotate(
        condicion=Case(
            When(precio__lte=10000, then=Value('Bajo')),
            When(precio__lte=30000, then=Value('Medio')),
            default=Value('Alto'),
            output_field=CharField(),
            )
    )
    return render(request, 'vehiculo/listar_vehiculos.html', {'vehiculos': vehiculos})

def registrar_usuario(request):
    
    if request.user.is_authenticated:
        return redirect('index')
    """
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Usuario registrado exitosamente.')
            return redirect('login')
    else:
        form = UserCreationForm()
    """

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            
            try:
                group = Group.objects.get(name='Nuevo Usuario')
                user.groups.add(group)
            except: 
                messages.error(request, "El grupo no existe")
                
            messages.success(request, 'Usuario registrado exitosamente.')
            return redirect('login')
    else:
        form = UserCreationForm()    
    return render(request, 'registration/register.html', {'form': form})

#def loguear_usuario(request):
 #   return render(request, 'registration/login.html')