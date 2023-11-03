from django.shortcuts import render
from turno.models import Turno

# Create your views here.

def mostrarIndex(request):
    return render(request, 'index.html')


def registrarTurno(request):
    if request.method == 'POST':
        dni = request.POST['txtdni']
        esp = request.POST['textesp']
        fec = request.POST['opcfec']
        hor = request.POST['opchor']
        inter = Turno(Dni = dni, Especialidad = esp, Fecha = fec, Hora = hor)
        inter.save()
        #opcional
        datos = { 'r' : 'Turno Registrado Correctamente!'}
        return render(request, 'index.html', datos)
    else:
        datos = { 'r2' : 'Error al guardar!'}
        return render(request, 'index.html', datos)