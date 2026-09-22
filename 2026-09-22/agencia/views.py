from django.shortcuts import render

# Diccionario que define A (llaves) y B (listas)
MENU = {
    'Ventas': ['Nuevos', 'Seminuevos', 'Garantias'],
    'Mecanico': ['Mantenimiento', 'Motor', 'Frenos'],
    'Refacciones': ['Aceites', 'Filtros', 'Llantas'],
    'Hojalateria': ['Pintura', 'Abolladuras']
}

def inicio(request):
    return render(request, 'agencia/inicio.html', {'menu_a': MENU.keys()})

def seccion(request, servicio):
    opciones_b = MENU.get(servicio, [])
    contexto = {
        'menu_a': MENU.keys(),
        'servicio_activo': servicio,
        'opciones_b': opciones_b
    }
    return render(request, 'agencia/inicio.html', contexto)

def detalle(request, servicio, subtema):
    opciones_b = MENU.get(servicio, [])
    contexto = {
        'menu_a': MENU.keys(),
        'servicio_activo': servicio,
        'opciones_b': opciones_b,
        'subtema_activo': subtema,
    }
    return render(request, 'agencia/detalle.html', contexto)