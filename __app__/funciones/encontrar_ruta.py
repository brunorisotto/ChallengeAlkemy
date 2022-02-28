import os
from datetime import date

# Provee ruta correspondiente a funcion leer_csv

def encuentra_ruta(nombre_archivo,dir):
    
    ruta_completa = f'{dir}\{date.today().strftime("%Y-%b")}'
    
    
    contenido_carpeta = os.listdir(ruta_completa)
    
    for dataset in contenido_carpeta:
        
        if dataset.find(nombre_archivo):

            ruta = f'{ruta_completa}\{dataset}'
            
    
    
    return ruta
