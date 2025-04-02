from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.

metas = [
    {
        'id': 1,
        'detalles': 'Correr por 30 minutos',
        'plazo': 'día',
        'frecuencia': 1,
        'icono': '🏃‍♂️',
        'meta': 365,
        'fecha_limite': '2030-01-01',
        'completado': 5
    },
    {
        'id': 2,
        'detalles': 'Leer libros',
        'plazo': 'año',
        'frecuencia': 6,
        'icono': '📚',
        'meta': 12,
        'fecha_limite': '2030-01-01',
        'completado': 0
    },
    {
        'id': 3,
        'detalles': 'Viajar a nuevos lugares',
        'plazo': 'mes',
        'frecuencia': 1,
        'icono': '✈️',
        'meta': 60,
        'fecha_limite': '2030-01-01',
        'completado': 40
    }
]

def hogar(request):
    return HttpResponse('Bienvenido a la API Metas')

def metas_path(request):
    if request.method == 'GET':
        return get_metas(request)
    elif request.method == 'POST':
        return crear_meta(request)

def meta_path(request, pk):
    if request.method == 'GET':
        return get_meta(request, pk)
    elif request.method == 'PUT':
        return actualizar_meta(request, pk)
    elif request.method == 'DELETE':
        return borrar_meta(request, pk)
    
def get_metas(request):
    return JsonResponse(metas, safe=False)

def get_meta(request, pk):
    return

def crear_meta(request):
    return

def actualizar_meta(request, pk):
    return

def borrar_meta(request, pk):
    return