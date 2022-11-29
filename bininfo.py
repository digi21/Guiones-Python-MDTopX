from mdtopx import *

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

    cantidad = {
        "lineas": 0,
        "lineas-eliminadas": 0,
        "textos": 0,
        "textos-eliminados": 0,
        "complejos": 0,
        "complejos-eliminados": 0,
        "clotoides": 0,
        "clotoides-eliminadas": 0
    }

    for g in view:
        if type(g) is line:
            if g.deleted:
                cantidad["lineas-eliminadas"] += 1
            else:
                cantidad["lineas"] += 1
        elif type(g) is text:
            if g.deleted:
                cantidad["textos-eliminados"] += 1
            else:
                cantidad["textos"] += 1
        elif type(g) is complex:
            if g.deleted:
                cantidad["complejos-eliminados"] += 1
            else:
                cantidad["complejos"] += 1
        elif type(g) is clotoid:
            if g.deleted:
                cantidad["clotoides"] += 1
            else:
                cantidad["clotoides-eliminadas"] += 1

    print("Líneas: {} de las cuales {} eliminadas".format(cantidad["lineas"] + cantidad["lineas-eliminadas"], cantidad["lineas-eliminadas"]))
    print("Textos: {} de las cuales {} eliminados".format(cantidad["textos"] + cantidad["textos-eliminados"], cantidad["textos-eliminados"]))
    print("Complejos: {} de las cuales {} eliminados".format(cantidad["complejos"] + cantidad["complejos-eliminados"], cantidad["complejos-eliminados"]))
    print("Clotoides: {} de las cuales {} eliminados".format(cantidad["clotoides"] + cantidad["clotoides-eliminadas"], cantidad["clotoides-eliminadas"]))

bininfo()
