from django.http import HttpResponse, JsonResponse, Http404
import json
from django.views.decorators.csrf import csrf_exempt
from .models import Metas
from django.shortcuts import get_object_or_404

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

@csrf_exempt
def metas_path(request):
    if request.method == 'GET':
        return get_metas(request)
    elif request.method == 'POST':
        return crear_meta(request)

@csrf_exempt
def meta_path(request, pk):
    if request.method == 'GET':
        return get_meta(request, pk)
    elif request.method == 'PUT':
        return actualizar_meta(request, pk)
    elif request.method == 'DELETE':
        return borrar_meta(request, pk)
    
def get_metas(request):
    metas = list(Metas.objects.all().values())
    return JsonResponse(metas, safe=False)

def get_meta(request, pk):
    # for meta in metas:
    #     if meta['id'] == pk:
    #         return JsonResponse(meta)
    # raise Http404('Not Found')
    meta = get_object_or_404(Metas, pk=pk)
    return JsonResponse(meta.dict(), safe=False)

def crear_meta(request):
    datos = json.loads(request.body)
    detalles = datos.get('detalles')
    id = datos.get('id')
    if len(detalles) < 5:
        return JsonResponse({ 'error': 'Detalles debe ser >= 5' }, status=400)
    elif id:
        return JsonResponse({ 'error': 'Meta no debe tener id' }, status=400)
    nueva_meta = {
        'id': len(metas) + 1,
        **datos
    }
    metas.append(datos)
    return JsonResponse(nueva_meta, status=201)

def actualizar_meta(request, pk):
    datos = json.loads(request.body)
    detalles = datos.get('detalles')
    id = datos.get('id')
    if len(detalles) < 5:
        return JsonResponse({ 'error': 'Detalles debe ser >= 5' }, status=400)
    elif id:
        return JsonResponse({ 'error': 'Meta no debe tener id' }, status=400)
    
    for meta in metas:
        if meta['id'] == pk:
            meta.update(**datos)
            return JsonResponse(meta, status=201)
        
    raise Http404('Not Found')

def borrar_meta(request, pk):
    for meta in metas:
        if meta['id'] == pk:
            metas.remove(meta)
            return HttpResponse(status=204)
    raise Http404('Not found')