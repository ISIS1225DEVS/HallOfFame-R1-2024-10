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


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""


def new_controller(decision):
    """
    Crea una instancia del modelo
    """
    #TODO: Llamar la función del modelo que crea las estructuras de datos
    control = {
        'model': None
    }
    control['model'] = model.new_data_structs(decision)
    return control


# Funciones para la carga de datos

def load_data(control, tupla_nombre):
    """
    Carga los datos del reto
    """
    tiempo_inicial = get_time()
    name_jobs = tupla_nombre[0]
    name_employment = tupla_nombre[1]
    name_skills = tupla_nombre[2]
    name_multilocations = tupla_nombre[3]
    
    data_structs = control["model"]
    jobs = load_jobs(data_structs, name_jobs)
    jobs_lst = jobs[0]
    jobs_size = jobs[1]
    #model.ordenamiento(5, data_structs)
    multilocations = load_multilocations(data_structs, name_multilocations)
    skills = load_skills(data_structs, name_skills)
    employments = load_employments(data_structs, name_employment)
    tiempo_final = get_time()
    tiempo_total = delta_time(tiempo_inicial, tiempo_final)
    return jobs_lst, jobs_size, multilocations, skills, employments, tiempo_total

def load_jobs(data_structs, name_jobs):
    jobs_file = cf.data_dir + name_jobs
    input_file = csv.DictReader(open(jobs_file, encoding="utf-8"), delimiter=";")
    
    for jobs in input_file:
        model.add_jobs(data_structs, jobs)
    lista_jobs, tamanio_jobs = model.jobs_size(data_structs)
    return lista_jobs, tamanio_jobs

def load_skills(data_structs, name_skills):
    skills_file = cf.data_dir + name_skills
    input_file = csv.DictReader(open(skills_file, encoding="utf-8"), delimiter=";")
    
    for skills in input_file:
        model.add_skills(data_structs, skills)
    return model.skills_size(data_structs)

def load_multilocations(data_structs, name_multilocations):
    multilocations_file = cf.data_dir + name_multilocations
    input_file = csv.DictReader(open(multilocations_file, encoding="utf-8"), delimiter=";")
    
    for multilocations in input_file:
        model.add_multilocations(data_structs, multilocations)
    return model.multilocations_size(data_structs)

def load_employments(data_structs, name_employments):
    employments_file = cf.data_dir + name_employments
    input_file = csv.DictReader(open(employments_file, encoding="utf-8"),delimiter=";")
    
    for employments in input_file:
        model.add_employments(data_structs, employments)
    return model.employments_size(data_structs)

# Funciones de ordenamiento

def sort(control):
    """
    Ordena los datos del modelo
    """
    #TODO: Llamar la función del modelo para ordenar los datos
    pass


# Funciones de consulta sobre el catálogo

def get_data(control, id):
    """
    Retorna un dato por su ID.
    """
    #TODO: Llamar la función del modelo para obtener un dato
    pass

def imprimir_n(control, pos_inicial, total):
    jobs = control["model"]["jobs"]
    n = model.imprimir_n(jobs, pos_inicial, total)
    
    return n


def req_1(control,n_ofertas,codigo_pais,experiencia):
    """
    Retorna el resultado del requerimiento 1
    """
    # TODO: Modificar el requerimiento 1
    tiempo_inicial = get_time()
    lista = model.req_1(control["model"],n_ofertas,codigo_pais,experiencia)
    tiempo_final = get_time()
    tiempo_total = delta_time(tiempo_inicial, tiempo_final)
    return lista, tiempo_total


def req_2(control):
    """
    Retorna el resultado del requerimiento 2
    """
    # TODO: Modificar el requerimiento 2
    pass


def req_3(control, empresa, fecha_inicial, fecha_final):
    """
    Retorna el resultado del requerimiento 3
    """
    # TODO: Modificar el requerimiento 3
    tiempo_inicial = get_time()
    total_ofertas, n_ofertas_experticia, ofertas_en_rango_ordenadas = model.req_3(control["model"], empresa, fecha_inicial, fecha_final)
    tiempo_final = get_time()
    tiempo_total = delta_time(tiempo_inicial, tiempo_final)
    return total_ofertas, n_ofertas_experticia, ofertas_en_rango_ordenadas, tiempo_total


def req_4(control, codigo_pais, fecha_inicial, fecha_final):
    """
    Retorna el resultado del requerimiento 4
    """
    # TODO: Modificar el requerimiento 4
    tiempo_inicial = get_time()
    total_ofertas, total_empresas, total_ciudades, nombre_ciudad_mas_ofertas, cantidad_mayor, nombre_ciudad_menos_ofertas, cantidad_menor, ofertas_de_trabajo_rango_fechas_ordenadas = model.req_4(control, codigo_pais, fecha_inicial, fecha_final)
    tiempo_final = get_time()
    tiempo_total = delta_time(tiempo_inicial, tiempo_final)
    return total_ofertas, total_empresas, total_ciudades, nombre_ciudad_mas_ofertas, cantidad_mayor, nombre_ciudad_menos_ofertas, cantidad_menor, ofertas_de_trabajo_rango_fechas_ordenadas, tiempo_total


def req_5(control):
    """
    Retorna el resultado del requerimiento 5
    """
    # TODO: Modificar el requerimiento 5
    pass

def req_6(control, cantidad_n_ciudades, codigo_pais, nivel_experticia, fecha_inicial, fecha_final):
    """
    Retorna el resultado del requerimiento 6
    """
    # TODO: Modificar el requerimiento 6
    tiempo_inicial = get_time()
    total_ciudades_que_cumplen_con_la_consulta, total_empresas, total_ofertas, promedio_salarios_global, ciudad_con_mas_ofertas, conteo_ciudad_con_mas_ofertas, ciudad_con_menos_ofertas, conteo_ciudad_menos_ofertas, lista_final = model.req_6(control, cantidad_n_ciudades, codigo_pais, nivel_experticia, fecha_inicial, fecha_final)
    tiempo_final = get_time()
    tiempo_total = delta_time(tiempo_inicial, tiempo_final)
    return total_ciudades_que_cumplen_con_la_consulta, total_empresas, total_ofertas, promedio_salarios_global, ciudad_con_mas_ofertas, conteo_ciudad_con_mas_ofertas, ciudad_con_menos_ofertas, conteo_ciudad_menos_ofertas, lista_final, tiempo_total


def req_7(control, n_paises, fecha_inicial, fecha_final):
    """
    Retorna el resultado del requerimiento 7
    """
    # TODO: Modificar el requerimiento 7
    tiempo_inicial = get_time()
    total_ofertas, pais_con_mas_ofertas, conteo_pais_con_mas_ofertas, lista_final = model.req_7(control["model"], n_paises, fecha_inicial, fecha_final)
    tiempo_final = get_time()
    tiempo_total = delta_time(tiempo_inicial, tiempo_final)
    return total_ofertas, pais_con_mas_ofertas, conteo_pais_con_mas_ofertas, lista_final, tiempo_total


def req_8(control):
    """
    Retorna el resultado del requerimiento 8
    """
    # TODO: Modificar el requerimiento 8
    pass





def decidir_metodo_sort(rta, control):
    lista_ordenada = model.ordenamiento(rta, control)
    return lista_ordenada
        

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