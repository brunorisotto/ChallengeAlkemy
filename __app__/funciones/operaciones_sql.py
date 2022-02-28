

# Genera tabla registro con informacion correspondiente mediante tabla_registro de apoyo

def crear_tabla_registro(conex):

    conex.execute('CREATE TABLE IF NOT EXISTS tabla_registro AS (SELECT b.*, SUM(b.cantidad_registro_categoria) over(partition by b.provincia) as cantidad_registro_categorias_por_provincias from (SELECT provincia,categoría,count(categoría) as cantidad_registro_categoria,count(fuente) as cantidad_registro_fuente, fecha_carga FROM tabla_registro_apoyo GROUP BY provincia,categoría,fuente,fecha_carga ORDER BY provincia) as b)')

# Genera tabla registro con informacion correspondiente mediante tabla_cine de apoyo


def crear_tabla_cine(conex):

    conex.execute('CREATE TABLE IF NOT EXISTS tabla_cine AS (SELECT provincia, count(pantallas) as cantidad_pantallas, count(butacas) as cantidad_butacas, count("espacio_INCAA") as espacios_INCAA, fecha_carga FROM tabla_cine_apoyo group by provincia,fecha_carga)')

# Elimina tabla registro de apoyo

def eliminar_tabla_registro_apoyo(conex):

    conex.execute('DROP TABLE IF EXISTS tabla_registro_apoyo')

# Elimina tabla cine de apoyo

def eliminar_tabla_cine_apoyo(conex):

    conex.execute('DROP TABLE IF EXISTS tabla_cine_apoyo')
    
# Elimina tabla normalizada al comienzo del programa si existe

def eliminar_tabla_normalizada(conex):

    conex.execute('DROP TABLE IF EXISTS tabla_normalizada')

# Elimina tabla registro al comienzo del programa si existe

def eliminar_tabla_registro(conex):

    conex.execute('DROP TABLE IF EXISTS tabla_registro')

# Elimina tabla cine al comienzo del programa si existe

def eliminar_tabla_cine(conex):

    conex.execute('DROP TABLE IF EXISTS tabla_cine')


    
