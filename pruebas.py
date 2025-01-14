import os
import json

def get_course_details(available_courses, datos_folder='datos'):
    """
    Obtiene los detalles de los cursos disponibles a partir de los códigos de curso y categorías.

    Parameters:
    - available_courses (set): Conjunto de códigos de curso disponibles.
    - course_categories_dict (dict): Diccionario que mapea código de curso a categoría.
    - datos_folder (str): Ruta a la carpeta 'datos' que contiene los archivos JSON.

    Returns:
    - dict: Diccionario que mapea cada código de curso a una lista de sus secciones.
    """
    course_categories_dict = {
        '0101': 'Matematicas',
        '0103': 'Matematicas',
        '0107': 'Matematicas',
        '0112': 'Matematicas',
        '0114': 'Matematicas',
        '0118': 'Matematicas',
        '0116': 'Matematicas',
        '0120': 'Matematicas',
        '0122': 'Matematicas',
        '0123': 'Matematicas',
        '0960': 'Matematicas',
        '0962': 'Matematicas',
        # Fisica
        '0147': 'Fisica',
        '0150': 'Fisica',
        '0152': 'Fisica',
        '0154': 'Fisica',
        '0156': 'Fisica',
        '0170': 'Fisica',
        '0172': 'Fisica',
        '0173': 'Fisica',
        '0200': 'Fisica',
        '0202': 'Fisica',
        '0210': 'Fisica',
        '0211': 'Fisica',
        '0212': 'Fisica',
        '0213': 'Fisica',
        '0250': 'Fisica',
        '0380': 'Fisica',
        '0382': 'Fisica',
        '0390': 'Fisica',
        '0392': 'Fisica',
        '0394': 'Fisica',
        '0396': 'Fisica',
        '0412': 'Fisica',
        # Electricidad y electronica
        '0200': 'ElectricidadyElectronica',
        '0204': 'ElectricidadyElectronica',
        '0202': 'ElectricidadyElectronica',
        '0206': 'ElectricidadyElectronica',
        '0208': 'ElectricidadyElectronica',
        '0201': 'ElectricidadyElectronica',
        '0209': 'ElectricidadyElectronica',
        '0214': 'ElectricidadyElectronica',
        '0218': 'ElectricidadyElectronica',
        '0219': 'ElectricidadyElectronica',
        '0220': 'ElectricidadyElectronica',
        '0221': 'ElectricidadyElectronica',
        '0222': 'ElectricidadyElectronica',
        '0224': 'ElectricidadyElectronica',
        '0230': 'ElectricidadyElectronica',
        '0232': 'ElectricidadyElectronica',
        '0233': 'ElectricidadyElectronica',
        '0234': 'ElectricidadyElectronica',
        '0235': 'ElectricidadyElectronica',
        '0239': 'ElectricidadyElectronica',
        '0240': 'ElectricidadyElectronica',
        '0241': 'ElectricidadyElectronica',
        '0246': 'ElectricidadyElectronica',
        '0248': 'ElectricidadyElectronica',
        '0249': 'ElectricidadyElectronica',
        '0462': 'ElectricidadyElectronica',
        '0769': 'ElectricidadyElectronica',
        '0980': 'ElectricidadyElectronica',
        '0991': 'ElectricidadyElectronica',
        '0090': 'ElectricidadyElectronica',
        '0092': 'ElectricidadyElectronica',
        #quimica
        '0348': 'Quimica',
        '0349': 'Quimica',
        '0352': 'Quimica',
        '0358': 'Quimica',
        '0360': 'Quimica',
        '0361': 'Quimica',
        '0370': 'Quimica',
        '0380': 'Quimica',
        '0382': 'Quimica',
        '0398': 'Quimica',
        '0409': 'Quimica',
        '0410': 'Quimica',
        '0412': 'Quimica',
        '0432': 'Quimica',
        '0434': 'Quimica',
        '0440': 'Quimica',
        '0442': 'Quimica',
        '0452': 'Quimica',
        '0486': 'Quimica',
        '0027': 'Quimica',
        # ciencias Hidro
        '0193': 'CienciasHidro',
        '0252': 'CienciasHidro',
        '0258': 'CienciasHidro',
        '0262': 'CienciasHidro',
        '0286': 'CienciasHidro',
        #construccion
        '0300': 'Construccion',
        '0302': 'Construccion',
        '0311': 'Construccion',
        '0314': 'Construccion',
        '0316': 'Construccion',
        '0318': 'Construccion',
        '0322': 'Construccion',
        '0324': 'Construccion',
        '0332': 'Construccion',
        '0346': 'Construccion',
        '0368': 'Construccion',
        '0450': 'Construccion',
        '0452': 'Construccion',
        '0453': 'Construccion',
        '0455': 'Construccion',
        '0458': 'Construccion',
        '0460': 'Construccion',
        '0550': 'Construccion',
        '5009': 'Construccion',
        '0075': 'Construccion',
        '0080': 'Construccion',
        '0082': 'Construccion',
        '0084': 'Construccion',
        #Administracion industial
        '0421': 'AdministracionIndustrial',
        '0423': 'AdministracionIndustrial',
        '0434': 'AdministracionIndustrial',
        '0437': 'AdministracionIndustrial',
        '0454': 'AdministracionIndustrial',
        '0482': 'AdministracionIndustrial',
        '0502': 'AdministracionIndustrial',
        '0520': 'AdministracionIndustrial',
        '0522': 'AdministracionIndustrial',
        '0606': 'AdministracionIndustrial',
        '0608': 'AdministracionIndustrial',
        '0630': 'AdministracionIndustrial',
        '0632': 'AdministracionIndustrial',
        '0634': 'AdministracionIndustrial',
        '0636': 'AdministracionIndustrial',
        '0637': 'AdministracionIndustrial',
        '0638': 'AdministracionIndustrial',
        '0639': 'AdministracionIndustrial',
        '0640': 'AdministracionIndustrial',
        '0642': 'AdministracionIndustrial',
        '0653': 'AdministracionIndustrial',
        '0706': 'AdministracionIndustrial',
        '0708': 'AdministracionIndustrial',
        '0710': 'AdministracionIndustrial',
        '0238': 'AdministracionIndustrial',
        '0236': 'AdministracionIndustrial',
        '0022': 'AdministracionIndustrial',
        #ambiental
        '0284': 'Ambiental',
        '0288': 'Ambiental',
        '0307': 'Ambiental',
        '0335': 'Ambiental',
        '0370': 'Ambiental',
        '0431': 'Ambiental',
        '0450': 'Ambiental',
        '0474': 'Ambiental',
        '0478': 'Ambiental',
        '0486': 'Ambiental',
        '0879': 'Ambiental',
        '7935': 'Ambiental',
        '0028': 'Ambiental',
        #seguridad e higiene
        '0280': 'SeguridadHigiene',
        '0282': 'SeguridadHigiene',
        '0284': 'SeguridadHigiene',
        '0441': 'SeguridadHigiene',
        '0437': 'SeguridadHigiene',
        '0511': 'SeguridadHigiene',
        '0642': 'SeguridadHigiene',
        '5004': 'SeguridadHigiene',
        '5005': 'SeguridadHigiene',
        '0670': 'SeguridadHigiene',
        #Mecanica
        '0504': 'Mecanica',
        '0506': 'Mecanica',
        '0508': 'Mecanica',
        '0510': 'Mecanica',
        '0512': 'Mecanica',
        '0524': 'Mecanica',
        '0530': 'Mecanica',
        #Estadistica
        '0362': 'Estadistica',
        '0653': 'Estadistica',
        '0650': 'Estadistica',
        '0652': 'Estadistica',
        '0654': 'Estadistica',
        '0669': 'Estadistica',
        '0700': 'Estadistica',
        '0702': 'Estadistica',
        '0704': 'Estadistica',
        '0732': 'Estadistica',
        '0734': 'Estadistica',
        '0736': 'Estadistica',
        '0014': 'Estadistica',
        #informatica
        '0610': 'Informatica',
        '0667': 'Informatica',
        #Ciencias de la computacion
        '0720': 'CienciasComputacion',
        '0722': 'CienciasComputacion',
        '0724': 'CienciasComputacion',
        '0729': 'CienciasComputacion',
        '0770': 'CienciasComputacion',
        '0771': 'CienciasComputacion',
        '0772': 'CienciasComputacion',
        '0773': 'CienciasComputacion',
        '0774': 'CienciasComputacion',
        '0777': 'CienciasComputacion',
        '0778': 'CienciasComputacion',
        '0779': 'CienciasComputacion',
        '0780': 'CienciasComputacion',
        '0781': 'CienciasComputacion',
        '0785': 'CienciasComputacion',
        '0786': 'CienciasComputacion',
        '0795': 'CienciasComputacion',
        '0796': 'CienciasComputacion',
        '0964': 'CienciasComputacion',
        '0968': 'CienciasComputacion',
        '0970': 'CienciasComputacion',
        '0972': 'CienciasComputacion',
        '0975': 'CienciasComputacion',
        #Administracion
        '0656': 'Administracion',
        '0657': 'Administracion',
        '0658': 'Administracion',
        '0660': 'Administracion',
        '0661': 'Administracion',
        '0662': 'Administracion',
        '0665': 'Administracion',
        '0666 ': 'Administracion',
        '0706': 'Administracion',
        '0708': 'Administracion',
        '5006': 'Administracion',
        #Diplomados
        '1023': 'Diplomados',
        '1025': 'Diplomados',
        '1034': 'Diplomados',
        '1035': 'Diplomados',
        '1056': 'Diplomados',
        '1059': 'Diplomados',
        '1060': 'Diplomados',
        '1065': 'Diplomados',
        '1071': 'Diplomados',
        '1074': 'Diplomados',
        '1076': 'Diplomados',
        '1077': 'Diplomados',
        '1084': 'Diplomados',
        '1088': 'Diplomados',
        '1091': 'Diplomados',
        '1092': 'Diplomados',
        '1093': 'Diplomados',
        '1094': 'Diplomados',
        '1095': 'Diplomados',
        '1096': 'Diplomados',
        '3022': 'Diplomados',
        '3116': 'Diplomados',
        '3118': 'Diplomados',
        '3120': 'Diplomados',
        '3123': 'Diplomados',
        '3606': 'Diplomados',
        '3656': 'Diplomados',
        '3657': 'Diplomados',
        '3658': 'Diplomados',
        '3661': 'Diplomados',
        '3662': 'Diplomados',
        '3664': 'Diplomados',
        '3669': 'Diplomados',
        '3710': 'Diplomados',
        #Otros
        '0001': 'Otro',
        '0006': 'Otro',
        '0008': 'Otro',
        '0009': 'Otro',
        '0010': 'Otro',
        '0011': 'Otro',
        '0019': 'Otro',
        '0030': 'Otro',
        '0040': 'Otro',
        '0073': 'Otro',
        '0074': 'Otro',
        '0366': 'Otro',
        '0242': 'Otro',
        '0243': 'Otro',
        '0244': 'Otro',
        '0245': 'Otro',
        '5007': 'Otro',
        '0414': 'Otro',
        '0416': 'Otro',
        '0418': 'Otro',
        '0436': 'Otro',
        '0439': 'Otro',
        '7980': 'Otro',
        '0454': 'Otro',
        '0472': 'Otro',
        '0532': 'Otro',
        '0585': 'Otro',
        '0969': 'Otro'
    }
    
    # Mapea categorías a los códigos de curso en esa categoría
    category_to_courses = {}
    for course_code in available_courses:
        category = course_categories_dict.get(course_code)
        if category:
            category_to_courses.setdefault(category, set()).add(course_code)
        else:
            print(f"Advertencia: Categoría no encontrada para el curso {course_code}")

    # Resultado final
    course_details = {}

    for category, courses in category_to_courses.items():
        # Asumiendo que el nombre del archivo JSON es la categoría en minúsculas + 's'
        # Por ejemplo, "Matematica" -> "matematicas.json"
        filename = f"{category}.json"
        filepath = os.path.join(datos_folder, filename)

        if not os.path.exists(filepath):
            print(f"Advertencia: Archivo JSON no encontrado para la categoría '{category}' en '{filepath}'")
            continue

        with open(filepath, 'r', encoding='utf-8') as file:
            try:
                data = json.load(file)
            except json.JSONDecodeError as e:
                print(f"Error al leer el archivo JSON '{filepath}': {e}")
                continue

        for entry in data:
            nombre_curso = entry.get("Nombre de Curso", "")
            if len(nombre_curso) < 4:
                continue
            curso_codigo = nombre_curso[:4]
            if curso_codigo in courses:
                course_details.setdefault(curso_codigo, []).append(entry)

    return course_details