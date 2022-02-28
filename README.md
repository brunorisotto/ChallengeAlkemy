# Challenge Alkemy
 with Python Data Analytics
 
 

## Descripción
Proyecto hecho con Python, aplicando herramientas Data Analytics



## ● Uso:
Automatización de obtención de DATASETS mediante Web Scrapping con librerías Requests, BeautifulSoup
para luego procesar, normalizar, limpiar la información utilizando librería Pandas, Numpy e introducirla
en base de datos (PostgreSQL) mediante librería SQLAlchemy



## ● Crear entorno virtual desde CMD (Símbolo del sistema de Windows):

Instalar libreria entorno virtual:

- C:\Users\YourUser>pip install virtualenv


Crear entorno virtual:

Por ejemplo:
- C:\Users\YourUser>python -m venv env


Una vez creado el directorio del entorno virtual:

- Introducir carpeta __app__ (proyecto) en directorio creado por entorno virual

- Introducir archivo requeriments.txt en carpeta env\Scripts


Volver al cmd e ingresar a directorio del entorno virtual:

- C:\Users\YourUser>cd env


Ingresar a carpeta Scripts dentro del directorio de entorno virtual:

- C:\Users\YourUser\env>cd scripts


Activar entorno virtual:

- C:\Users\YourUser\env\Scripts>activate


### ● Instalación de dependencias necesarias:

Ejecutar archivo requirements.txt:

- (env) C:\Users\YourUser\env\Scripts>pip install -r requirements.txt


### ● Ejecución de proyecto

Ya con el entorno virtual en óptimas condiciones, puedes ejecutar el proyecto desde cmd
procediendo:

Salir de carpeta Scripts:

- (env) C:\Users\YourUser\env\Scripts>cd ..


Ingresar a carpeta __app__:

- (env) C:\Users\YourUser\env>cd __app__


Ejecutar codigo:

- (env) C:\Users\YourUser\env\__app__>python main.py



## ● Configuración Base de datos:

Accediendo al archivo: settings.ini, variable = RUTA_CONEXION_PATH:

Añadir password, port, name database correspondientes, Por ejemplo:

RUTA_CONEXION_PATH = postgresql://postgres:[password]@localhost:[port]/[name_database <default postgres>]
	


## ● Instalación utilizando linea de comando:

Via Git:

  Clonar en ordenador:

	git clone https://github.com/brunorisotto/ChallengeAlkemy.git
	


## ● Estado del proyecto:

Proyecto terminado.
