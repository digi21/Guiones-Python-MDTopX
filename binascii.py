from mdtopx import *

def binascii(view, ruta):
    '''
    Esta función crea un archivo ASCII de Digi3D a partir de las geometrías de la ventana de dibujo
    '''
    with open(ruta, "w") as file:
        for g in view:
            if g.deleted:
                continue

            if type(g) is Line:
                file.write('C={} {}\n'.format(g.code, g.num_points))

                for c in g:
                    file.write('{:.02f} {:.02f} {:.02f}\n'.format(c[0], c[1], c[2]))

            elif type(g) is Text:
                file.write('T={} 1\n'.format(g.code))
                file.write('{} {} {}\n'.format(g.height, g.justification, g.rotation))
                file.write('{:.02f} {:.02f} {:.02f}\n'.format(g.position[0], g.position[1], g.position[2]))
                file.write(g.text)
                file.write('\n')
        
view = current_view()

if view is None:
    raise Exception("No tienes abierta ninguna ventana")

if view is None or type(view) != DrawingView:
    raise Exception("La ventana abierta no es una ventana de dibujo")

ruta = ask_file(False, filetypes=[('Archivos ASCII de Digi3D','*.asc')], title="Selecciona el archivo a crear")
if ruta is not None:
    binascii(view, ruta)