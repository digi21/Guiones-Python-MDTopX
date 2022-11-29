from mdtopx import *

def triangula_archivo_dibujo():
    '''
    Pregunta al usuario el archivo de dibujo que quiere triangular mediante el cuadro de diálogo estándar de cargar archivo, 
    crea una ventana de dibujo para el archivo seleccionado, 
    triangula el contenido de la ventana (lo que ocasionará que se abra una ventana nueva con la triangulación)
    y por último cierra la ventana de dibujo, dejando abierta únicamente la ventana con la triangulación.
    '''
    ruta = ask_file(True, filetypes=[('Archivos binarios de Digi3D de doble precisión','*.bind'), ('Archivos binarios de Digi3D clásicos', '*.bin')], title="Selecciona el archivo de dibujo a triangular")
    if ruta is None:
        return

    vista = open_view(ruta)
    vista.triangulate()
    vista.close()

triangula_archivo_dibujo()
