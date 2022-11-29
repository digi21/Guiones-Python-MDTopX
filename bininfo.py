from mdtopx import *
from collections import Counter

def bininfo():
    '''
    Simula la orden BININFO de Digi3D: Muestra en el panel de resultados el número de geometrías que tiene el archivo de dibujo
    cargado agrupándolas por su tipo (línea, texto, etc.) e indicando la cantidad de geometrías eliminadas.

    Este ejemplo demuestra que los objetos devueltos por "currentView" son iterables: En caso de que la vista sea de tipo "drawingView"
    la iteración devuelve objetos de tipo "line", "text", "complex", "clotoid". Todos estos objetos heredan de la clase "geometry" que
    proporciona una propiedad de solo lectura denominada "deleted" que indica si la geometría está o no eliminada.
    '''
    view = currentView()

    if view is None:
        raise Exception("No tienes abierta ninguna ventana")

    if view is None or type(view) != drawingView:
        raise Exception("La ventana abierta no es una ventana de dibujo")

    noEliminadas = Counter(type(x) for x in view if not x.deleted)
    eliminadas = Counter(type(x) for x in view if x.deleted)

    def imprime(titulo, tipo, noEliminadas, eliminadas):
        print("{}: {} de las cuales {} eliminadas".format(titulo, noEliminadas[tipo] + eliminadas[tipo], eliminadas[tipo]))

    imprime("Líneas", line, noEliminadas, eliminadas)
    imprime("Textos", text, noEliminadas, eliminadas)
    imprime("Complejos", complex, noEliminadas, eliminadas)
    imprime("Clotoides", clotoid, noEliminadas, eliminadas)

bininfo()