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
from DISClib.ADT import list as lt
from DISClib.ADT import stack as st
from DISClib.ADT import queue as qu
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.Algorithms.Sorting import insertionsort as ins
from DISClib.Algorithms.Sorting import selectionsort as se
from DISClib.Algorithms.Sorting import customsort as cus
from DISClib.Algorithms.Sorting import mergesort as merg
from DISClib.Algorithms.Sorting import quicksort as quk
from datetime import datetime
assert cf
"""
Se define la estructura de un catálogo de videos. El catálogo tendrá
dos listas, una para los videos, otra para las categorias de los mismos.
"""

# Construccion de modelos

def new_data_structs(tipo_estructura:str):
    """
    Inicializa las estructuras de datos del modelo. Las crea de
    manera vacía para posteriormente almacenar la información.
    """
    #Se crean los diccionarios vacios que van a almacenar la información
    #Se crea un diccionario con las llaves del archivo Jobs que corresponden a los datos que se van a cargar
    datos={
        "jobs": None,
        "skills": None,
        "employment": None,
        "multilocation": None
    }


    #Se crean las listas vacias que van a almacenar la información con la librería DISClib
    datos["jobs"] = lt.newList(tipo_estructura)
    datos["skills"] = lt.newList(tipo_estructura)
    datos["employment"] = lt.newList(tipo_estructura)
    datos["multilocation"] = lt.newList(tipo_estructura)
    return datos
# Funciones para agregar informacion al modelo

def add_jobs(lista_jobs_actual, data):
    """
    Función para agregar nuevos elementos a la lista
    Args:
    lista_jobs_actual: lista de datos actual de los trabajos unicamente
    data: datos a agregar leidos del archivo csv
    Returns:
    lista_jobs_actual: lista de datos actual de los trabajos con los datos agregados
    """
    #TODO: Crear una funcion para arreglar esto mejor
    #Se añaden los datos a las listas que corresponden
    lista_categorias=["title", "street", "city", "country_code", "address_text", "marker_icon", "workplace_type", "company_name", "company_url", "company_size", "experience_level", "published_at", "remote_interview", "open_to_hire_ukrainians", "id", "display_offer"]
    resultado_jobs = new_job(data[lista_categorias[0]], data[lista_categorias[1]], data[lista_categorias[2]], data[lista_categorias[3]], data[lista_categorias[4]], data[lista_categorias[5]], data[lista_categorias[6]], data[lista_categorias[7]], data[lista_categorias[8]], data[lista_categorias[9]], data[lista_categorias[10]], data[lista_categorias[11]], data[lista_categorias[12]], data[lista_categorias[13]], data[lista_categorias[14]], data[lista_categorias[15]])
    lt.addLast(lista_jobs_actual, resultado_jobs)
    return lista_jobs_actual
def add_skills(lista_skills_actual, data, tamanio):
    """
    Función para agregar nuevos elementos a la lista
    Args:
    lista_skills_actual: lista de datos actual de las habilidades unicamente
    data: datos a agregar leidos del archivo csv
    Returns:
    lista_skills_actual: lista de datos actual de las habilidades con los datos agregados
    """
    #Se añaden los datos a las listas que corresponden
    lista_categorias=["name", "level", "id"]
    if tamanio=="small" or tamanio=="medium" or tamanio=="large":
        resultado_skills = new_skill(data[0], data[1], data[2])
    else:
        resultado_skills = new_skill(data[lista_categorias[0]], data[lista_categorias[1]], data[lista_categorias[2]])
    lt.addLast(lista_skills_actual, resultado_skills)   
    return lista_skills_actual
def add_employments(lista_employments_actual, data, tamanio):
    
    lista_categorias=["type","id", "currency_salary", "salary_from", "salary_to"]
    if tamanio=="small" or tamanio=="medium" or tamanio=="large":
        resultado_employments = new_employment(data[0], data[1], data[2], data[3], data[4])
    else:
        resultado_employments=new_employment(data[lista_categorias[0]], data[lista_categorias[1]], data[lista_categorias[2]], data[lista_categorias[3]], data[lista_categorias[4]])
    lt.addLast(lista_employments_actual, resultado_employments)
    return lista_employments_actual
def add_multilocation(lista_multilocation, data, tamanio):
    """
    Función para agregar nuevos elementos a la lista
    Args:
    lista_multilocation: lista de datos actual de las habilidades unicamente
    data: datos a agregar leídos del archivo csv
    Returns:
    lista_multilocation: lista de datos actual de las habilidades con los datos agregados
    """
    #Se añaden los datos a las listas que corresponden
    lista_categorias=["city", "street", "id"]
    if tamanio=="small" or tamanio=="medium" or tamanio=="large":
            resultado_multilocation = new_multilocation(data[0], data[1], data[2])
    else:
        resultado_multilocation = new_multilocation(data[lista_categorias[0]], data[lista_categorias[1]], data[lista_categorias[2]])
    lt.addLast(lista_multilocation, resultado_multilocation)
    return lista_multilocation 

# Funciones para creacion de datos
def new_job(title, street, city, country_code, address_text, marker_icon, workplace_type, company_name, company_url, company_size, experience_level, published_at, remote_interview, open_to_hire_ukrainians, id, display_offer):      
    """
    Crea una nueva estructura para modelar los datos de los trabajos obtenidos en el CSV
    Args:
    Elementos de la estructura de datos de los trabajos obtenidos en el CSV
    Returns:
    Un diccionario con los datos de los trabajos obtenidos en el CSV
    """
    #Se crea un diccionario con las llaves del archivo Jobs que corresponden a los datos que se van a cargar
    return {'title':title,
             'street':street,
             'city':city,
             'country_code':country_code,
             'address_text':address_text,
             'marker_icon':marker_icon,
             'workplace_type':workplace_type,
                'company_name':company_name,
                'company_url':company_url,
                'company_size':company_size,
                'experience_level':experience_level,
                'published_at':published_at,
                'remote_interview':remote_interview,
                'open_to_hire_ukrainians':open_to_hire_ukrainians,
                'id':id,
                'display_offer':display_offer}
def new_skill(name, level, id):
    """
    Crea una nueva estructura para modelar los datos de las habilidades obtenidos en el CSV
    Args:
    Elementos de la estructura de datos de las habilidades obtenidos en el CSV
    Returns:
    Un diccionario con los datos de las habilidades obtenidos en el CSV
    """
    #Se crea un diccionario con las llaves del archivo Skills que corresponden a los datos que se van a cargar
    return {'name':name,
            'level':level,
            'id':id}

    # TODO: Crear la función para estructurar los datos
def new_employment(type,id, currency_salary, salary_from, salary_to):
    """
    Crea una nueva estructura para modelar los datos de los empleo obtenidos en el CSV
    Args:
    Elementos de la estructura de datos de los empleos obtenidos en el CSV
    Returns:
    Un diccionario con los datos de los empleos obtenidos en el CSV
    """
    
    return {'type':type,
            'id':id,
            'currency_salary':currency_salary,   
            'salary_from':salary_from,
            'salary_to':salary_to}
    
def new_multilocation(city, street, id):
    """
    Crea una nueva estructura para modelar los datos de las habilidades obtenidos en el CSV
    Args:
    Elementos de la estructura de datos de las habilidades obtenidos en el CSV
    Returns:
    Un diccionario con los datos de las habilidades obtenidos en el CSV
    """
    #Se crea un diccionario con las llaves del archivo Multilocation que corresponden a los datos que se van a cargar
    return {'city':city,
            'street':street,
            'id':id}
# Funciones de consulta
def new_data(lst, llave: str, info):
    """
    Crea una nueva estructura para modelar los datos
    """
    lst[llave] = info
    return lst

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

def req_1(data_structs,cod_pais,lvl_exp): # -> Si se separa por codigo de pais y nivel de experiencia despues se puede organizar para hacerlo mas rapido
    """
    Función que soluciona el requerimiento 1
    """
    # TODO: Realizar el requerimiento 1
    #Se obtiene el tamaño de la lista de trabajos y se crea una lista vacia para almacenar los trabajos que cumplen con el requerimiento
    size=lt.size(data_structs["jobs"])
    lista_nueva=lt.newList('ARRAY_LIST')
    #Se recorre la lista de trabajos y se añaden los trabajos que cumplen con el requerimiento a la lista de trabajos
    for i in range(1,size+1):
        if lt.getElement(data_structs["jobs"], i)["country_code"] == cod_pais and lt.getElement(data_structs["jobs"], i)["experience_level"] == lvl_exp:
                lt.addLast(lista_nueva, lt.getElement(data_structs["jobs"], i))
    #Se ordenan los trabajos de acuerdo a la fecha de publicación
    sorteado=merg.sort(lista_nueva, sort_dates)
    return sorteado

def req_2(data_structs, nombre_empresa, ciudad):
    """
    Función que soluciona el requerimiento 2
    """
    #Se obtiene el tamaño de la lista de trabajos y se crea una lista vacia para almacenar los indices de los trabajos que cumplen con el requerimiento
    size=lt.size(data_structs["jobs"])
    lista_nueva=lt.newList('ARRAY_LIST')
    
    #Se recorre la lista de trabajos y se añaden los indices de los trabajos que cumplen con el requerimiento a la lista de indices
    for i in range(1,size+1):
        if lt.getElement(data_structs["jobs"], i)["company_name"] == nombre_empresa and lt.getElement(data_structs["jobs"], i)["city"] == ciudad:
                lt.addLast(lista_nueva, lt.getElement(data_structs["jobs"], i))
    sorteado=merg.sort(lista_nueva, sort_dates)
    return sorteado


def cmp_req_3(data_1, data_2):
    if data_1["published_at"]==data_2["published_at"]:
        if data_1["company_name"]>data_2["company_name"]:
            return True
        else:
            return False
    elif data_1["published_at"]>data_2["published_at"]:
        return True
    else:
        return False

def req_3(data_structs, nombre_empresa, fecha_inicial, fecha_final):
    """
    Función que soluciona el requerimiento 3
    """
    # Contador para el número total de ofertas
    n = 0
    size=lt.size(data_structs["jobs"])
    lista_n=lt.newList('ARRAY_LIST')
    # Inicializar contadores para cada nivel de experiencia
    ofertas_junior = 0
    ofertas_mid = 0
    ofertas_senior = 0
    # Filtrar el DataFrame por empresa y rango de fechas
    for i in range(1,size+1):
        job= lt.getElement(data_structs["jobs"],i)        
        if (job["company_name"]) == nombre_empresa and fecha_inicial <= (job["published_at"]) <= fecha_final:
            lt.addLast(lista_n, job)
            n += 1
            # Calcular el número de ofertas por nivel de experticia
            if "junior" in job["experience_level"]:
                ofertas_junior += 1
            elif "mid" in job["experience_level"]:
                ofertas_mid += 1
            elif "senior" in job["experience_level"]:
                ofertas_senior += 1

    # Ordenar los datos por fecha y país (si es necesario)
    lista_n= merg.sort(lista_n, cmp_req_3)

    return {
        'total_ofertas': n,
        'ofertas_junior': ofertas_junior,
        'ofertas_mid': ofertas_mid,
        'ofertas_senior': ofertas_senior,
        'listado_ofertas': lista_n
    }

def req_4(data_structs,codigo,fecha_inicial,fecha_final):
    """
    Función que soluciona el requerimiento 4
    La meta es consultar las ofertas de trabajo publicadas en un país dado su código y un
    rango de fechas.

    """
    # TODO: Realizar el requerimiento 4
    size=lt.size(data_structs["jobs"])
    lista_nueva=lt.newList('ARRAY_LIST')
    lista_empresas={}
    lista_ciudades={}
    # total de ofertas en el país en el periodo de consulta
    for i in range(1,size+1):
        
        if lt.getElement(data_structs["jobs"], i)["country_code"] == codigo and lt.getElement(data_structs["jobs"], i)["published_at"] >=fecha_inicial and lt.getElement(data_structs["jobs"], i)["published_at"] <= fecha_final :
            lt.addLast(lista_nueva, lt.getElement(data_structs["jobs"], i))
            if  lt.getElement(data_structs["jobs"], i)["company_name"] not in lista_empresas :
                cantidad= 0
                lista_empresas[lt.getElement(data_structs["jobs"], i)["company_name"]]= 1
            else:
                cantidad+=1
                lista_empresas[lt.getElement(data_structs["jobs"], i)["company_name"]]= cantidad
            if lt.getElement(data_structs["jobs"], i)["city"] in lista_ciudades :
                lista_ciudades[lt.getElement(data_structs["jobs"], i)["city"]]["cantidad"]+=1
                lt.addLast(lista_ciudades[lt.getElement(data_structs["jobs"], i)["city"]]["lista"],lt.getElement (data_structs["jobs"], i))
            else:
                lista_temporal=lt.newList('ARRAY_LIST')
                lista_ciudades[lt.getElement(data_structs["jobs"], i)["city"]]={"cantidad":1,"lista":lista_temporal}
    # El listado de ofertas publicadas ordenados cronológicamente por fecha y nombre de la empresa
    sorteado=merg.sort(lista_nueva, cmp_ofertas_by_fecha_y_nombre)
    sizee=len(lista_empresas)
    totalc= len(lista_ciudades.keys())
    lista_ciudad = lt.newList('ARRAY_LIST')
    salarios={}
    for i in range(1,lt.size(data_structs["employment"])+1):
        if lt.getElement(data_structs["employment"], i)["salary_from"]!="" and int(lt.getElement(data_structs["employment"], i)["salary_to"])!="":
            salarios[lt.getElement(data_structs["employment"], i)["id"]]=int(lt.getElement(data_structs["employment"], i)["salary_from"])+int(lt.getElement(data_structs["employment"], i)["salary_to"])
        elif lt.getElement(data_structs["employment"], i)["salary_from"]!="":
            salarios[lt.getElement(data_structs["employment"], i)["id"]]=int(lt.getElement(data_structs["employment"], i)["salary_from"])
        elif lt.getElement(data_structs["employment"], i)["salary_to"]!="":
            salarios[lt.getElement(data_structs["employment"], i)["id"]]=int(lt.getElement(data_structs["employment"], i)["salary_to"])
        else:
            salarios[lt.getElement(data_structs["employment"], i)["id"]]=0
            
    for i in lista_ciudades:
        lt.addLast(lista_ciudad, {"city":i, "cantidad":lista_ciudades[i]["cantidad"],"lista":lista_ciudades[i]["lista"]}) 
    for i in range(1,lt.size(lista_ciudad)+1):
        average=0
        for j in lt.iterator(lt.getElement(lista_ciudad, i)["lista"]):
            if j["id"] in salarios:
                average+=salarios[j["id"]]
        if average!=0:
            average=average/lt.size(lt.getElement(lista_ciudad, i)["lista"])
            lt.getElement(lista_ciudad, i)["average"]=average
        else:
            lt.getElement(lista_ciudad, i)["average"]=0
    sorteado2=merg.sort(lista_ciudad, cmp_req_4)
        
    mayor = lt.firstElement(sorteado2)
    menor= lt.lastElement(sorteado2)
    return sorteado,sizee,totalc,mayor,menor

def cmp_req_4(oferta1, oferta2):
    if oferta1["cantidad"]==oferta2["cantidad"]:
        if oferta1["average"]<oferta2["average"]:
            if oferta1["city"]<oferta2["city"]:
                return True
            else:
                return False
        elif oferta1["average"]>oferta2["average"]:
            return True
        else:
            return False
    elif oferta1["cantidad"]>oferta2["cantidad"]:
        return True
    else:
        return False

def cmp_ofertas_by_fecha_y_nombre(oferta1, oferta2):
    """
    Devuelve verdadero (True) si la fecha de la oferta 1 es menor que en la oferta ,
    en caso de que sean iguales se analiza la empresa de la oferta laboral, de lo contrario devuelva Falso

    Args:
        oferta1: información de la primera oferta laboral que incluye "company_name" y "published_at"
        oferta2: información de la segunda oferta laboral que incluye "company_name" y "published_at"
    """
    nombre1= oferta1["company_name"].lower()
    nombre2= oferta2["company_name"].lower()
    fecha1= oferta1["published_at"]
    fecha2= oferta2["published_at"]
    return (fecha1<fecha2) or (fecha1 == fecha2 and nombre1 < nombre2)
        
def req_5(data_structs,ciudad,fecha_1,fecha_2):
    """
    Función que soluciona el requerimiento 5
    """
    #Se crea una lista vacia para almacenar los trabajos que cumplen con el requerimiento
    nueva_lista=lt.newList('ARRAY_LIST')
    
    #Se recorre la lista de trabajos y se añaden los trabajos que cumplen con el requerimiento a la lista de trabajos
    for i in lt.iterator(data_structs["jobs"]):
        if cmp_city_and_date(i, ciudad, fecha_1, fecha_2):
            lt.addLast(nueva_lista, i)
    nueva_lista=merg.sort(nueva_lista, cmp_fecha_nombre)
    #Se crea un diccionario vacio para almacenar las empresas y la cantidad de trabajos que tienen
    top={}
    salarios={}
    
    #Se recorre la lista de trabajos y se añaden las empresas y la cantidad de trabajos que tienen a la lista de trabajos
    for i in lt.iterator(nueva_lista):
        if i["company_name"] in top:
            top[i["company_name"]]["cantidad"]+=1
            lt.addLast(top[i["company_name"]]["id"], i["id"])
        else:
            nueva_lista2=lt.newList('ARRAY_LIST')
            lt.addLast(nueva_lista2, i["id"])
            top[i["company_name"]]={"cantidad":1,"id":nueva_lista2}
            
    #Se reestructura la lista de trabajos para que sea mas facil de ordenar
    lista_top=lt.newList('ARRAY_LIST')
    for i in top:
        lt.addLast(lista_top, {"company_name":i,"cantidad":top[i]["cantidad"],"id":top[i]["id"]})
        
    #Se recorre la lista de salario y se añaden los salarios a la lista de salarios con el id del trabajo como llave
    for i in range(1,lt.size(data_structs["employment"])+1):
        #Si el salario no esta vacio se añade a la lista de salarios
        if lt.getElement(data_structs["employment"], i)["salary_from"]!="" and lt.getElement(data_structs["employment"], i)["salary_to"]!="":
            salarios[lt.getElement(data_structs["employment"], i)["id"]]=int(lt.getElement(data_structs["employment"], i)["salary_from"])+int(lt.getElement(data_structs["employment"], i)["salary_to"])/2
        elif lt.getElement(data_structs["employment"], i)["salary_from"]!="":
            salarios[lt.getElement(data_structs["employment"], i)["id"]]=int(lt.getElement(data_structs["employment"], i)["salary_from"])
        elif lt.getElement(data_structs["employment"], i)["salary_to"]!="":
            salarios[lt.getElement(data_structs["employment"], i)["id"]]=int(lt.getElement(data_structs["employment"], i)["salary_to"])
        #Sino, se añade un 0 a la lista de salarios
        else:
            salarios[lt.getElement(data_structs["employment"], i)["id"]]=0
    #Se recorre la lista de trabajos y se añaden los promedios de salarios a la lista de trabajos
    for i in range(1,lt.size(lista_top)+1):
        average=0
        for j in lt.iterator(lt.getElement(lista_top, i)["id"]):
            if j in salarios:
                average+=salarios[j]
        if average!=0:
            average=average/lt.getElement(lista_top, i)["cantidad"]
            lt.getElement(lista_top, i)["average"]=average
        else:
            lt.getElement(lista_top, i)["average"]=0
    #Se crea una lista vacia para eliminar los ID y falicitar el ordenamiento
    lista_final=lt.newList('ARRAY_LIST')
    for x in lt.iterator(lista_top):
            del x["id"]
            lt.addLast(lista_final, x)
    #Se ordena la lista de trabajos de acuerdo a la cantidad de trabajos y el promedio de salarios
    lista_final=merg.sort(lista_final, cmp_nuevo)
    return nueva_lista,lista_final
    # TODO: Realizar el requerimiento 5
    
def req_6(data_structs,num_ciudades, nivel_exp, fecha_ini, fecha_fin, codigo_pais):
    """    
    Función que soluciona el requerimiento 6
    """
    #Se crea una lista vacia para almacenar los trabajos que cumplen con los requerimientos
    lista_nueva=lt.newList('ARRAY_LIST')
    #Se hace un diccionario vacio para almacenar ciudades junto con sus cantidades
    dict_completo={}
    #Se hace un diccionario vacio para almacenar empresas junto con sus cantidades
    dict_ciudad_cantidad={}
    #Si el codigo del pais es diferente de None se recorre la lista de trabajos de acuerdo al pais 
    datos_employments=data_structs["employment"]
    #RESPUESTA 1
    cantidad_ofertas=0
    
    if codigo_pais!=None:
        for i in lt.iterator(data_structs["jobs"]):
            #Si el codigo del pais, el nivel de experiencia y la fecha de publicación del trabajo cumplen con los requerimientos se añade a la lista de trabajos
            if i["country_code"]==codigo_pais and i["experience_level"]==nivel_exp and fecha_a_iso(i["published_at"])>=fecha_ini and fecha_a_iso(i["published_at"])<=fecha_fin:
                lt.addLast(lista_nueva, i)
                cantidad_ofertas+=1
                if i["city"] not in dict_ciudad_cantidad:
                    dict_ciudad_cantidad[i["city"]]=1
                else:
                    dict_ciudad_cantidad[i["city"]]+=1

                #Si la ciudad del trabajo esta en el diccionario de ciudades se añade uno a la cantidad de trabajos en esa ciudad
    else:
        for i in lt.iterator(data_structs["jobs"]):
            if i["experience_level"]==nivel_exp and fecha_a_iso(i["published_at"])>=fecha_ini and fecha_a_iso(i["published_at"])<=fecha_fin:
                lt.addLast(lista_nueva, i)
                cantidad_ofertas+=1
                if i["city"] not in dict_ciudad_cantidad:
                    dict_ciudad_cantidad[i["city"]]=1
                else:
                    dict_ciudad_cantidad[i["city"]]+=1
    dict_salarios = {}
    print(dict_ciudad_cantidad["Warszawa"])

    for i in lt.iterator(datos_employments):
            if i["salary_from"] != "" and i["salary_to"] != "":
                dict_salarios[i["id"]] = (int(i["salary_from"]) + int(i["salary_to"])) / 2

    lista_ciudad_cantidad=lt.newList('ARRAY_LIST')
    
    for i in dict_ciudad_cantidad:
        lt.addLast(lista_ciudad_cantidad, {"city":i,"cantidad":dict_ciudad_cantidad[i]})
    sorted_list = merg.sort(lista_ciudad_cantidad, cmp_ciudades)
    sublista_ciudad_cantidad =lt.newList('ARRAY_LIST')
    for i in range(num_ciudades+1, lt.size(sorted_list)+1):
        lt.addLast(sublista_ciudad_cantidad, lt.getElement(sorted_list, i))
    lista_ciudad_cantidad=sublista_ciudad_cantidad
    
    for i in lt.iterator(lista_nueva):
        if i["city"] not in dict_completo:
            dict_completo[i["city"]] = {"cantidad": 1, "empresa": {}}
        else:
            dict_completo[i["city"]]["cantidad"] += 1

        if i["company_name"] not in dict_completo[i["city"]]["empresa"]:
            lista_temporal = lt.newList('ARRAY_LIST')
            lt.addLast(lista_temporal, i)
            dict_completo[i["city"]]["empresa"][i["company_name"]] = {"cantidad": 1, "lista": lista_temporal}
        else:
            dict_completo[i["city"]]["empresa"][i["company_name"]]["cantidad"] += 1
            lt.addLast(dict_completo[i["city"]]["empresa"][i["company_name"]]["lista"], i)
    
    for i in lt.iterator(lista_ciudad_cantidad):
        if i["city"] in dict_completo:
            del dict_completo[i["city"]]
            
    for i in dict_completo:
        salario_promedio_ciudad = 0
        contador_ciudad = 0
        for j in dict_completo[i]["empresa"]:
            salario_promedio_id = 0
            contador_id = 0
            for k in lt.iterator(dict_completo[i]["empresa"][j]["lista"]):
                if k["id"] in dict_salarios:
                    contador_id += 1
                    salario_promedio_id += dict_salarios[k["id"]]
            if contador_id > 0:
                salario_promedio_id = salario_promedio_id / contador_id
                salario_promedio_ciudad += salario_promedio_id
                contador_ciudad += 1
                dict_completo[i]["empresa"][j]["salario_promedio"] = salario_promedio_id

        if contador_ciudad > 0:
            salario_promedio_ciudad = salario_promedio_ciudad / contador_ciudad
            dict_completo[i]["salario_promedio"] = salario_promedio_ciudad
    
    cantidad_empresas = 0
    for i in dict_completo:
        for j in dict_completo[i]["empresa"]:
            if dict_completo[i]["empresa"][j]["cantidad"] > 0:
                cantidad_empresas += 1
    promedio_salario_ofertas = 0
    for i in dict_completo:
        promedio_salario_ofertas += dict_completo[i]["salario_promedio"]
    promedio_salario_ofertas = promedio_salario_ofertas / len(dict_completo)
    
    lista_retorno=lt.newList('ARRAY_LIST')
    for i in range(1, num_ciudades+1):
        cantidad_trabajos=0
        informacion_mas_trabajos=None
        for j in dict_completo[lt.getElement(sorted_list, i)["city"]]["empresa"]:
            if dict_completo[lt.getElement(sorted_list, i)["city"]]["empresa"][j]["cantidad"]>0:
                if cantidad_trabajos<dict_completo[lt.getElement(sorted_list, i)["city"]]["empresa"][j]["cantidad"]:
                    cantidad_trabajos=dict_completo[lt.getElement(sorted_list, i)["city"]]["empresa"][j]["cantidad"]
                    informacion_mas_trabajos=j
        tope_alto=0
        informacion_alto={}
        for j in dict_completo[lt.getElement(sorted_list, i)["city"]]["empresa"]:
                for k in lt.iterator(dict_completo[lt.getElement(sorted_list, i)["city"]]["empresa"][j]["lista"]):
                    if k["id"] in dict_salarios:
                        if tope_alto<dict_salarios[k["id"]]:
                            tope_alto=dict_salarios[k["id"]]
                            informacion_alto=k
        tope_bajo=100000
        informacion_bajo={}
        for j in dict_completo[lt.getElement(sorted_list, i)["city"]]["empresa"]:
                for k in lt.iterator(dict_completo[lt.getElement(sorted_list, i)["city"]]["empresa"][j]["lista"]):
                    if k["id"] in dict_salarios:
                        if tope_bajo>dict_salarios[k["id"]] and dict_salarios[k["id"]]!=0:
                            tope_bajo=dict_salarios[k["id"]]
                            informacion_bajo=k
        lt.addLast(lista_retorno, {"ciudad":lt.getElement(sorted_list, i)["city"],
                                   "cantidad":dict_completo[lt.getElement(sorted_list, i)["city"]]["cantidad"],
                                   "salario_promedio":dict_completo[lt.getElement(sorted_list, i)["city"]]["salario_promedio"],
                                   "empresas":len(dict_completo[lt.getElement(sorted_list, i)["city"]]["empresa"]),
                                   "mayor_cantidad":informacion_mas_trabajos,
                                   "empresa_alta":informacion_alto,
                                   "salario_alto":tope_alto,
                                   "empresa_baja":informacion_bajo,
                                   "salario_bajo":tope_bajo})
    retorno={"total_ciudades":len(dict_completo),
             "total_empresas":cantidad_empresas,
             "total_ofertas":cantidad_ofertas,
             "promedio_salario":promedio_salario_ofertas,
             "ciudad_mas_ofertas":(lt.getElement(sorted_list, 1)["city"],dict_completo[lt.getElement(sorted_list, 1)["city"]]["cantidad"]),
             "ciudad_menos_ofertas":(lt.getElement(sorted_list, num_ciudades)["city"],dict_completo[lt.getElement(sorted_list, num_ciudades)["city"]]["cantidad"]),
             "lista_ciudades":lista_retorno}
    return retorno

def cmp_ciudades(data_1, data_2):
    if data_1["cantidad"]==data_2["cantidad"]:
        if data_1["city"]<data_2["city"]:
            return True
        else:
            return False
    elif data_1["cantidad"]>data_2["cantidad"]:
        return True
    else:
        return False

    

def req_7(data_structs,num_paises, fecha_ini, fecha_fin):
    """
    Función que soluciona el requerimiento 7
    """
    #======FILTRADO Y DIVISION DE DATOS=======
    #Obtener los datos de los trabajos entre las fechas dadas
    datos = data_structs["jobs"]
    paises = lt.newList('ARRAY_LIST')
    dict_pais = {"paises": {}}
    #Se itera la lista de trabajos por medio de un iterador
    for i in lt.iterator(datos):
        #Si la fecha de publicación del trabajo esta entre las fechas dadas se añade a la lista de trabajos
        if fecha_a_iso(i["published_at"]) >= fecha_ini and fecha_a_iso(i["published_at"]) <= fecha_fin:
            lt.addLast(paises, i)
            #Si el pais del trabajo esta en el diccionario de paises se añade uno a la cantidad de trabajos en ese pais
            if i["country_code"] in dict_pais["paises"]:
                dict_pais["paises"][i["country_code"]]["cantidad"] += 1
                #Si la ciudad del trabajo esta en el diccionario de ciudades se añade uno a la cantidad de trabajos en esa ciudad
                if i["city"] in dict_pais["paises"][i["country_code"]]["ciudades"]:
                    dict_pais["paises"][i["country_code"]]["ciudades"][i["city"]] += 1
                #Sino, se añade la ciudad al diccionario de ciudades
                else:
                    dict_pais["paises"][i["country_code"]]["ciudades"][i["city"]] = 1
            #Sino, se añade el pais al diccionario de paises
            else:
                dict_pais["paises"][i["country_code"]] = {"cantidad": 1, "ciudades": {i["city"]: 1}}
    
    #Si el dato ingresado es mayor al tamaño de la lista de paises se iguala el dato al tamaño de la lista de paises
    if num_paises>len(dict_pais["paises"]):
        num_paises=len(dict_pais["paises"])-1

    #Se crea una lista vacia para almacenar los paises en forma de diccionario con el codigo del pais y la cantidad de trabajos
    lista_paises=lt.newList('ARRAY_LIST')

    #Separar los datos en lista con numero de ofertas por ciudad con una estructura de diccionario {"country_code":PL,"cantidad":1}
    for i in dict_pais["paises"]:
        lt.addLast(lista_paises, {"country_code":i,"cantidad":dict_pais["paises"][i]["cantidad"]})
        
    #Se ordena la lista de paises de acuerdo a la cantidad de trabajos y se obtiene la sublista con el numero de paises ingresado
    lista_paises=lt.subList(merg.sort(lista_paises, cmp_paises),1,num_paises)
    
    #Se crea una lista vacia para almacenar las ciudades en forma de diccionario {"city":Warsaw,"cantidad":1}
    lista_ciudades=lt.newList('ARRAY_LIST')
    for i in lt.iterator(lista_paises):
        for j in dict_pais["paises"][i["country_code"]]["ciudades"]:
            lt.addLast(lista_ciudades, {"city":j,"cantidad":dict_pais["paises"][i["country_code"]]["ciudades"][j]})
    
    #Se ordena la lista de ciudades de acuerdo a la cantidad de trabajos
    lista_ciudades=merg.sort(lista_ciudades, cmp_ciudades)
    
    #Se crea unas listas vacias para almacenar los trabajos de acuerdo al nivel de experiencia
    lista_junior=lt.newList('ARRAY_LIST')
    lista_mid=lt.newList('ARRAY_LIST')
    lista_senior=lt.newList('ARRAY_LIST')
    
    #Separar los datos en listas de acuerdo al nivel de experiencia
    for i in lt.iterator(paises):
        #Se recorre la lista de paises recortada
        for j in lt.iterator(lista_paises):
            #Si el nivel de experiencia del trabajo es junior y el codigo del pais es igual al codigo del pais de la lista de paises se añade a la lista de trabajos junior
            if i["experience_level"]=="junior" and j["country_code"]==i["country_code"]:
                lt.addLast(lista_junior, i)
            #Si el nivel de experiencia del trabajo es mid y el codigo del pais es igual al codigo del pais de la lista de paises se añade a la lista de trabajos mid
            elif i["experience_level"]=="mid" and j["country_code"]==i["country_code"]:
                lt.addLast(lista_mid, i)
            #Si el nivel de experiencia del trabajo es senior y el codigo del pais es igual al codigo del pais de la lista de paises se añade a la lista de trabajos senior
            else:
                if j["country_code"]==i["country_code"]:
                    lt.addLast(lista_senior, i)
                    
    #====CONVERSION DE SKILLS A DICCIONARIO====                       
    datos_skills=data_structs["skills"]
    #Crear un diccionario con el id como llave y otro diccionario con el nombre de la habilidad y el nivel como valor
    dict_skills_id={}
    #Se itera la lista de habilidades por medio de un iterador
    for i in lt.iterator(datos_skills):
        #Se crea una lista temporal para almacenar los nombres y los niveles de las habilidades
        lista_tem_id=lt.newList('ARRAY_LIST')
        #Si el id ya esta en el diccionario se añade la habilidad a la lista de habilidades
        if i["id"] in dict_skills_id:
            lt.addLast(dict_skills_id[i["id"]],{"name":i["name"],"level":i["level"]})
        #Sino, se añade el id al diccionario y se añade la habilidad a la lista de habilidades
        else:
            lt.addLast(lista_tem_id,{"name":i["name"],"level":i["level"]})
            dict_skills_id[i["id"]]=lista_tem_id
            
    #====CONVERSION DE MULTILOCATION A DICCIONARIO===
    datos_multilocation=data_structs["multilocation"]
    #Crear un diccionario con el id como llave y otro diccionario con la ciudad y la cantidad de trabajos como valor
    dict_multilocation={}
    for i in lt.iterator(datos_multilocation):
        lista_tem_id=lt.newList('ARRAY_LIST')
        if i["id"] in dict_multilocation:
            lt.addLast(dict_multilocation[i["id"]],i["city"])
        else:
            lt.addLast(lista_tem_id,i["city"])
            dict_multilocation[i["id"]]=lista_tem_id
    #===CREACION INFORMACION PARA MOSTRAR====
    
    #====JUNIOR=====
    #Se crean las variables para almacenar los datos de los trabajos junior
    #Se cuentan el numero de habilidades
    conteo_habilidades_junior=0
    #Se obtienen las habilidades más y menos solicitadas
    top_habilidades_junior={}
    #Se obtiene una sumatoria de los niveles de las habilidades para despues dividir sobre la cantidad de habilidades
    nivel_promedio_junior=0
    #Se obtienen las empresas más y menos solicitadas
    dict_empresa_junior={}
    #Se obtienen las empresas con trabajos con diferentes ID
    empresas_sede_junior_id={}
    #Se obtienen las empresas que ya se han añadido
    empresas_sede_junior={}
    #Se añade un contador a las empresas de nivel junior
    contador_empresas_skills_junior=0
    
    #Se recorre toda la lista junior
    for i in range(1,lt.size(lista_junior)+1):
        #Se obtiene el elemento del diccionario de habilidades con el id del trabajo y se itera sobre la lista resultante
        for j in lt.iterator(dict_skills_id[lt.getElement(lista_junior, i)["id"]]):
            #Se cuenta una habilidad
            conteo_habilidades_junior+=1
            #Si la habilidad ya esta en el diccionario se añade uno a la cantidad de veces que se ha solicitado
            if j["name"] in top_habilidades_junior:
                top_habilidades_junior[j["name"]]+=1
            #Sino, se añade la habilidad al diccionario
            else:
                top_habilidades_junior[j["name"]]=1
            #Se suma el nivel de la habilidad al nivel promedio
            nivel_promedio_junior+=int(j["level"])
            
        #Si la empresa ya esta en el diccionario se añade uno a la cantidad de veces que se ha solicitado
        if lt.getElement(lista_junior, i)["company_name"] in dict_empresa_junior:
            dict_empresa_junior[lt.getElement(lista_junior, i)["company_name"]]+=1
        #Sino, se añade la empresa al diccionario
        else:
            dict_empresa_junior[lt.getElement(lista_junior, i)["company_name"]]=1
            
        #Por a busqueda del ID en el diccionario de multilocation se itera en la lista de multilocation resultante
        for j in lt.iterator(dict_multilocation[lt.getElement(lista_junior, i)["id"]]):
            #Si la empresa no esta en el diccionario de IDs y la empresa no esta en el diccionario de empresas se añade la empresa al diccionario de empresas
            if j not in empresas_sede_junior_id and lt.getElement(lista_junior, i)["company_name"] not in empresas_sede_junior:
                empresas_sede_junior[j]=lt.getElement(lista_junior, i)["company_name"]
                empresas_sede_junior_id[j]=lt.getElement(lista_junior, i)["id"]
                #Se añade 1 al contador de empresas
                contador_empresas_skills_junior+=1
                
    #Se obtiene el promedio de los niveles de las habilidades
    nivel_promedio_junior=nivel_promedio_junior/conteo_habilidades_junior
    
    #=======MID=======
    #Se crean las variables para almacenar los datos de los trabajos mid
    #Se cuentan el numero de habilidades
    conteo_habilidades_mid=0
    #Se obtienen las habilidades más y menos solicitadas
    top_habilidades_mid={}
    #Se obtiene una sumatoria de los niveles de las habilidades para despues dividir sobre la cantidad de habilidades
    nivel_promedio_mid=0
    #Se obtienen las empresas más y menos solicitadas
    dict_empresa_mid={}
    #Se obtienen las empresas con trabajos con diferentes ID
    empresas_sede_mid_id={}
    #Se obtienen las empresas que ya se han añadido
    empresas_sede_mid={}
    #Se añade un contador a las empresas de nivel mid
    contador_empresas_skills_mid=0
    
    #Se recorre toda la lista mid
    for i in range(1,lt.size(lista_mid)+1):
        #Se obtiene el elemento del diccionario de habilidades con el id del trabajo y se itera sobre la lista resultante
        for j in lt.iterator(dict_skills_id[lt.getElement(lista_mid, i)["id"]]):
            #Se cuenta una habilidad
            conteo_habilidades_mid+=1
            #Si la habilidad ya esta en el diccionario se añade uno a la cantidad de veces que se ha solicitado
            if j["name"] in top_habilidades_mid:
                top_habilidades_mid[j["name"]]+=1
            #Sino, se añade la habilidad al diccionario
            else:
                top_habilidades_mid[j["name"]]=1
            nivel_promedio_mid+=int(j["level"])	
            
        #Si la empresa ya esta en el diccionario se añade uno a la cantidad de veces que se ha solicitado
        if lt.getElement(lista_mid, i)["company_name"] in dict_empresa_mid:
            dict_empresa_mid[lt.getElement(lista_mid, i)["company_name"]]+=1
        #Sino, se añade la empresa al diccionario
        else:
            dict_empresa_mid[lt.getElement(lista_mid, i)["company_name"]]=1
            
        #Se recorre la lista de multilocation resultante de obtener el ID
        for j in lt.iterator(dict_multilocation[lt.getElement(lista_mid, i)["id"]]):
            #Si no esta en el diccionario de IDs y no esta en el diccionario de empresas se añade la empresa a ambos
            if j not in empresas_sede_mid_id and lt.getElement(lista_mid, i)["company_name"] not in empresas_sede_mid:
                empresas_sede_mid[j]=lt.getElement(lista_mid, i)["company_name"]
                empresas_sede_mid_id[j]=lt.getElement(lista_mid, i)["id"]
                #Se añade 1 al contador de empresas
                contador_empresas_skills_mid+=1
    #Se calcula el promedio con la sumatoria de los niveles de las habilidades y la cantidad de habilidades
    nivel_promedio_mid=nivel_promedio_mid/conteo_habilidades_mid
    
    #=======SENIOR=======
    #Contar el numero de habilidades de nivel senior
    conteo_habilidades_senior=0
    #Obtener las habilidades mas y menos solicitadas
    top_habilidades_senior={}
    #Obtener una sumatoria de los niveles de las habilidades para despues dividir sobre la cantidad de habilidades
    nivel_promedio_senior=0
    #Obtener las empresas mas y menos solicitadas
    dict_empresa_senior={}
    #Obtener las empresas con trabajos con diferentes ID
    empresas_sede_senior_id={}
    #Obtener las empresas que ya se han añadido
    empresas_sede_senior={}
    #Añadir un contador a las empresas de nivel senior
    contador_empresas_skills_senior=0
    #Recorrer toda la lista senior y obtener los datos
    for i in range(1,lt.size(lista_senior)+1):
        #Obtener el elemento del diccionario de habilidades con el id del trabajo y recorrer la lista resultante
        for j in lt.iterator(dict_skills_id[lt.getElement(lista_senior, i)["id"]]):
            #Contar una habilidad de nivel senior al contador
            conteo_habilidades_senior+=1
            #Si la habilidad ya esta en el diccionario se añade uno a la cantidad de veces que se ha solicitado
            if j["name"] in top_habilidades_senior:
                top_habilidades_senior[j["name"]]+=1
            #Sino, se añade la habilidad al diccionario
            else:
                top_habilidades_senior[j["name"]]=1
            nivel_promedio_senior+=int(j["level"])
        #Si la empresa ya esta en el diccionario se añade uno a la cantidad de veces que se ha solicitado
        if lt.getElement(lista_senior, i)["company_name"] in dict_empresa_senior:
            dict_empresa_senior[lt.getElement(lista_senior, i)["company_name"]]+=1
        #Sino, se añade la empresa al diccionario de empresas
        else:
            dict_empresa_senior[lt.getElement(lista_senior, i)["company_name"]]=1
        #Se recorre la lista de multilocation resultante de obtener el ID en el diccionario de multilocation
        for j in lt.iterator(dict_multilocation[lt.getElement(lista_senior, i)["id"]]):
            #Si no esta en el diccionario de IDs y no esta en el diccionario de empresas se añade la empresa a ambos
            if j not in empresas_sede_senior_id and lt.getElement(lista_senior, i)["company_name"] not in empresas_sede_senior:
                empresas_sede_senior[j]=lt.getElement(lista_senior, i)["company_name"]
                empresas_sede_senior_id[j]=lt.getElement(lista_senior, i)["id"]
                #Se añade 1 al contador de empresas
                contador_empresas_skills_senior+=1
    #Se calcula el promedio con la sumatoria de los niveles de las habilidades y la cantidad de habilidades
    nivel_promedio_senior=nivel_promedio_senior/conteo_habilidades_senior
    
    #Conversion Diccionarios a Listas DISCLib
    #Se crean las listas vacias para almacenar los datos de los diccionarios
    top_habilidades_junior_lista=lt.newList('ARRAY_LIST')
    top_habilidades_mid_lista=lt.newList('ARRAY_LIST')
    top_habilidades_senior_lista=lt.newList('ARRAY_LIST')
    empresa_junior_lista=lt.newList('ARRAY_LIST')
    empresa_mid_lista=lt.newList('ARRAY_LIST')
    empresa_senior_lista=lt.newList('ARRAY_LIST')
    #Por cada elemento en el diccionario se añade a la lista de habilidades
    for i in top_habilidades_junior:
        lt.addLast(top_habilidades_junior_lista, {"habilidad":i,"cantidad":top_habilidades_junior[i]})
    for i in top_habilidades_mid:
        lt.addLast(top_habilidades_mid_lista, {"habilidad":i,"cantidad":top_habilidades_mid[i]})
    for i in top_habilidades_senior:
        lt.addLast(top_habilidades_senior_lista, {"habilidad":i,"cantidad":top_habilidades_senior[i]})
    for i in dict_empresa_junior:
        lt.addLast(empresa_junior_lista, {"empresa":i,"cantidad":dict_empresa_junior[i]})
    for i in dict_empresa_mid:
        lt.addLast(empresa_mid_lista, {"empresa":i,"cantidad":dict_empresa_mid[i]})
    for i in dict_empresa_senior:
        lt.addLast(empresa_senior_lista, {"empresa":i,"cantidad":dict_empresa_senior[i]})
    #Se ordena las listas de acuerdo a la cantidad de trabajos por medio de merge sort
    top_habilidades_junior_lista=merg.sort(top_habilidades_junior_lista, cmp_top)
    top_habilidades_mid_lista=merg.sort(top_habilidades_mid_lista, cmp_top)
    top_habilidades_senior_lista=merg.sort(top_habilidades_senior_lista, cmp_top)
    empresa_junior_lista=merg.sort(empresa_junior_lista, cmp_empresa)
    empresa_mid_lista=merg.sort(empresa_mid_lista, cmp_empresa)
    empresa_senior_lista=merg.sort(empresa_senior_lista, cmp_empresa)
    
    #Se crea un diccionario con el id como llave y otro diccionario con el nombre de la habilidad y el nivel como valor
    retorno={"junior":{"conteo_habilidades":conteo_habilidades_junior,
                      "habilidad_mas_solicitada":(lt.getElement(top_habilidades_junior_lista, 1)["habilidad"],lt.getElement(top_habilidades_junior_lista, 1)["cantidad"]),
                      "habilidad_menos_solicitada":(lt.getElement(top_habilidades_junior_lista, lt.size(top_habilidades_junior_lista))["habilidad"],lt.getElement(top_habilidades_junior_lista, lt.size(top_habilidades_junior_lista))["cantidad"]),
                      "nivel_promedio":nivel_promedio_junior,
                      "conteo_empresas":lt.size(empresa_junior_lista),
                      "empresa_mas_solicitada":(lt.getElement(empresa_junior_lista, 1)["empresa"],lt.getElement(empresa_junior_lista, 1)["cantidad"]),
                      "empresa_menos_solicitada":(lt.getElement(empresa_junior_lista, lt.size(empresa_junior_lista))["empresa"],lt.getElement(empresa_junior_lista, lt.size(empresa_junior_lista))["cantidad"]),
                      "conteo_empresas_skills":contador_empresas_skills_junior
                      },
                "mid":{"conteo_habilidades":conteo_habilidades_mid,
                        "habilidad_mas_solicitada":(lt.getElement(top_habilidades_mid_lista, 1)["habilidad"],lt.getElement(top_habilidades_mid_lista, 1)["cantidad"]),
                        "habilidad_menos_solicitada":(lt.getElement(top_habilidades_mid_lista, lt.size(top_habilidades_mid_lista))["habilidad"],lt.getElement(top_habilidades_mid_lista, lt.size(top_habilidades_mid_lista))["cantidad"]),
                        "nivel_promedio":nivel_promedio_mid,
                        "conteo_empresas":lt.size(empresa_mid_lista),
                        "empresa_mas_solicitada":(lt.getElement(empresa_mid_lista, 1)["empresa"],lt.getElement(empresa_mid_lista, 1)["cantidad"]),
                        "empresa_menos_solicitada":(lt.getElement(empresa_mid_lista, lt.size(empresa_mid_lista))["empresa"],lt.getElement(empresa_mid_lista, lt.size(empresa_mid_lista))["cantidad"]),
                        "conteo_empresas_skills":contador_empresas_skills_mid
                        },
                "senior":{"conteo_habilidades":conteo_habilidades_senior,
                            "habilidad_mas_solicitada":(lt.getElement(top_habilidades_senior_lista, 1)["habilidad"],lt.getElement(top_habilidades_senior_lista, 1)["cantidad"]),
                            "habilidad_menos_solicitada":(lt.getElement(top_habilidades_senior_lista, lt.size(top_habilidades_senior_lista))["habilidad"],lt.getElement(top_habilidades_senior_lista, lt.size(top_habilidades_senior_lista))["cantidad"]),
                            "nivel_promedio":nivel_promedio_senior,
                            "conteo_empresas":lt.size(empresa_senior_lista),
                            "empresa_mas_solicitada":(lt.getElement(empresa_senior_lista, 1)["empresa"],lt.getElement(empresa_senior_lista, 1)["cantidad"]),
                            "empresa_menos_solicitada":(lt.getElement(empresa_senior_lista, lt.size(empresa_senior_lista))["empresa"],lt.getElement(empresa_senior_lista, lt.size(empresa_senior_lista))["cantidad"]),
                            "conteo_empresas_skills":contador_empresas_skills_senior
                            },
            "otros":{"total_ofertas":lt.size(lista_junior)+lt.size(lista_mid)+lt.size(lista_senior),
                     "num_ciudades":lt.size(lista_ciudades),
                     "pais_mas_ofertas":((lt.getElement(lista_paises, 1)["country_code"]),lt.getElement(lista_paises, 1)["cantidad"]),  
                     "ciudad_mas_ofertas":((lt.getElement(lista_ciudades, 1)["city"]),lt.getElement(lista_ciudades, 1)["cantidad"])}
    }
            
    return retorno


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

    
def sort_dates(fecha_1:int, fecha_2:int):
    """
    Función encargada de comparar dos fechas
    """
    fechas1=fecha_1["published_at"]
    fecha_int1=date_to_unix(str(fechas1))
    fechas2=fecha_2["published_at"]
    fecha_int2=date_to_unix(str(fechas2))
    return fecha_int1>fecha_int2
    
def date_to_unix(fecha:str):
    """
    Función que convierte una fecha en formato "%Y-%m-%dT%H:%M:%S.%fZ" a un entero en tiempo unix
    """
    
    timestamp_dt = datetime.strptime(fecha, "%Y-%m-%dT%H:%M:%S.%fZ")
    unix_timestamp = timestamp_dt.timestamp()
    timestamp_int = int(unix_timestamp)
    return timestamp_int
def cmp_ofertas_by_empresa_y_fecha(oferta1, oferta2):
    """
    Devuelve verdadero (True) si la empresa de la oferta 1 es menor que en la oferta ,
    en caso de que sean iguales se analiza la fecha de publicación de la oferta laboral, de lo contrario devuelva dalso

    Args:
        oferta1: información de la primera oferta laboral que incluye "company_name" y "published_at"
        oferta2: información de la segunda oferta laboral que incluye "company_name" y "published_at"
    """
    nombre1= oferta1["company_name"].lower()
    nombre2= oferta2["company_name"].lower()
    fecha1= oferta1["published_at"]
    fecha2= oferta2["published_at"]
    return (nombre1<nombre2) or (nombre1 == nombre2 and fecha1 < fecha2)
# ------------Requerimiento 5----------------
def fecha_a_iso(fecha:str):
    """
    Función que convierte una fecha en formato "%Y-%m-%dT%H:%M:%S.%fZ" a un entero en tiempo unix
    """
    return fecha+"T00:00:00.000Z"

def cmp_nuevo(data_1, data_2):
    if data_1["cantidad"]==data_2["cantidad"]:
        if data_1["average"]==data_2["average"]:
            if data_1["company_name"]<data_2["company_name"]:
                return True
            else:
                return False
        elif data_1["average"]>data_2["average"]:
            return True
        else:
            return False
    elif data_1["cantidad"]>data_2["cantidad"]:
        return True
    else:
        return False

            
def cmp_fecha_nombre(oferta1:dict, oferta2:dict):
    if oferta1["published_at"]>oferta2["published_at"]:
        return True
    elif oferta1["published_at"]==oferta2["published_at"]:
        if oferta1["company_name"]>oferta2["company_name"]:
            return True
        else:
            return False
def cmp_city_and_date(oferta1:dict, ciudad:str, fecha_1:str, fecha_2:str):
    """
    El listado de ofertas publicadas ordenadas cronológicamente por fecha y nombre de la empresa (v.gr.
    Para dos ofertas con la misma fecha, el orden lo decide la empresa de forma alfabética)

    Args:
        oferta1 (dict): _description_
        oferta2 (dict): _description_
    """
    fecha1_datos= fecha_a_iso(oferta1["published_at"])
    nombre1= oferta1["city"].lower()
    if fecha_1<=fecha1_datos<=fecha_2 and nombre1==ciudad.lower():
        return True
#---------------Requerimiento 7----------------
def cmp_paises(data_1, data_2):
    if data_1["cantidad"]>data_2["cantidad"]:
        return True
    else:
        return False
def cmp_top(data_1, data_2):
    if data_1["cantidad"]==data_2["cantidad"]:
        if data_1["habilidad"]<data_2["habilidad"]:
            return True
        else:
            return False
    elif data_1["cantidad"]>data_2["cantidad"]:
        return True
    else:
        return False
def cmp_empresa(data_1, data_2):
    if data_1["cantidad"]==data_2["cantidad"]:
        if data_1["empresa"]<data_2["empresa"]:
            return True
        else:
            return False
    elif data_1["cantidad"]>data_2["cantidad"]:
        return True
    else:
        return False
def cmp_ciudades(data_1, data_2):
    if data_1["cantidad"]==data_2["cantidad"]:
        if data_1["city"]<data_2["city"]:
            return True
        else:
            return False
    elif data_1["cantidad"]>data_2["cantidad"]:
        return True
    else:
        return False
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
def sublista(datos,cantidad):
    return lt.subList(datos,0,cantidad+1)
# -----------------------------------------
# Funciones de ordenamiento
# -----------------------------------------
def ordenamiento_selection(datos):
    datos=se.sort(datos, cmp_ofertas_by_empresa_y_fecha)
    return datos
def ordenamiento_insertion(datos):
    datos=ins.sort(datos, cmp_ofertas_by_empresa_y_fecha)
    return datos
def ordenamiento_shell(datos):
    datos=sa.sort(datos, cmp_ofertas_by_empresa_y_fecha)
    return datos
def ordenamiento_merge(datos):
    datos=merg.sort(datos, cmp_ofertas_by_empresa_y_fecha)
    return datos
def ordenamiento_quick(datos):
    datos=quk.sort(datos, cmp_ofertas_by_empresa_y_fecha)
    return datos
def ordenamiento_tim(datos):
    datos=cus.sort(datos, cmp_ofertas_by_empresa_y_fecha)
    return datos



