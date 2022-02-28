from decouple import config

# Ruta csv generada por Scrapper > extraccion_datos
RUTA_CSV = config('RUTA_CSV_PATH')

# Ruta conexion SQL
RUTA_CONEXION_SQL = config('RUTA_CONEXION_PATH')

RUTA_LOG = config('LOG_PATH')
