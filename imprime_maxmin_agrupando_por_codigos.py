from mdtopx import *

def imprime_maxmin_agrupando_por_codigos():
    ''' 
    Esta función muestra las coordenadas mínimas y máximas de cada código 
    de las geometrías de la ventana de dibujo
    '''
    view = current_view()

    if view is None:
        raise Exception("No tienes abierta ninguna ventana")

    if view is None or type(view) != DrawingView:
        raise Exception("La ventana abierta no es una ventana de dibujo")

    maxmin = {}

    for g in view:
        if g.code not in maxmin:
            maxmin[g.code] = (g.min, g.max)
        else:
            maxmin[g.code] = (min(maxmin[g.code][0], g.min), max(maxmin[g.code][1], g.max))

    for k in maxmin.keys():
        print('{} {} --- {}'.format(k, maxmin[k][0], maxmin[k][1]))

imprime_maxmin_agrupando_por_codigos()