from settings import RUTA_CSV
import requests
from bs4 import BeautifulSoup
from loggers import logger_debug, logger_error

from funciones.guardar_dataset_carpeta import guarda_dataset
from datetime import date

# extraccion de DATASETS


url_principal = 'https://datos.gob.ar/dataset/cultura-mapa-cultural-espacios-culturales/archivo/cultura_4207def0-2ff7-41d5-9095-d42ae8207a5d'
page = requests.get(url_principal)
soup = BeautifulSoup(page.content, 'html.parser')

titular = soup.find_all('div', class_="footer-down")

nombres_dataset = ["museo.csv", "cine.csv", "biblioteca_popular.csv"]

try:
    
    for elem in titular:
        
        for link in elem.find_all('a'):
            
            try:
                
                for archivo in nombres_dataset:

                    if archivo in str(link.get('href')):

                        url = link.get('href')
                        
                        response = requests.get(url, stream=True)
                        
                        ruta_con_archivo = guarda_dataset(archivo)
                        
                        with open(f'{ruta_con_archivo}', 'wb') as file:
                           
                            for chunk in response.iter_content():  # descarga contenido de DATASETS

                                file.write(chunk)

                        response.close()
                
                
            
            except Exception as e:
                
                logger_error.error(e)
                
    logger_debug.debug(f"Web Scrapping con exito.")

except Exception as e:
    
            logger_error.error(e)
