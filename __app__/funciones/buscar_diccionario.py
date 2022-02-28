
# Retorna diccionario correspondiente a cada DATASET para renombrar columnas y buscar indices

def buscar_dic_normalizado(nombre_archivo):

    dic_cine = {'Cod_Loc': 'cod_localidad',
                'IdProvincia': 'id_provincia',
                'IdDepartamento': 'id_departamento',
                'Categoría': 'categoría',
                'Provincia': 'provincia',
                'Localidad': 'localidad',
                'Nombre': 'nombre',
                'Dirección': 'domicilio',
                'CP': 'codigo_postal',
                'Teléfono': 'numero_de_telefono',
                'Mail': 'mail',
                'Web': 'web'}

    dic_museo = {'Cod_Loc': 'cod_localidad',
                 'IdProvincia': 'id_provincia',
                 'IdDepartamento': 'id_departamento',
                 'subcategoria': 'categoría',
                 'provincia': 'provincia',
                 'localidad': 'localidad',
                 'nombre': 'nombre',
                 'direccion': 'domicilio',
                 'CP': 'codigo_postal',
                 'telefono': 'numero_de_telefono',
                 'Mail': 'mail',
                 'Web': 'web'}

    dic_biblioteca = {'Cod_Loc': 'cod_localidad',
                      'IdProvincia': 'id_provincia',
                      'IdDepartamento': 'id_departamento',
                      'Categoría': 'categoría',
                      'Provincia': 'provincia',
                      'Localidad': 'localidad',
                      'Nombre': 'nombre',
                      'Domicilio': 'domicilio',
                      'CP': 'codigo_postal',
                      'Teléfono': 'numero_de_telefono',
                      'Mail': 'mail',
                      'Web': 'web'}

    if nombre_archivo == 'cine.csv':
        dic = dic_cine
    if nombre_archivo == 'museo.csv':
        dic = dic_museo
    if nombre_archivo == 'biblioteca_popular.csv':
        dic = dic_biblioteca

    return dic

# Retorna diccionario correspondiente a cada DATASET para renombrar columnas y buscar indices


def buscar_dic_registro(nombre_archivo):

    dic_registro_cine = {'Categoría': 'categoría',
                         'Fuente': 'fuente',
                         'Provincia': 'provincia'}

    dic_registro_museo = {'subcategoria': 'categoría',
                          'fuente': 'fuente',
                          'provincia': 'provincia'}

    dic_registro_biblioteca = {'Categoría': 'categoría',
                               'Fuente': 'fuente',
                               'Provincia': 'provincia'}

    if nombre_archivo == 'cine.csv':
        dic = dic_registro_cine

    if nombre_archivo == 'museo.csv':
        dic = dic_registro_museo

    if nombre_archivo == 'biblioteca_popular.csv':
        dic = dic_registro_biblioteca

    return dic

# Retorna diccionario correspondiente a DATASET cine para renombrar columnas y buscar indices


def buscar_dic_cine(nombre_archivo):

    diccionario_cine = {'Provincia': 'provincia',
                        'Pantallas': 'pantallas',
                        'Butacas': 'butacas',
                        'espacio_INCAA': 'espacio_INCAA'}

    if nombre_archivo == 'cine.csv':
        return diccionario_cine
