from sqlalchemy import create_engine

# Funcion generadora de conexion a DB, Recibe String con los datos de la conexion

def conexion(connect):
    engine = create_engine(connect)

    return engine
