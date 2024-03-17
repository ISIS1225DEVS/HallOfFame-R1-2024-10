"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import model
import time
import csv
csv.field_size_limit(2147483647)

"""
El controlador se encarga de mediar entre la vista y el modelo.
"""


def new_controller():
    """
    Crea una instancia del modelo
    """
    control = {'model': None}
    control['model'] = model.new_data_structs()
    return control


# Funciones para la carga de datos

def load_data(control):
    catalog = control['model']
    numero_jobs = load_jobs(catalog)
    numero_skills = load_skills(catalog)
    numero_employment_types = load_employment_types(catalog)
    numero_multilocations = load_multilocations(catalog)
    return numero_jobs, numero_skills, numero_employment_types, numero_multilocations

def load_jobs(control):
    file = cf.data_dir + 'small-jobs.csv'
    input_file = csv.DictReader(open(file, encoding='utf-8'), delimiter=';')
    for job in input_file:
        for i in job:
            if job[i] == "":
                job[i] = "Unknown"
        model.add_jobs(control['jobs'], job)
    return model.data_size(control['jobs'])

def load_skills(control):
    file = cf.data_dir + 'small-skills.csv'
    with open(file, encoding='utf-8') as file:
        reader = csv.reader(file, delimiter=';')
        headers = ['name', 'level', 'id']  
        for fila in reader:
            skill = {}
            for header, value in zip(headers, fila):
                skill[header] = value
            for llave in skill: 
                if skill[llave] == "":
                    skill[llave] = "Unknown"
            model.add_skills(control['skills'], skill)
    return model.data_size(control['skills'])

def load_employment_types(control):
    file = cf.data_dir + 'small-employments_types.csv'
    with open(file, encoding='utf-8') as file:
        reader = csv.reader(file, delimiter=';')
        headers = ['type', 'id', 'currency_salary', 'salary_from', 'salary_to'] 
        for fila in reader:
            employment_types = {}
            for header, value in zip(headers, fila):
                employment_types[header] = value
            for llave in employment_types:
                if employment_types[llave] == "":
                    employment_types[llave] = "Unknown"
            model.add_employment_types(control['employment_types'], employment_types)
    return model.data_size(control['employment_types'])

def load_multilocations(control):
    file = cf.data_dir + 'small-multilocations.csv'
    with open(file, encoding='utf-8') as file:
        reader = csv.reader(file, delimiter=';')
        headers = ['city', 'street', 'id'] 
        for fila in reader:
            multilocation = {}
            for header, value in zip(headers, fila):
                multilocation[header] = value
            for llave in multilocation:        
                if multilocation[llave] == "":
                    multilocation[llave] = "Unknown"
            model.add_employment_types(control['multilocation'], multilocation)
    return model.data_size(control['multilocation'])

# Funciones de ordenamiento

def sort(control,criterio):
    """
    Ordena los datos del modelo
    """
    #TODO: Llamar la función del modelo para ordenar los datos
    model.insertion_sort(control,criterio)


# Funciones de consulta sobre el catálogo

def get_jobs(control, id):
    pass

def get_skills(control, id):
    pass

def get_employment_types(control, id):
    pass

def get_multilocations(control, id):
    pass

def req_1(control, codigo, nivel_experiencia):
    lista = model.req_1(control, codigo, nivel_experiencia)
    contador = lista[1]
    lista = lista[0]
    size = model.data_size(lista)
    return size, lista, contador

def req_2(control, company_name, ciudad):
    """
    Retorna el resultado del requerimiento 2
    """
    lista = model.req_2(control, company_name, ciudad)
    contador = lista[1]
    lista = lista[0]
    size = model.data_size(lista)
    return size, lista, contador


def req_3(control, company_name, rango_abajo, rango_arriba):
    """
    Retorna el resultado del requerimiento 3
    """
    lista = model.req_3(control, company_name, rango_abajo, rango_arriba)
    num_ofertas_junior = lista[1]
    num_ofertas_mid = lista[2]
    num_ofertas_senior = lista[3]
    size = model.data_size(lista[0])
    lista = lista[0]["elements"]
    return size, lista, num_ofertas_junior, num_ofertas_mid, num_ofertas_senior


def req_4(control, country_code, start_date, end_date):
    """
        Retorna el resultado del requerimiento 4
        Consultar las ofertas que se publicaron en un país durante un periodo de tiempo.

        Argumentos:
            control Dict: Diccionario con la estructura de datos del modelo.
            country_code str: Código del país.
            start_date str: Fecha de inicio del periodo de tiempo.
            end_date str: Fecha de fin del periodo de tiempo.

        Retorna:
            retorno de la función req_4 del paquete model.
    """

    return model.req_4(control, country_code, start_date, end_date)


def req_5(data_structs, nombre, fecha_in, fecha_fin):
    """
    Retorna el resultado del requerimiento 5
    """
    start= get_time()
    r= model.req_5(data_structs, nombre, fecha_in, fecha_fin)
    end= get_time()
    time= delta_time(start, end)
    return r, time
    

def req_6(control, nivel_experiencia, fecha_in, fecha_fin, country_code):
    """
    Retorna el resultado del requerimiento 6
    """
    lista = model.req_6(control, nivel_experiencia, fecha_in, fecha_fin, country_code)
    numero_ciudades = lista[0]
    numero_empresas = lista[1]
    numero_ofertas_publicadas = lista[2]
    salario_promedio_total = lista[3]
    ciudad_mayor_cantidad = lista[4]["elements"]
    ciudad_menor_cantidad = lista[5]["elements"]
    size = model.data_size(lista[6])
    lista = lista[6]["elements"]
    return numero_ciudades, numero_empresas, numero_ofertas_publicadas, salario_promedio_total, ciudad_mayor_cantidad, ciudad_menor_cantidad, lista, size


def req_7(data_structs, n, fecha_in, fecha_fin):
    """
    Retorna el resultado del requerimiento 7
    """
    start= get_time()
    r= model.req_7(data_structs, n, fecha_in, fecha_fin)
    end= get_time()
    time= delta_time(start, end)
    return r, time
    


def req_8(control):
    """
    Retorna el resultado del requerimiento 8
    """
    # TODO: Modificar el requerimiento 8
    pass


# Funciones para medir tiempos de ejecucion

def get_time():
    """
    devuelve el instante tiempo de procesamiento en milisegundos
    """
    return float(time.perf_counter()*1000)


def delta_time(start, end):
    """
    devuelve la diferencia entre tiempos de procesamiento muestreados
    """
    elapsed = float(end - start)
    return elapsed
