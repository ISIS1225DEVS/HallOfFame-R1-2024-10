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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
import ast 
from datetime import datetime
from DISClib.ADT import list as lt
from DISClib.ADT import stack as st
from DISClib.ADT import queue as qu
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.Algorithms.Sorting import insertionsort as ins
from DISClib.Algorithms.Sorting import selectionsort as se
from DISClib.Algorithms.Sorting import mergesort as merg
from DISClib.Algorithms.Sorting import quicksort as quk
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá
dos listas, una para los videos, otra para las categorias de los mismos.
"""

# Construccion de modelos


def new_data_structs(decision):
    """
    Inicializa las estructuras de datos del modelo. Las crea de
    manera vacía para posteriormente almacenar la información.
    """
    data_structs = {"jobs": None,
                    "employment": None,
                    "multilocations": None,
                    "skills": None  
                    }
    data_structs["jobs"] = lt.newList(decision)
    data_structs["employments_types"] = lt.newList(decision)
    data_structs["skills"] = lt.newList(decision)
    data_structs["multilocations"] = lt.newList(decision)
    return data_structs
    


# Funciones para agregar informacion al modelo

def add_data(data_structs, data):
    """
    Función para agregar nuevos elementos a la lista
    """
    #TODO: Crear la función para agregar elementos a una lista
    lt.addLast(data_structs,data)
    return data_structs

def add_jobs(data_structs, jobs):
    lt.addLast(data_structs["jobs"], jobs)
    
    return data_structs

def jobs_size(data_structs):
    return lt.size(data_structs["jobs"]), data_structs["jobs"]

def add_skills(data_structs, skills):
    lt.addLast(data_structs["skills"], skills)
    
    return data_structs

def skills_size(data_structs):
    return lt.size(data_structs["skills"])

def add_employments(data_structs, employments):
    lt.addLast(data_structs["employments_types"], employments)
    
    return data_structs

def employments_size(data_structs):
    return lt.size(data_structs["employments_types"])

def add_multilocations(data_structs, multilocations):
    lt.addLast(data_structs["multilocations"], multilocations)
    
    return data_structs

def multilocations_size(data_structs):
    return lt.size(data_structs["multilocations"])
    

# Funciones para creacion de datos

def new_data(id, info):
    """
    Crea una nueva estructura para modelar los datos
    """
    #TODO: Crear la función para estructurar los datos
    pass


# Funciones de consulta

def get_data(data_structs, id):
    """
    Retorna un dato a partir de su ID
    """
    #TODO: Crear la función para obtener un dato de una lista
    pass


def data_size(data_structs):
    """
    Retorna el tamaño de la lista de datos
    """
    #TODO: Crear la función para obtener el tamaño de una lista
    pass

def imprimir_n(data_structs, pos_inicial, total):
    n = lt.subList(data_structs, pos_inicial, total)
    return n


def req_1(data_structs, n_ofertas, codigo_pais, experiencia):
    """
    Función que soluciona el requerimiento 1
    Como analista de datos quiero listar las últimas N ofertas de trabajo (v.gr. las más recientes) ofrecidas en un
país filtrando por el nivel de experticia del puesto (junior, mid, senior).
Los parámetros de entrada de este requerimiento son:
• El número (N) de ofertas a listar (ej.: 3, 5, 10 o 20).
• Código del país (ej.: PL, CO, ES, etc).
• Nivel de experticia de las ofertas a consultar (junior, mid, o senior).
La respuesta esperada debe contener:
• El total de ofertas de trabajo ofrecidas según la condición (junior, mid, o senior).
• Para cada una de las ofertas de la consulta debe presentar la siguiente información:
o Fecha de publicación de la oferta
o Título de la oferta
o Nombre de la empresa de la oferta
o Nivel de experticia de la oferta (es el mismo del filtro)
o País de la empresa de la oferta
o Ciudad de la empresa de la oferta
o Tamaño de la empresa de la oferta
o Tipo de ubicación de trabajo (remote, partialy_remote, office)
o Disponible a contratar ucranianos (Verdadero o Falso)

    """
    # TODO: Realizar el requerimiento 1
    lista = lt.newList() 
    contador_ofertas = 0
    for job in lt.iterator(data_structs["jobs"]):
        if str(job["experience_level"]) == str(experiencia) and str(job["country_code"]) == str(codigo_pais):
            lt.addLast(lista,job)
            contador_ofertas += 1

        if contador_ofertas == n_ofertas:
            break
        
    return lista
        
        
        
        
    


def req_2(data_structs):
    """
    Función que soluciona el requerimiento 2
    """
    # TODO: Realizar el requerimiento 2
    pass


def req_3(data_structs, empresa, fecha_inicial, fecha_final):
    """
    Función que soluciona el requerimiento 3
    Como analista de datos quiero consultar las ofertas de trabajo publicadas por una empresa en un rango de
fechas dado.
Los parámetros de entrada de este requerimiento son:
• Nombre de la empresa.
• La fecha inicial del periodo a consultar (con formato "%Y-%m-%d").
• La fecha final del periodo a consultar (con formato "%Y-%m-%d").
La respuesta esperada debe contener:
• Número total de ofertas.
• Número total de ofertas con experticia junior.
• Número total de ofertas con experticia mid.
• Número total de ofertas con experticia senior.
• El listado de ofertas de la empresa ordenados cronológicamente por fecha y país (v.gr. Para dos
ofertas con la misma fecha, el orden lo decide el país de forma alfabética). Donde para cada uno de
los elementos resultantes contendrá la siguiente información:
o Fecha de la oferta.
o Título de la oferta.
o Nivel de experticia requerido
o Ciudad de la empresa de la oferta
o País de la empresa de la oferta
o Tamaño de la empresa de la oferta
o Tipo de lugar de trabajo de la oferta.
o Disponible a contratar ucranianos (Verdadero o Falso).
Recomendaciones:
• Antes de empezar el desarrollo del requerimiento analice los archivos e identifique posibles valores
para datos como código de país, nivel de experticia, nombre de la empresa y fechas de consulta.
    """
    # TODO: Realizar el requerimiento 3
    jobs = data_structs["jobs"]
    ofertas_en_rango = lt.newList()
    
    fecha_inicial = convertir_fecha(fecha_inicial)
    fecha_final = convertir_fecha(fecha_final)
    n_ofertas_experticia = {"senior": 0, "mid": 0, "junior": 0}
    for job in lt.iterator(jobs):
        
        fecha1 = convertir_fecha(job["published_at"])
        
        if ((fecha_comparacion(fecha1, fecha_inicial)) and (fecha_comparacion(fecha_final, fecha1)) and (job["company_name"] == empresa)):
            lt.addLast(ofertas_en_rango, job)
            if job["experience_level"] == "senior":
                n_ofertas_experticia["senior"] += 1
            elif job["experience_level"] == "mid":
                n_ofertas_experticia["mid"] += 1
            elif job["experience_level"] == "junior":
                n_ofertas_experticia["junior"] += 1
    
    ofertas_en_rango_ordenadas = sa.sort(ofertas_en_rango, cmp_ofertas_by_pais_y_fecha)
    total_ofertas = lt.size(ofertas_en_rango)
    
    return total_ofertas, n_ofertas_experticia, ofertas_en_rango_ordenadas
            
    

def convertir_fecha(fecha):
    año = fecha[:4]
    mes = fecha[5:7]
    dia = fecha[8:10]
    if len(fecha) >= 10:
        horas = fecha[11:13]
    else:
        horas = False
    if len(fecha) >= 13:
        minutos = fecha[14:16]
    else:
        minutos = False
    return año, mes, dia, horas, minutos

def fecha_comparacion(fecha1, fecha2):
    """
    Retorna True si fecha1 es mayor a fecha2
    """
    if(fecha1[0] < fecha2[0]):
        return False
    elif(fecha1[0] > fecha2[0]):
        return True
    else:
        if(fecha1[1] < fecha2[1]):
            return False
        elif(fecha1[1] > fecha2[1]):
            return True
        else:
            if(fecha1[2] < fecha2[2]):
                return False
            elif(fecha1[2] > fecha2[2]):
                return True
            else:
                if(fecha1[3]) != False:
                    if(fecha1[3] < fecha2[3]):
                        return False
                    elif(fecha1[3] > fecha2[3]):
                        return True
                    else:
                        if(fecha1[4]) != False:
                            if(fecha1[4] < fecha2[4]):
                                return False
                            elif(fecha1[4] > fecha2[4]):
                                return True
                            else:
                                return True
                        else:
                            return True
                else:
                    return True



def req_4(data_structs, codigo_pais, fecha_inicial, fecha_final):
    """
    Función que soluciona el requerimiento 4
    """
    # TODO: Realizar el requerimiento 4
    lista_ofertas = data_structs["model"]["jobs"]
    ofertas_de_trabajo_rango_fechas = lt.newList("ARRAY_LIST")
    empresas = [] #hace referencia a las empresas que hicieron una publicación en el país indicado
    ciudades_sin_repetir = {} #hace referencia a las ciudades que pertenecen al país de búsqueda

    #fecha_inicial = datetime.strptime(fecha_inicial, "%Y-%m-%dT%H:%M:%S.%fZ")
    fecha_inicial = convertir_fecha(fecha_inicial)

    fecha_final = convertir_fecha(fecha_final)

    #fecha_final= datetime.strptime(fecha_final, "%Y-%m-%dT%H:%M:%S.%fZ")
    conteo = 0
    for ofertas in lt.iterator(lista_ofertas):
        fecha1 = convertir_fecha(ofertas["published_at"])
        

        if((fecha_comparacion(fecha1, fecha_inicial)) and (fecha_comparacion(fecha_final, fecha1)) and (ofertas["country_code"] == codigo_pais)):

            lt.addLast(ofertas_de_trabajo_rango_fechas, ofertas)
            if(ofertas["company_name"] not in empresas):
                empresas.append(ofertas["company_name"])
            if(ofertas["city"] not in ciudades_sin_repetir):
                ciudades_sin_repetir[ofertas["city"]] = 1
            else:
                ciudades_sin_repetir[ofertas["city"]] += 1
                
                
    nombre_ciudad_mas_ofertas = ""
    cantidad_mayor = -1
    nombre_ciudad_menos_ofertas = ""
    cantidad_menor = -1
    iteracion = 1
    for ciudad in ciudades_sin_repetir:
        if(iteracion == 1):
            nombre_ciudad_menos_ofertas = ciudad
            cantidad_menor = ciudades_sin_repetir[ciudad]
            iteracion += 1
        if(ciudades_sin_repetir[ciudad] > cantidad_mayor):
            cantidad_mayor = ciudades_sin_repetir[ciudad]
            nombre_ciudad_mas_ofertas = ciudad
        if(ciudades_sin_repetir[ciudad] < cantidad_menor):
            cantidad_menor = ciudades_sin_repetir[ciudad]
            nombre_ciudad_menos_ofertas = ciudad
            
    total_ofertas = lt.size(ofertas_de_trabajo_rango_fechas)
    total_empresas = len(empresas)
    total_ciudades = len(ciudades_sin_repetir)
    
    #print(total_ofertas)
    #print(total_empresas)
    #print(total_ciudades)
    #print(ofertas_de_trabajo_rango_fechas)
    #print("veces for: " + str(conteo))
    #print(lt.size(data_structs["model"]["jobs"]))
    ofertas_de_trabajo_rango_fechas_ordenadas = sa.sort(ofertas_de_trabajo_rango_fechas, cmp_ofertas_by_empresa_y_fecha)
    
    if(total_ofertas == 0):
        return False
     
    return total_ofertas, total_empresas, total_ciudades, nombre_ciudad_mas_ofertas, cantidad_mayor, nombre_ciudad_menos_ofertas, cantidad_menor, ofertas_de_trabajo_rango_fechas_ordenadas
        
        
# def req_4(data_structs, codigo_pais, fecha_inicial, fecha_final):
#     """
#     Función que soluciona el requerimiento 4
#     """
#     # TODO: Realizar el requerimiento 4
#     lista_ofertas = data_structs["model"]["jobs"]
#     ofertas_de_trabajo_rango_fechas = lt.newList("ARRAY_LIST")
#     empresas = lt.newList("ARRAY_LIST") #hace referencia a las empresas que hicieron una publicación en el país indicado
#     ciudades_sin_repetir = {} #hace referencia a las ciudades que pertenecen al país de búsqueda

#     #fecha_inicial = datetime.strptime(fecha_inicial, "%Y-%m-%dT%H:%M:%S.%fZ")
#     fecha_inicial = convertir_fecha(fecha_inicial)

#     fecha_final = convertir_fecha(fecha_final)

#     #fecha_final= datetime.strptime(fecha_final, "%Y-%m-%dT%H:%M:%S.%fZ")
#     conteo = 0
#     for ofertas in lt.iterator(lista_ofertas):
#         fecha1 = convertir_fecha(ofertas["published_at"])
        

#         if((fecha_comparacion(fecha1, fecha_inicial)) and (fecha_comparacion(fecha_final, fecha1)) and (ofertas["country_code"] == codigo_pais)):

#             lt.addLast(ofertas_de_trabajo_rango_fechas, ofertas)
#             if(lt.isPresent(empresas, ofertas["company_name"]) == 0):
#                lt.addLast(empresas, ofertas["company_name"])
#             if(ofertas["city"] not in ciudades_sin_repetir):
#                 ciudades_sin_repetir[ofertas["city"]] = 1
#             else:
#                 ciudades_sin_repetir[ofertas["city"]] += 1
                
                
#     nombre_ciudad_mas_ofertas = ""
#     cantidad_mayor = -1
#     nombre_ciudad_menos_ofertas = ""
#     cantidad_menor = -1
#     iteracion = 1
#     for ciudad in ciudades_sin_repetir:
#         if(iteracion == 1):
#             nombre_ciudad_menos_ofertas = ciudad
#             cantidad_menor = ciudades_sin_repetir[ciudad]
#             iteracion += 1
#         if(ciudades_sin_repetir[ciudad] > cantidad_mayor):
#             cantidad_mayor = ciudades_sin_repetir[ciudad]
#             nombre_ciudad_mas_ofertas = ciudad
#         if(ciudades_sin_repetir[ciudad] < cantidad_menor):
#             cantidad_menor = ciudades_sin_repetir[ciudad]
#             nombre_ciudad_menos_ofertas = ciudad
            
#     total_ofertas = lt.size(ofertas_de_trabajo_rango_fechas)
#     total_empresas = len(empresas)
#     total_ciudades = len(ciudades_sin_repetir)
    
#     #print(total_ofertas)
#     #print(total_empresas)
#     #print(total_ciudades)
#     #print(ofertas_de_trabajo_rango_fechas)
#     #print("veces for: " + str(conteo))
#     #print(lt.size(data_structs["model"]["jobs"]))
#     ofertas_de_trabajo_rango_fechas_ordenadas = sa.sort(ofertas_de_trabajo_rango_fechas, cmp_ofertas_by_empresa_y_fecha)
    
#     if(total_ofertas == 0):
#         return False
     
#     return total_ofertas, total_empresas, total_ciudades, nombre_ciudad_mas_ofertas, cantidad_mayor, nombre_ciudad_menos_ofertas, cantidad_menor, ofertas_de_trabajo_rango_fechas_ordenadas
        

def req_5(data_structs):
    """
    Función que soluciona el requerimiento 5
    """
    # TODO: Realizar el requerimiento 5
    pass

def compare_id(id1, id2):
    return id1["id"] < id2["id"]

def ordenar_ciudades(dato1, dato2):

    ciudad_1 = dato1["city"]
    ciudad_2 = dato2["city"]
    
    if(ciudad_1 < ciudad_2):
        return True
    else:
        return False



def buscar_salario_oferta(data_structs, jobs):

    lista_salarios = data_structs["model"]["employments_types"]
    id_jobs = jobs["id"]
    #voy a usar búsqueda binaria
    top = lt.size(lista_salarios)
    valor_ref = 0
    if(top != None):
        indice_inicial = 1
        while indice_inicial <= top:
            valor_ref = (indice_inicial + top) / 2
            valor_ref = int(valor_ref)
            elemento_buscado= lt.getElement(lista_salarios, valor_ref)
            if(top != None):
                if elemento_buscado["id"] < id_jobs:
                    indice_inicial = valor_ref + 1
                elif elemento_buscado["id"] > id_jobs:
                    top = valor_ref - 1
                else:
                    if(elemento_buscado != None):
                        return elemento_buscado
        
    
    
    # for info_trabajo in lt.iterator(lista_salarios):
    #      if info_trabajo["id"] == id:
    #          salario_menor = info_trabajo["salary_from"]
    #          if salario_menor == '':
    #              salario_menor = None
    #          else:
    #              salario_menor = int(salario_menor)
    #          salario_mayor = info_trabajo["salary_to"]
    #          if salario_mayor == '':
    #              salario_mayor = None
    #          else:
    #              salario_mayor = int(salario_mayor)
    #          if((salario_mayor != None) and (salario_menor != None)):
    #             promedio_salario = (salario_mayor + salario_menor)/2
    #          else:
    #             promedio_salario = None
    # return salario_menor, salario_mayor, promedio_salario

def req_6(data_structs, cantidad_n_ciudades, codigo_pais, nivel_experticia, fecha_inicial, fecha_final):
    #conteo_n_ciudades = 0
    lista_ofertas = data_structs["model"]["jobs"]
    fecha_inicial = convertir_fecha(fecha_inicial)
    fecha_final = convertir_fecha(fecha_final)
    
    data_structs["model"]["employments_types"] = sa.sort(data_structs["model"]["employments_types"], compare_id)
    
    posicion = 1
    #diccionario_a_retornar = {}
    empresas_sin_repetir = []
    total_ofertas = 0
    data_structs["model"]["jobs"] = sa.sort(data_structs["model"]["jobs"], ordenar_ciudades)
    array_inicial = lt.newList("ARRAY_LIST")
    for ofertas in lt.iterator(lista_ofertas):
        fecha1 = convertir_fecha(ofertas["published_at"])
        if codigo_pais != False: #caso para un país específico
            if ((ofertas["country_code"] == codigo_pais) and (ofertas["experience_level"] == nivel_experticia) and fecha_comparacion(fecha1, fecha_inicial)) and (fecha_comparacion(fecha_final, fecha1)):
                if(ofertas["company_name"]) not in empresas_sin_repetir:
                    empresas_sin_repetir.append(ofertas["company_name"])
                total_ofertas += 1
                
                correspondiente_salario = buscar_salario_oferta(data_structs, ofertas)
                
                salario_menor = correspondiente_salario["salary_from"]
                salario_mayor = correspondiente_salario["salary_to"]
                if salario_menor != "":
                    promedio_salario = (int(salario_menor) + int(salario_mayor))/2
                else:
                    promedio_salario = None
                if promedio_salario != None:
                    if(lt.size(array_inicial) == 0):
                        actual_vigente = ofertas["city"]
                        posicion = 1
                        salario_global = promedio_salario
                        nombre_ciudad = ofertas["city"]
                        cantidad_ofertas_ciudad = 1
                        empresas = [ofertas["company_name"]]
                        lt.addLast( array_inicial, {"nombre ciudad": nombre_ciudad,
                                                                "cantidad ofertas": cantidad_ofertas_ciudad,
                                                                "promedio salario": promedio_salario,
                                                                "lista empresas": empresas,
                                                                "mejor oferta": ofertas,
                                                                "salario mejor oferta": salario_mayor,
                                                                "peor oferta": ofertas,
                                                                "salario peor oferta": salario_menor,
                                                                "empresas sin repetir": empresas
                                                                })
                    elif ofertas["city"] == actual_vigente:
                        lt.getElement(array_inicial, posicion)["cantidad ofertas"] += 1
                        lt.getElement(array_inicial, posicion)["promedio salario"] += promedio_salario
                        lt.getElement(array_inicial, posicion)["lista empresas"].append(ofertas["company_name"])
                        if ofertas["company_name"] not in lt.getElement(array_inicial, posicion)["empresas sin repetir"]:
                            lt.getElement(array_inicial, posicion)["empresas sin repetir"].append(ofertas["company_name"])
                        if salario_mayor >lt.getElement(array_inicial, posicion)["salario mejor oferta"]:
                            lt.getElement(array_inicial, posicion)["salario mejor oferta"] = salario_mayor
                            lt.getElement(array_inicial, posicion)["mejor oferta"] = ofertas
                        if salario_menor < lt.getElement(array_inicial, posicion)["salario peor oferta"]:
                            lt.getElement(array_inicial, posicion)["salario peor oferta"] = salario_menor
                            lt.getElement(array_inicial, posicion)["peor oferta"] = ofertas
                    else:
                        actual_vigente = ofertas["city"]
                        posicion += 1
                        salario_global = promedio_salario
                        nombre_ciudad = ofertas["city"]
                        cantidad_ofertas_ciudad = 1
                        empresas = [ofertas["company_name"]]
                        lt.addLast( array_inicial, {"nombre ciudad": nombre_ciudad,
                                                                "cantidad ofertas": cantidad_ofertas_ciudad,
                                                                "promedio salario": promedio_salario,
                                                                "lista empresas": empresas,
                                                                "mejor oferta": ofertas,
                                                                "salario mejor oferta": salario_mayor,
                                                                "peor oferta": ofertas,
                                                                "salario peor oferta": salario_menor,
                                                                "empresas sin repetir": empresas
                                                                })

                else:
                    if ofertas["city"] == actual_vigente:
                        lt.getElement(array_inicial, posicion)["cantidad ofertas"] += 1

        else:
            if ((ofertas["experience_level"] == nivel_experticia) and fecha_comparacion(fecha1, fecha_inicial)) and (fecha_comparacion(fecha_final, fecha1)):
                correspondiente_salario = buscar_salario_oferta(data_structs, ofertas)
                
                salario_menor = correspondiente_salario["salary_from"]
                salario_mayor = correspondiente_salario["salary_to"]
                if salario_menor != "":
                    promedio_salario = (int(salario_menor) + int(salario_mayor))/2
                else:
                    promedio_salario = None
                if promedio_salario != None:
                    if(lt.size(array_inicial) == 0):
                        actual_vigente = ofertas["city"]
                        posicion = 1
                        salario_global = promedio_salario
                        nombre_ciudad = ofertas["city"]
                        cantidad_ofertas_ciudad = 1
                        empresas = [ofertas["company_name"]]
                        lt.addLast( array_inicial, {"nombre ciudad": nombre_ciudad,
                                                                "cantidad ofertas": cantidad_ofertas_ciudad,
                                                                "promedio salario": promedio_salario,
                                                                "lista empresas": empresas,
                                                                "mejor oferta": ofertas,
                                                                "salario mejor oferta": salario_mayor,
                                                                "peor oferta": ofertas,
                                                                "salario peor oferta": salario_menor,
                                                                "empresas sin repetir": empresas
                                                                })
                    elif ofertas["city"] == actual_vigente:
                        lt.getElement(array_inicial, posicion)["cantidad ofertas"] += 1
                        lt.getElement(array_inicial, posicion)["promedio salario"] += promedio_salario
                        lt.getElement(array_inicial, posicion)["lista empresas"].append(ofertas["company_name"])
                        if ofertas["company_name"] not in lt.getElement(array_inicial, posicion)["empresas sin repetir"]:
                            lt.getElement(array_inicial, posicion)["empresas sin repetir"].append(ofertas["company_name"])
                        if salario_mayor >lt.getElement(array_inicial, posicion)["salario mejor oferta"]:
                            lt.getElement(array_inicial, posicion)["salario mejor oferta"] = salario_mayor
                            lt.getElement(array_inicial, posicion)["mejor oferta"] = ofertas
                        if salario_menor < lt.getElement(array_inicial, posicion)["salario peor oferta"]:
                            lt.getElement(array_inicial, posicion)["salario peor oferta"] = salario_menor
                            lt.getElement(array_inicial, posicion)["peor oferta"] = ofertas
                    else:
                        actual_vigente = ofertas["city"]
                        posicion += 1
                        salario_global = promedio_salario
                        nombre_ciudad = ofertas["city"]
                        cantidad_ofertas_ciudad = 1
                        empresas = [ofertas["company_name"]]
                        lt.addLast( array_inicial, {"nombre ciudad": nombre_ciudad,
                                                                "cantidad ofertas": cantidad_ofertas_ciudad,
                                                                "promedio salario": promedio_salario,
                                                                "lista empresas": empresas,
                                                                "mejor oferta": ofertas,
                                                                "salario mejor oferta": salario_mayor,
                                                                "peor oferta": ofertas,
                                                                "salario peor oferta": salario_menor,
                                                                "empresas sin repetir": empresas
                                                                })

                else:
                    if ofertas["city"] == actual_vigente:
                        lt.getElement(array_inicial, posicion)["cantidad ofertas"] += 1
                    
    

    
    sa.sort(array_inicial, cmp_function_ordenar_ciudades_con_mas_ofertas_nombres)
    #print(array_inicial)
    
    if cantidad_n_ciudades > lt.size(array_inicial):
         cantidad_n_ciudades = lt.size(array_inicial)
    sublista_de_las_N_ciudades = lt.subList(array_inicial, 1, cantidad_n_ciudades)
    
    
    lista_final = lt.newList("ARRAY_LIST")
    #los diccionarios a crear a continuación son únicamente para mostrar la información
    for x in lt.iterator(sublista_de_las_N_ciudades):
         diccionario_final = {"Nombre ciudad": "", "Conteo ofertas": "", "Promedio del salario": "","Cantidad empresas": "", "Empresa con más ofertas": "", "Conteo empresa con más ofertas": "", "Información mejor oferta": "", "Información peor oferta": ""}
         diccionario_final["Nombre ciudad"] = x["nombre ciudad"]
         diccionario_final["Conteo ofertas"] = x["cantidad ofertas"]
         diccionario_final["Promedio del salario"] = int(x["promedio salario"]) / int(x["cantidad ofertas"])
         diccionario_final["Cantidad empresas"] = len(x["empresas sin repetir"])
         empresa_con_mas_ofertas = max(x["lista empresas"], key=x["lista empresas"].count)
         diccionario_final["Empresa con más ofertas"] = empresa_con_mas_ofertas
         conteo_empresa = x["lista empresas"].count(empresa_con_mas_ofertas)
         diccionario_final["Conteo empresa con más ofertas"] = conteo_empresa
         diccionario_final["Información mejor oferta"] = x["mejor oferta"]
         diccionario_final["Información peor oferta"] = x["peor oferta"]
         lt.addLast(lista_final, diccionario_final)
        
    #print(lista_final)
    
    total_ciudades_que_cumplen_con_la_consulta = lt.size(sublista_de_las_N_ciudades)
    total_empresas = len(empresas_sin_repetir)
    total_ofertas = total_ofertas
    if total_ofertas != 0:
        promedio_salarios_global = salario_global/total_ofertas #únicamente para country_code
    else: 
        promedio_salarios_global = 0
    ciudad_con_mas_ofertas = lt.firstElement(sublista_de_las_N_ciudades)["nombre ciudad"]
    conteo_ciudad_con_mas_ofertas = lt.firstElement(sublista_de_las_N_ciudades)["cantidad ofertas"]
    ciudad_con_menos_ofertas = lt.lastElement(sublista_de_las_N_ciudades)["nombre ciudad"]
    conteo_ciudad_menos_ofertas = lt.lastElement(sublista_de_las_N_ciudades)["cantidad ofertas"]
    
    # print(total_ciudades_que_cumplen_con_la_consulta)
    # print(total_empresas)
    # print(total_ofertas)
    # print(promedio_salarios_global)
    # print(ciudad_con_mas_ofertas)
    # print(conteo_ciudad_con_mas_ofertas)
    # print(ciudad_con_menos_ofertas)
    # print(conteo_ciudad_menos_ofertas)
    
    return total_ciudades_que_cumplen_con_la_consulta, total_empresas, total_ofertas, promedio_salarios_global, ciudad_con_mas_ofertas, conteo_ciudad_con_mas_ofertas, ciudad_con_menos_ofertas, conteo_ciudad_menos_ofertas, lista_final

    
    
    
    
def cmp_function_ordenar_ciudades_con_mas_ofertas_nombres(dato1, dato2):
    cantidad_1 = dato1["cantidad ofertas"]
    cantidad_2 = dato2["cantidad ofertas"]
    
    ciudad_1 = dato1["nombre ciudad"]
    ciudad_2 = dato2["nombre ciudad"]
    
    if(cantidad_1 > cantidad_2):
        return True
    elif(cantidad_1 == cantidad_2):
        if(ciudad_1 < ciudad_2):
            return True
        else:
            return False
    else:
        return False
    
                  
                    
    


# def req_6(data_structs, cantidad_n_ciudades, codigo_pais, nivel_experticia, fecha_inicial, fecha_final):
#     """
#     Función que soluciona el requerimiento 6
#     """
#     # TODO: Realizar el requerimiento 6
    
#     conteo_n_ciudades = 0
#     lista_ofertas = data_structs["model"]["jobs"]
#     ofertas_de_trabajo_caracteristicas_cumplidas = lt.newList("ARRAY_LIST")
#     ciudades_cantidad_empleos = {} #va a ser una lista de diccionarios, que va a tener como llaves {"nombre_ciudad": ----, "total_ofertas_ciudad": ---, 
#     #"suma_promedios_salarios": ---, "empresas_en_ciudad": ---, "informacion_oferta_mejor_salario: ---, 
#     #"informacion_oferta_peor_salario: ---}"  
    
#     #sa.sort(data_structs["model"]["employments_types"])
    
    
#     fecha_inicial = convertir_fecha(fecha_inicial)

#     fecha_final = convertir_fecha(fecha_final)
            
#     for ofertas in lt.iterator(lista_ofertas):
#         fecha1 = convertir_fecha(ofertas["published_at"])
#         #primero voy a agregar todas las ofertas de trabajo que cumplen con las características dadas:
#         if codigo_pais != False: #caso para un país específico
#             if ((ofertas["country_code"] == codigo_pais) and (ofertas["experience_level"] == nivel_experticia) and fecha_comparacion(fecha1, fecha_inicial)) and (fecha_comparacion(fecha_final, fecha1)):
#                 salario_menor, salario_mayor, promedio_salario = buscar_salario_oferta(data_structs, ofertas["id"])
#                 if promedio_salario != None:
#                     oferta_con_salario = {"title": ofertas["title"], "city": ofertas["city"], "country_code": ofertas["country_code"], "company_name": ofertas["company_name"],
#                                         "salario_menor": salario_menor, "salario_mayor": salario_mayor, "promedio_salario": promedio_salario}
#                     lt.addLast(ofertas_de_trabajo_caracteristicas_cumplidas, oferta_con_salario)
#                     if ofertas["city"] not in ciudades_cantidad_empleos:
#                         ciudades_cantidad_empleos[ofertas["city"]] = 1
#                     else:
#                         ciudades_cantidad_empleos[ofertas["city"]] += 1
#         else:
#             if ((ofertas["experience_level"] == nivel_experticia) and fecha_comparacion(fecha1, fecha_inicial)) and (fecha_comparacion(fecha_final, fecha1)):
#                 salario_menor, salario_mayor, promedio_salario = buscar_salario_oferta(data_structs, ofertas["id"])
#                 oferta_con_salario = {"title": ofertas["title"], "city": ofertas["city"], "company_name": ofertas["company_name"],
#                                       "salario_menor": salario_menor, "salario_mayor": salario_mayor, "promedio_salario": promedio_salario}
#                 lt.addLast(ofertas_de_trabajo_caracteristicas_cumplidas, oferta_con_salario)
#                 if ofertas["city"] not in ciudades_cantidad_empleos:
#                     ciudades_cantidad_empleos[ofertas["city"]] = 1
#                 else:
#                     ciudades_cantidad_empleos[ofertas["city"]] += 1
    
#     print(ciudades_cantidad_empleos)
#     array_ciudades_con_mayor_oferta = lt.newList("ARRAY_LIST")
#     #aqui lleno el array para luego ordenarlo
#     for ofertas_que_cumplen_caracteristicas in ciudades_cantidad_empleos:
#         dct_creado = {ofertas_que_cumplen_caracteristicas: ciudades_cantidad_empleos[ofertas_que_cumplen_caracteristicas], 
#                       "quantity": ciudades_cantidad_empleos[ofertas_que_cumplen_caracteristicas], 
#                       "name_city": ofertas_que_cumplen_caracteristicas}
#         lt.addLast(array_ciudades_con_mayor_oferta, dct_creado)
        
#     array_ordenado = sa.sort(array_ciudades_con_mayor_oferta, cmp_function_ordenar_ciudades_con_mas_ofertas)    
#     print(array_ordenado)
    
#     #ahora, voy a hacer un for para recorrer el array_ordenado y obtener las primeras N ciudades que tienen más ofertas de trabajo
#     conteo_n_ciudades = 0
#     lista_ciudades = [] #nombre de las ciudades que tienen la mayor cantidad de ofertas de trabajo
#     for k in lt.iterator(array_ordenado):
#         if conteo_n_ciudades <= cantidad_n_ciudades:
#             lista_ciudades.append(k["name_city"])
#         conteo_n_ciudades += 1
        
#     print(lista_ciudades)
    
#     lista_finalmente_filtrada = lt.newList("ARRAY_LIST")
#     lista_empresas = []
    
#     lista_a_retornar = []
#     for ciudades in lista_ciudades:
#         cantidad_ofertas_por_ciudad = 0
#         promedio_salario_ciudad = 0
#         lista_empresas = []
#         info_mejor_oferta = ""
#         salario_mejor_oferta = 0
#         salario_menor_oferta = 5000000
#         info_peor_oferta = ""
#         for j in lt.iterator(ofertas_de_trabajo_caracteristicas_cumplidas):
#             if(j["city"] == ciudades):
#                 lt.addLast(lista_finalmente_filtrada, j)
#                 cantidad_ofertas_por_ciudad += 1
#                 promedio_salario_ciudad += j["promedio_salario"]
#                 lista_empresas.append(j["company_name"])
#                 if(j["salario_mayor"] > salario_mejor_oferta):
#                     salario_mejor_oferta = j["salario_mayor"]
#                     info_mejor_oferta = j
#                 if(j["salario_menor"] < salario_menor_oferta):
#                     salario_menor_oferta = j["salario_menor"]
#                     info_peor_oferta = j
#         frecuencia_empresas = {}

#         # Iterar sobre la lista y contar las repeticiones de cada elemento
#         for elemento in lista_empresas:
#             if elemento in frecuencia_empresas:
#                 frecuencia_empresas[elemento] += 1
#             else:
#                 frecuencia_empresas[elemento] = 1
#         numero_total_empresas = len(frecuencia_empresas)
        
#         # Encontrar el elemento con la mayor frecuencia
#         empresa_con_mas_ofertas = None
#         conteo_ofertas = 0

#         for elemento, repeticiones in frecuencia_empresas.items():
#             if repeticiones > conteo_ofertas:
#                 empresa_con_mas_ofertas = elemento
#                 conteo_ofertas = repeticiones
                
        
#         lista_a_retornar.append({"ciudad": ciudades, 
#                                  "total ofertas ciudad": cantidad_ofertas_por_ciudad, 
#                                  "promedio salario ciudad": ((promedio_salario_ciudad)/(cantidad_ofertas_por_ciudad)),
#                                  "total empresas con al menos una oferta": numero_total_empresas, 
#                                  "empresa con más ofertas": empresa_con_mas_ofertas,
#                                  "conteo empresa con mas ofertas": conteo_ofertas,
#                                  "informacion mejor oferta": info_mejor_oferta,
#                                  "informacion peor oferta": info_peor_oferta})      
#     print(lista_a_retornar)            
                
                
    
    
#     #print(lista_finalmente_filtrada)            
#     #notese que la lista_finalmente_filtrada tiene únicamente aquellas ofertas de trabajo que cumplen con todos los requisitos, y que están
#     #en las N ciudades que el usuario diga. Adicionalmente, ya están ordenadas de las que tienen mayor número de ofertas y menor número de ofertas. no se tiene que volver a ordenar !!! :)
#     for ofertas in lt.iterator(lista_finalmente_filtrada):
#         if ofertas["company_name"] not in lista_empresas:
#             lista_empresas.append(ofertas["company_name"])
            
    
    
    
    
    #diccionario_a_retornar = {}
    
    # total_ciudades = len(lista_ciudades)
    # total_empresas = len(lista_empresas)
    # total_ofertas = lt.size(lista_finalmente_filtrada)
    # nombre_ciudad_mayor_ofertas = lista_ciudades[0]
    # cantidad_mayor_ofertas = ciudades_cantidad_empleos[nombre_ciudad_mayor_ofertas]
    # nombre_ciudad_menor_ofertas = lista_ciudades[total_ciudades - 1]
    # cantidad_menor_ofertas = ciudades_cantidad_empleos[nombre_ciudad_menor_ofertas]
    # print(total_ciudades)
    # print(total_empresas)
    # print(total_ofertas)
    # print(cantidad_mayor_ofertas)
    # print(cantidad_menor_ofertas)
    # print(nombre_ciudad_mayor_ofertas)
    # print(nombre_ciudad_menor_ofertas)            
                   
                
def cmp_function_ordenar_ciudades_con_mas_ofertas(ciudad1, ciudad2):
    cantidad_1 = ciudad1["quantity"]
    cantidad_2 = ciudad2["quantity"]
    
    if cantidad_1 < cantidad_2:
        return False
    else:
        return True

#def filtro_habilidades(data_struct, habilidad):
   # if habilidad == "senior":
        #habilidades_senior = lt.newList("ARRAY_LIST")
       # for element in lt.iterator(data_struct["skills"]):
      #      if "senior" in element["id"]:
   #  #           lt.addLast(habilidades_senior, element)
  #      return habilidades_senior
  #  if habilidad == "mid":
  #     for element in lt.iterator(data_struct["skills"]):
   #         if "mid" in element["id"]:
   #             lt.addLast(habilidades_mid, element)
   #     return habilidades_mid
   # if habilidad == "junior":
   #     habilidades_junior = lt.newList("ARRAY_LIST")
   #     for element in lt.iterator(data_struct["skills"]):
  #          if "junior" in element["id"]:
  #              lt.addLast(habilidades_junior, element)
  ##      return habilidades_junior
  
#def filtro_habilidades(data_struct, habilidad, oferta):
     # lista = lt.newList("ARRAY_LIST")
      #for elemen in lt.iterator(data_struct["skills"]):
          


def req_7(data_structs, n_paises, fecha_inicial, fecha_final):
    """
    Como analista de datos, quiero identificar las habilidades solicitadas en los niveles de experticia publicados
en los primeros N países dado un rango de fechas.
Los parámetros de entrada de este requerimiento son:
• El número (N) de países para consulta (ej.: 3, 5, 10 o 20).
• La fecha inicial del periodo a consultar (con formato "%Y-%m-%d").
• La fecha final del periodo a consultar (con formato "%Y-%m-%d").
La respuesta esperada debe contener:
• El total de ofertas de empleo
• Número de ciudades donde se ofertó en los países resultantes de la consulta.
• Nombre del país con mayor cantidad de ofertas y su conteo
• Nombre de la ciudad con mayor cantidad de ofertas y su conteo
• Para el conjunto de las ofertas de trabajo en los países resultantes de la consulta, por cada uno de
los tres niveles de experticia (junior, mid y senior) calcule y presente la siguiente información:
o Conteo de habilidades diferentes solicitadas en ofertas de trabajo
o Nombre de la habilidad más solicitada y su conteo en ofertas de trabajo
o Nombre de la habilidad menos solicitada y su conteo en ofertas de trabajo
o Nivel mínimo promedio de las habilidades
o Conteo de empresas que publicaron una oferta con este nivel
o Nombre de la empresa con mayor número de ofertas y su conteo
o Nombre de la empresa con menor número de ofertas (al menos una) y su conteo
o Número de empresas que publicaron una oferta en este nivel que tienen una o más sedes
Recomendaciones:
• Antes de empezar el desarrollo del requerimiento analice los archivos e identifique posibles valores
para datos como código de país, nivel de experticia, nombre de la empresa y fechas de consulta.
• Si solo una empresa cumple con la condición, presente esta empresa como la empresa con mayor y
menor número de ofertas.
• En caso de que al ordenar por número de ofertas dos o más empresas presentan el mismo número
de ofertas, sobre estas empresas realice un orden alfabético ascendente.
    """
    # TODO: Realizar el requerimiento 7
    """jobs = data_structs["jobs"]
    fecha_inicial = convertir_fecha(fecha_inicial)
    fecha_final = convertir_fecha(fecha_final)
    ofertas = lt.newList("ARRAY_LIST")
    diccionario = {"total_ofertas" : 0 ,
                   "numero_ciudades" : 0,
                   "paises" : {},
                   "ciudades" : {},
                   "habilidades_junior" : {},
                   "empresas_junior" : {},
                   "habilidades_mid" : {},
                   "empresas_mid" : {},
                   "habilidades_senior" : {},
                   "empresas_senior" : {},
                   }
    
    
    for job in lt.iterator(jobs):
        fecha = convertir_fecha(job["published_at"])
        if fecha_comparacion(fecha, fecha_final) and fecha_comparacion(fecha_final, fecha):
            lt.addLast(ofertas, job)
            if job["country_code"] not in diccionario["paises"].keys():
                diccionario["paises"][job["country_code"]] = 1
            else: diccionario["paises"][job["country_code"]] += 1
            if job["city"] not in diccionario["ciudades"].keys():
                diccionario["ciudades"][job["city"]] = 1
            else: diccionario["ciudades"][job["city"]] += 1
            
            if job["experience_level"] == "junior":
                if job["marker_icon"] not in diccionario["habilidades_junior"]:
                    diccionario["habilidades_junior"] = 1
                else: diccionario["habilidades_junior"] += 1
                if job["company_name"] not in diccionario["empresas_junior"]:
                    diccionario["empresas_junior"] = 1
                else: diccionario["empresas_junior"] += 1
            
            if job["experience_level"] == "mid":
                if job["marker_icon"] not in diccionario["habilidades_mid"]:
                    diccionario["habilidades_mid"] = 1
                else: diccionario["habilidades_mid"] += 1
                if job["company_name"] not in diccionario["empresas_mid"]:
                    diccionario["empresas_mid"] = 1
                else: diccionario["empresas_mid"] += 1
            
            if job["experience_level"] == "senior":
                if job["marker_icon"] not in diccionario["habilidades_senior"]:
                    diccionario["habilidades_senior"] = 1
                else: diccionario["habilidades_senior"] += 1
                if job["company_name"] not in diccionario["empresas_senior"]:
                    diccionario["empresas_senior"] = 1
                else: diccionario["empresas_senior"] += 1
                
    estructura_de_datos_paises = lt.newList("ARRAY_LIST")
    for paises in diccionario:
        diccionario_add = diccionario[paises]
        lt.addLast(estructura_de_datos_paises, diccionario_add)"""
    diccionario = {}
    jobs = data_structs["jobs"]
    fecha_inicial = convertir_fecha(fecha_inicial)
    fecha_final = convertir_fecha(fecha_final)
    total_ofertas = 0
    habilidad_junior = None
    habilidad_mid = None
    habilidad_senior = None
    suma_senior = None
    suma_mid = None
    suma_junior = None
    empresas_junior = None
    empresas_mid = None
    empresas_senior = None
    habilidad_junior_append = None
    habilidad_senior_append = None
    habilidad_mid_append = None
    
    data_structs["skills"] = sa.sort(data_structs["skills"], compare_id)
    #ciudades = {}
    for oferta in lt.iterator(jobs):
        fecha = convertir_fecha(oferta["published_at"])
        if fecha_comparacion(fecha, fecha_inicial) and fecha_comparacion(fecha_final, fecha):
            total_ofertas += 1
            #if oferta["city"] not in ciudades:
                #ciudades[oferta["city"]] = 1
            #else: ciudades[oferta["city"]] += 1
            if oferta["experience_level"] == "senior":
                element = buscar_habilidad_oferta(data_structs,oferta)
                #for element in lt.iterator(data_structs["skills"]):
                    #print(element)
                if element["id"] == oferta["id"]:
                    habilidad_senior = [element["name"]]
                    habilidad_senior_append = element["name"]
                suma_senior = int(element["level"])
                #cantidad_senior = 1      
                empresas_senior = [oferta["company_name"]]
                empresas_senior_append = oferta["company_name"]
            if oferta["experience_level"] == "mid":
                element = buscar_habilidad_oferta(data_structs, oferta)
                #for element in lt.iterator(data_structs["skills"]):
                if element["id"] == oferta["id"]:
                    habilidad_mid = [element["name"]]
                    habilidad_mid_append = element["name"]
                suma_mid = int(element["level"])
                #cantidad_mid = 1
                empresas_mid = [oferta["company_name"]]
                empresas_mid_append = oferta["company_name"]
            if oferta["experience_level"] == "junior":
                element = buscar_habilidad_oferta(data_structs, oferta)
                #for element in lt.iterator(data_structs["skills"]):
                if element["id"] == oferta["id"]:
                    habilidad_junior = [element["name"]]
                    habilidad_junior_append = element["name"]
                suma_junior = int(element["level"])
                #cantidad_junior = 1
                empresas_junior = [oferta["company_name"]]
                empresas_junior_append = oferta["company_name"]
                
        
            
            if oferta["country_code"] not in diccionario:
                pais = oferta["country_code"]
                cantidad_ofertas_pais = 1
                ciudades = [oferta["city"]]
                
                diccionario[pais] = {"nombre pais" : pais,
                                     "cantidad ofertas" : cantidad_ofertas_pais,
                                     "ciudades" : ciudades,
                                     "junior" : {"habilidades_junior" : habilidad_junior,
                                                 "suma_junior" : suma_junior,
                                                 "contador_junior" : 1,
                                                 "empresas_junior" : empresas_junior},
                                     "mid" : {"habilidades_mid" : habilidad_mid,
                                              "suma_mid" : suma_mid,
                                                 "contador_mid" : 1,
                                                 "empresas_mid" : empresas_mid},
                                     "senior" : {"habilidades_senior" : habilidad_senior,
                                                 "suma_senior" : suma_senior,
                                                 "contador_senior" : 1,
                                                 "empresas_senior" : empresas_senior}
                                     }
            else: 
                diccionario[pais]["cantidad ofertas"] += 1
                diccionario[pais]["ciudades"].append(oferta["city"])
                #JUNIOR
                if (habilidad_junior_append != None) and (diccionario[pais]["junior"]["habilidades_junior"] != None):
                    diccionario[pais]["junior"]["habilidades_junior"].append(habilidad_junior_append)
                if (suma_junior != None) and (diccionario[pais]["junior"]["suma_junior"] != None):
                    diccionario[pais]["junior"]["suma_junior"] +=suma_junior
                diccionario[pais]["junior"]["contador_junior"] += 1
                if (empresas_junior != None) and (diccionario[pais]["junior"]["empresas_junior"] != None):
                    diccionario[pais]["junior"]["empresas_junior"].append(empresas_junior_append)
                
                #MID
                
                #print("antes")
                #print(habilidad_mid)
                if (habilidad_mid_append !=  None) and (diccionario[pais]["mid"]["habilidades_mid"] != None):
                    #print("despues")
                    #print(habilidad_mid)
                    diccionario[pais]["mid"]["habilidades_mid"].append(habilidad_mid_append)
                if (suma_mid != None) and (diccionario[pais]["mid"]["suma_mid"] != None):
                    diccionario[pais]["mid"]["suma_mid"] +=suma_mid
                diccionario[pais]["mid"]["contador_mid"] += 1
                if (empresas_mid != None) and (diccionario[pais]["mid"]["empresas_mid"] != None):
                    diccionario[pais]["mid"]["empresas_mid"].append(empresas_mid_append)
                
                #SENIOR
                if (habilidad_senior_append != None) and (diccionario[pais]["senior"]["habilidades_senior"] != None):
                    diccionario[pais]["senior"]["habilidades_senior"].append(habilidad_senior_append)
                if (suma_senior != None) and (diccionario[pais]["senior"]["suma_senior"] != None):
                    diccionario[pais]["senior"]["suma_senior"] +=suma_senior
                diccionario[pais]["senior"]["contador_senior"] += 1
                if (empresas_senior != None) and (diccionario[pais]["senior"]["empresas_senior"] != None):
                    diccionario[pais]["senior"]["empresas_senior"].append(empresas_senior_append)
    #numero_ciudades = len(ciudades)
    #ciudad_con_mayor_n_ofertas = max(ciudades, key=ciudades.get)            
    
    #print(diccionario)
    
    estructura_de_datos_paises = lt.newList("ARRAY_LIST")
    for paises in diccionario.keys():
        diccionario_add = diccionario[paises]
        lt.addLast(estructura_de_datos_paises, diccionario_add)
    quk.sort(estructura_de_datos_paises, cmp_function_ordenar_paises_con_mas_ofertas_nombres)
    
    #print(estructura_de_datos_paises)
    
    if n_paises > lt.size(estructura_de_datos_paises):
        n_paises = lt.size(estructura_de_datos_paises)
    sublista_de_las_N_paises = lt.subList(estructura_de_datos_paises, 1, n_paises)
    
    lista_final = lt.newList("ARRAY_LIST")
    for x in lt.iterator(sublista_de_las_N_paises):
        ciudad_con_mas_ofertas = max(x["ciudades"], key=x["ciudades"].count)
        conteo_ciudad_mas_ofertas = x["ciudades"].count(ciudad_con_mas_ofertas)
        numero_ciudades = len(x["ciudades"])
        #junior
        habilidad_mas_solicitada_junior = max(x["junior"]["habilidades_junior"], key=x["junior"]["habilidades_junior"].count)
        conteo_habilidad_mas_solicitada_junior = x["junior"]["habilidades_junior"].count(habilidad_mas_solicitada_junior)
        habilidad_menos_solicitada_junior = min(x["junior"]["habilidades_junior"], key=x["junior"]["habilidades_junior"].count)
        conteo_habilidad_menos_solicitada_junior = x["junior"]["habilidades_junior"].count(habilidad_menos_solicitada_junior)
        promedio_junior = int(x["junior"]["suma_junior"]) / int(x["junior"]["contador_junior"])
        empresas_junior_con_mas_ofertas = max(x["junior"]["empresas_junior"], key=x["junior"]["empresas_junior"].count)
        conteo_empresas_junior_con_mas_ofertas = x["junior"]["empresas_junior"].count(empresas_junior_con_mas_ofertas)
        
        #mid
        habilidad_mas_solicitada_mid = max(x["mid"]["habilidades_mid"], key=x["mid"]["habilidades_mid"].count)
        conteo_habilidad_mas_solicitada_mid = x["mid"]["habilidades_mid"].count(habilidad_mas_solicitada_mid)
        habilidad_menos_solicitada_mid = min(x["mid"]["habilidades_mid"], key=x["mid"]["habilidades_mid"].count)
        conteo_habilidad_menos_solicitada_mid = x["mid"]["habilidades_mid"].count(habilidad_menos_solicitada_mid)
        promedio_mid = int(x["mid"]["suma_mid"]) / int(x["mid"]["contador_mid"])
        empresas_mid_con_mas_ofertas = max(x["mid"]["empresas_mid"], key=x["mid"]["empresas_mid"].count)
        conteo_empresas_mid_con_mas_ofertas = x["mid"]["empresas_mid"].count(empresas_mid_con_mas_ofertas)
        
        #senior
        habilidad_mas_solicitada_senior = max(x["senior"]["habilidades_senior"], key=x["senior"]["habilidades_senior"].count)
        conteo_habilidad_mas_solicitada_senior = x["senior"]["habilidades_senior"].count(habilidad_mas_solicitada_senior)
        habilidad_menos_solicitada_senior = min(x["senior"]["habilidades_senior"], key=x["senior"]["habilidades_senior"].count)
        conteo_habilidad_menos_solicitada_senior = x["senior"]["habilidades_senior"].count(habilidad_menos_solicitada_senior)
        promedio_senior = int(x["senior"]["suma_senior"]) / int(x["senior"]["contador_senior"])
        empresas_senior_con_mas_ofertas = max(x["senior"]["empresas_senior"], key=x["senior"]["empresas_senior"].count)
        conteo_empresas_senior_con_mas_ofertas = x["senior"]["empresas_senior"].count(empresas_senior_con_mas_ofertas)
        
        diccionario_final = {"Nombre Pais" : x["nombre pais"],
                            "Ciudad mas ofertas" : ciudad_con_mas_ofertas,
                             "Conteo" : conteo_ciudad_mas_ofertas,
                             "Numero ciudades" : numero_ciudades,
                             "Junior" : {"Habilidad mas solicitada" : habilidad_mas_solicitada_junior,
                                         "Conteo" : conteo_habilidad_mas_solicitada_junior,
                                         "Habilidad menos solicitada" : habilidad_menos_solicitada_junior,
                                         "Conteo" : conteo_habilidad_menos_solicitada_junior,
                                         "Promedio" : round(promedio_junior,3),
                                         "Empresa mas ofertas" : empresas_junior_con_mas_ofertas,
                                         "Conteo" : conteo_empresas_junior_con_mas_ofertas},
                             "Mid" : {"Habilidad mas solicitada" : habilidad_mas_solicitada_mid,
                                         "Conteo" : conteo_habilidad_mas_solicitada_mid,
                                         "Habilidad menos solicitada" : habilidad_menos_solicitada_mid,
                                         "Conteo" : conteo_habilidad_menos_solicitada_mid,
                                         "Promedio" : round(promedio_mid,3),
                                         "Empresa mas ofertas" : empresas_mid_con_mas_ofertas,
                                         "Conteo" : conteo_empresas_mid_con_mas_ofertas},
                             "Senior" : {"Habilidad mas solicitada" : habilidad_mas_solicitada_senior,
                                         "Conteo" : conteo_habilidad_mas_solicitada_senior,
                                         "Habilidad menos solicitada" : habilidad_menos_solicitada_senior,
                                         "Conteo" : conteo_habilidad_menos_solicitada_senior,
                                         "Promedio" : round(promedio_senior,3),
                                         "Empresa mas ofertas" : empresas_senior_con_mas_ofertas,
                                         "Conteo" : conteo_empresas_senior_con_mas_ofertas}
                             }
        
        lt.addLast(lista_final, diccionario_final)
        
   #print(sublista_de_las_N_paises)
    pais_con_mas_ofertas = lt.firstElement(sublista_de_las_N_paises)["nombre pais"]
    conteo_pais_con_mas_ofertas = lt.firstElement(sublista_de_las_N_paises)["cantidad ofertas"]
    
    return total_ofertas, pais_con_mas_ofertas, conteo_pais_con_mas_ofertas, lista_final
    
def buscar_habilidad_oferta(data_structs, jobs):

    lista_skills = data_structs["skills"]
    id_jobs = jobs["id"]
    #voy a usar búsqueda binaria
    top = lt.size(lista_skills)
    valor_ref = 0
    if(top != None):
        indice_inicial = 1
        while indice_inicial <= top:
            valor_ref = (indice_inicial + top) / 2
            valor_ref = int(valor_ref)
            elemento_buscado= lt.getElement(lista_skills, valor_ref)
            if(top != None):
                if elemento_buscado["id"] < id_jobs:
                    indice_inicial = valor_ref + 1
                elif elemento_buscado["id"] > id_jobs:
                    top = valor_ref - 1
                else:
                    if(elemento_buscado != None):
                        return elemento_buscado

def cmp_function_ordenar_paises_con_mas_ofertas_nombres(dato1,dato2):
    cantidad_1 = dato1["cantidad ofertas"]
    cantidad_2 = dato2["cantidad ofertas"]
    
    pais_1 = dato1["nombre pais"]
    pais_2 = dato2["nombre pais"]
    
    if(cantidad_1 > cantidad_2):
        return True
    elif(cantidad_1 == cantidad_2):
        if(pais_1 < pais_2):
            return True
        else:
            return False
    else:
        return False
    
    
   
    
    
    
    
    
def cmp_function_ordenar_ciudades_con_mas_ofertas_nombres(dato1, dato2):
    cantidad_1 = dato1["cantidad ofertas"]
    cantidad_2 = dato2["cantidad ofertas"]
    
    ciudad_1 = dato1["nombre ciudad"]
    ciudad_2 = dato2["nombre ciudad"]
    
    if(cantidad_1 > cantidad_2):
        return True
    elif(cantidad_1 == cantidad_2):
        if(ciudad_1 < ciudad_2):
            return True
        else:
            return False
    else:
        return False
    
    
    
    
 
        
        


def req_8(data_structs):
    """
    Función que soluciona el requerimiento 8
    """
    # TODO: Realizar el requerimiento 8
    pass


# Funciones utilizadas para comparar elementos dentro de una lista

def compare(data_1, data_2):
    """
    Función encargada de comparar dos datos
    """
    #TODO: Crear función comparadora de la lista
    pass

# Funciones de ordenamiento


def sort_carga_datos(lst):
    quk.sort(lst, cmp_ofertas_by_empresa_y_fecha)

def sort_criteria(data_1, data_2):
    """sortCriteria criterio de ordenamiento para las funciones de ordenamiento

    Args:
        data1 (_type_): _description_
        data2 (_type_): _description_

    Returns:
        _type_: _description_
    """
    #TODO: Crear función comparadora para ordenar
    pass

def ordenamiento(rta, control):
    if rta == 1:
        lista_ordenada = ins.sort(control, cmp_ofertas_by_empresa_y_fecha)
    elif rta == 2:
        lista_ordenada = merg.sort(control, cmp_ofertas_by_empresa_y_fecha)
    elif rta == 3:
        lista_ordenada = quk.sort(control, cmp_ofertas_by_empresa_y_fecha)
    elif rta == 4:
        lista_ordenada = se.sort(control, cmp_ofertas_by_empresa_y_fecha)
    elif rta == 5:
        lista_ordenada = sa.sort(control, cmp_ofertas_by_empresa_y_fecha)
    return lista_ordenada

def cmp_ofertas_by_empresa_y_fecha (oferta1, oferta2):
    """
    Devuelve verdadero (True) si la empresa de la oferta1 es menor que en la
    oferta2,
    en caso de que sean iguales se analiza la fecha de publicación de la oferta
    laboral,
    de lo contrario devuelva falso (False).
    Args:
    oferta1: información de la primera oferta laboral que incluye
    "company_name" y "published_at"
    oferta1: información de la segunda oferta laboral que incluye
    "company_name" y "published_at"
    """
    company_name1 = oferta1["company_name"]
    company_name2 = oferta2["company_name"]
    
    fecha_1 = oferta1["published_at"]
    fecha_2 = oferta2["published_at"]
    

    if(fecha_1 < fecha_2):
        return True
    elif(fecha_1 == fecha_2):
        if(company_name1 < company_name2):
            return True
        else:
            return False
    else:
        return False

def cmp_ofertas_by_pais_y_fecha(oferta1, oferta2):
    """
    Devuelve verdadero (True) si el país de la oferta1 es menor que en la
    oferta2,
    en caso de que sean iguales se analiza la fecha de publicación de la oferta
    laboral,
    de lo contrario devuelva falso (False).
    Args:
    oferta1: información de la primera oferta laboral que incluye
    "country_code" y "published_at"
    oferta1: información de la segunda oferta laboral que incluye
    "country_code" y "published_at"
    """
    country_code1 = oferta1["country_code"]
    country_code2 = oferta2["country_code"]
    
    fecha_1 = oferta1["published_at"]
    fecha_2 = oferta2["published_at"]
    

    if(country_code1 < country_code2):
        return True
    elif(country_code1 == country_code2):
        if(fecha_1 < fecha_2):
            return True
        else:
            return False
    else:
        return False

# def sort_criteria_published_at(oferta1, oferta2):
#     fecha_1 = oferta1["published_at"]
#     fecha_2 = oferta2["published_at"]
    
#     yymmdd = "%Y-%m-%dT%H:%M:%S.%fZ"
    
#     if(fecha_1 < fecha_2):
#         return True
#     else:
#         return False
    
    
    
    
    
def sort(data_structs):
    """
    Función encargada de ordenar la lista con los datos
    """
    #TODO: Crear función de ordenamiento
    pass