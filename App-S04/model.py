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
import New_Functions as nf
import tabulate 
assert cf
import Sorts as srt
from datetime import datetime


"""
Se define la estructura de un catálogo de videos. El catálogo tendrá
dos listas, una para los videos, otra para las categorias de los mismos.
"""

# Construccion de modelos


def new_data_structs():
    """
    Inicializa las estructuras de datos del modelo. Las crea de
    manera vacía para posteriormente almacenar la información.
    """
    #TODO: Inicializar las estructuras de datos
    catalog = {'jobs': None,
               'skills': None,
               'employment_types': None,
               'multilocation': None}
    
    catalog['jobs'] = nf.newList()
    catalog['skills'] = nf.newList()
    catalog['employment_types'] = nf.newList()
    catalog['multilocation'] = nf.newList()
           
    return catalog


# Funciones para agregar informacion al modelo


def add_jobs(lista, data):
    nf.addLast(lista, data)

def add_skills(lista, data):
    nf.addLast(lista, data)

def add_employment_types(lista, data):
    nf.addLast(lista, data)
    
def add_multilocations(lista, data):
    nf.addLast(lista, data)

def new_jobs():
    pass

def new_skills():
    pass

def new_employment_types():
    pass

def new_multilocations():
    pass


def get_jobs(data_structs, id):
    pass

def get_skills(data_structs, id):
    pass

def get_employment_types(data_structs, id):
    pass

def get_multilocations(data_structs, id):
    pass



def data_size(lista):
    """
    Retorna el tamaño de la lista de datos
    """
    #TODO: Crear la función para obtener el tamaño de una lista
    return nf.get_size(lista)

def req_1(data_structs, codigo, nivel_experiencia):
    lista = nf.newList()
    contador = 0 #solo según el nivel de experiencia
    for i in data_structs["model"]["jobs"]["elements"]:
        if i["experience_level"] == nivel_experiencia:
            contador += 1
            if i["country_code"] == codigo:
                nf.addLast(lista, i)
    srt.MergeSort(lista, srt.fecha_empresa)
    return lista, contador
    """
    Función que soluciona el requerimiento 1
    """


def req_2(data_structs, company_name, ciudad):
    """
    Función que soluciona el requerimiento 2
    """
    lista = nf.newList()
    for i in data_structs["model"]["jobs"]["elements"]:
        if i["company_name"] == company_name and i["city"] == ciudad:
            nf.addLast(lista, i)
    srt.MergeSort(lista, srt.fecha_empresa)
    return lista, nf.get_size(lista)
    # TODO: Realizar el requerimiento 2

def req_3(data_structs, company_name , rango_abajo, rango_arriba):
    """
    Función que soluciona el requerimiento 3
    """
    # Ana
    lista = nf.newList()
    num_ofertas_junior = 0
    num_ofertas_mid = 0
    num_ofertas_senior = 0
    rango_abajo = datetime.strptime(rango_abajo, "%Y-%m-%d")
    rango_arriba = datetime.strptime(rango_arriba, "%Y-%m-%d")
    data_structs = data_structs["model"]["jobs"]
    
    for i in data_structs["elements"]:
        fecha= i["published_at"]
        fecha = datetime.strptime(fecha[:10], "%Y-%m-%d")
        if i["company_name"] == company_name and rango_abajo < fecha < rango_arriba:
                nf.addLast(lista, i)
                if i["experience_level"] == "senior":
                    num_ofertas_senior += 1
                elif i["experience_level"] == "mid":
                    num_ofertas_mid += 1
                elif i["experience_level"] == "junior":
                    num_ofertas_junior += 1
    srt.MergeSort(lista, srt.fecha_pais)
        
    return lista, num_ofertas_junior, num_ofertas_mid, num_ofertas_senior


def req_4(control, country_code, start_date, end_date):
    """
        Función que soluciona el requerimiento 4
        Consultar las ofertas que se publicaron en un país durante un periodo de tiempo.

        Argumentos:
            control Dict: Diccionario con la información de las ofertas de trabajo.
            country_code str: Código del país.
            start_date str: Fecha de inicio del periodo.
            end_date str: Fecha de fin del periodo.

        Retorna:
            jobs_found list: Lista de ofertas encontradas.
            qty_jobs_found int: Cantidad de ofertas encontradas.
            qty_companies int: Cantidad de empresas que publicaron ofertas.
            qty_cities int: Cantidad de ciudades con ofertas.
            city_most_offers str: Ciudad con más ofertas.
            city_less_offers str: Ciudad con menos ofertas.
            qty_city_most_offers int: Cantidad de ofertas en la ciudad con más ofertas.
            qty_city_less_offers int: Cantidad de ofertas en la ciudad con menos ofertas.
    """

    # Se extraen los datos necesarios del diccionario de control
    jobs = control["model"]["jobs"]
    jobs = srt.MergeSort(jobs, srt.fecha_empresa) # Se ordenan las ofertas por fecha y país
    
    # Se convierten las fechas a objetos datetime
    start_date = datetime.strptime(start_date, "%Y-%m-%d")
    end_date = datetime.strptime(end_date, "%Y-%m-%d")

    # Se inicializan las variables necesarias
    companies = set()
    cities_with_jobs = {}
    jobs_found = nf.newList("ARRAY_LIST")

    # Se recorren las ofertas de trabajo para encontrar las que cumplen con los criterios de búsqueda de país y fecha
    for job in nf.iterator(jobs):
        job["published_at"] = job["published_at"].replace("T", " ").replace("Z", "")
        published_at = datetime.strptime(job["published_at"], "%Y-%m-%d %H:%M:%S.%f")

        if job["country_code"] == country_code and published_at >= start_date and published_at <= end_date:
            nf.addLast(jobs_found, job) # Se añade la oferta a la lista de ofertas encontradas
            companies.add(job["company_name"]) # Se añade la empresa a la lista de empresas (si ya está no se añade)

            # Se añade la ciudad a la lista de ciudades con ofertas (si ya está se suma 1 a la cantidad de ofertas)
            cities_with_jobs[job["city"]] = cities_with_jobs.get(job["city"], 0) + 1

    # Se encuentran las ciudades con más y menos ofertas
    city_most_offers = max(cities_with_jobs, key = cities_with_jobs.get)
    qty_city_most_offers = cities_with_jobs[city_most_offers]

    city_less_offers = min(cities_with_jobs, key=cities_with_jobs.get)
    qty_city_less_offers = cities_with_jobs[city_less_offers]

    jobs_found = [job for job in nf.iterator(jobs_found)] # Se convierte la lista de ofertas a una lista de Python

    to_return = (
                    jobs_found,
                    len(jobs_found),
                    len(companies),
                    len(cities_with_jobs),
                    city_most_offers,
                    city_less_offers,
                    qty_city_most_offers,
                    qty_city_less_offers
                )

    return to_return


def req_5(data_structs, nombre, fecha_in, fecha_fin):
    """
    Función que soluciona el requerimiento 5
    """
    #Funciona bien pero al tabular se demora mucho y no se ven todos los datos
    fecha_in = datetime.strptime(fecha_in, "%Y-%m-%d")
    fecha_fin = datetime.strptime(fecha_fin, "%Y-%m-%d")
    
    en_rango=nf.newList()
    en_ciudad=nf.newList()
    empresas= {}
    
    for i in range(nf.get_size(data_structs)): 
        oferta= nf.getElement(data_structs, i)
        fecha= datetime.strptime(oferta["published_at"], '%Y-%m-%dT%H:%M:%S.%fZ')
        oferta["published_at"] = fecha.strftime("%Y-%m-%d")
        if fecha>= fecha_in and fecha<= fecha_fin:
            nf.addFirst(en_rango,oferta)
            if oferta['city']==nombre:
                nf.addFirst(en_ciudad,oferta)
                empresa= oferta['company_name']
                if empresa not in empresas:
                    empresas[empresa]=1
                else:
                    empresas[empresa]+=1
    
    total_empresas= len(empresas)
    
    mayor=0
    e_mayor= None
    menor=2
    e_menor= None
    
    #TODO: revisar lo de Si al ordenar por número de ofertas dos o más ciudades presentan el mismo número, ordene las ciudades por el promedio de salario de las ofertas hechas
    for empresa in empresas:
        if empresas[empresa]>mayor:
            mayor= empresas[empresa]
            e_mayor= empresa
        if empresas[empresa]<menor:
            menor= empresas[empresa]
            e_menor= empresa
    
    srt.TimSort(en_ciudad,srt.fecha_empresa)
    
    total_ofertas= nf.get_size(en_ciudad)
    if nf.get_size(en_ciudad)>6:
        p_u= nf.first_last(en_ciudad)
    else:
        p_u=en_ciudad
    para_tabular= nf.newList()
    for oferta in p_u['elements']:
        fila= nf.newList()
        nf.addLast(fila,oferta["published_at"])
        nf.addLast(fila,oferta['title'] )
        nf.addLast(fila,oferta['company_name'] )
        nf.addLast(fila,oferta['workplace_type'] )
        nf.addLast(fila,oferta['company_size'] )
        nf.addLast(para_tabular, fila['elements'])

    headers = ['Fecha de publicación','Título de la oferta', 'Nombre de la empresa', 'Tipo de lugar de trabajo', 'Tamaño de la empresa']
    
    return total_ofertas, total_empresas, e_mayor, mayor, e_menor, menor, (para_tabular, headers)

def req_6(data_structs, nivel_experiencia, fecha_in, fecha_fin, country_code):
    fecha_in = datetime.strptime(fecha_in, "%Y-%m-%d")
    fecha_fin = datetime.strptime(fecha_fin, "%Y-%m-%d")
    ciudades_nombres = nf.newList()
    ciudades_info = nf.newList()
    empresas = nf.newList()
    ofertas_publicadas = 0
    salarios_total = nf.newList() #Solo cuando nos dan el país
    salarios_promedio_total = 0
    conteo = 0
    
    jobs = data_structs["model"]["jobs"]
    employment_types = data_structs["model"]["employment_types"]
    
    for oferta in jobs["elements"]:
        primero = jobs["elements"][0]
        fecha= oferta["published_at"]
        fecha = datetime.strptime(fecha[:10], "%Y-%m-%d")
            
        if (oferta["experience_level"] == nivel_experiencia) and (fecha_in <= fecha <= fecha_fin) and (country_code == oferta["country_code"] or country_code == None):
            ofertas_publicadas += 1
            #nombres = ciudad, total_ofertas = #ofertas, total_salario= #ofertas con salario, salario= sumatoria todos los salarios
            #empresas = lista de empresas, conteo_empresas = lista de #veces que aparece cada empresa, mejor_oferta= mejor oferta, peor_oferta=peor oferta, ubi_mejor_oferta = posicion mejor oferta
            #ubi_peor_oferta = posicion peor oferta, mejor empresa = lista con información de nombre y #apariciones de la mejor empresa
            info = {"nombre": 0, "total_ofertas": 0, "total_salario": 0, "salario": 0, "empresas": nf.newList(), "conteo_empresas": nf.newList(), "mejor_oferta": primero, "peor_oferta": primero, "ubi_mejor_oferta": 0, "ubi_peor_oferta": 0, "mejor_empresa": nf.newList()}
            nf.addLast(info["mejor_empresa"], 0)
            nf.addLast(info["mejor_empresa"], 0)
            #datos base
            if nf.isPresent(ciudades_nombres, oferta["city"]) == None:
                nf.addLast(ciudades_nombres, oferta["city"])
                nf.addLast(ciudades_info, info)
                posicion = nf.get_size(ciudades_info)-1
                ciudades_info["elements"][posicion]["nombre"] = oferta["city"]
                ciudades_info["elements"][posicion] = info
                ciudades_info["elements"][posicion]["mejor_oferta"] = oferta
                ciudades_info["elements"][posicion]["peor_oferta"] = oferta
                ciudades_info["elements"][posicion]["ubi_mejor_oferta"] = conteo
                ciudades_info["elements"][posicion]["ubi_peor_oferta"] = conteo
                lugar_ciudad = posicion
            else:
                lugar_ciudad = nf.isPresent(ciudades_info, oferta["city"], "nombre")
                
            if nf.isPresent(empresas, oferta["company_name"]) == None:
                nf.addLast(empresas, oferta["company_name"])    
                
            lugar_empresa = nf.isPresent(ciudades_info["elements"][lugar_ciudad]["empresas"], oferta["company_name"])
            if lugar_empresa == None:
                nf.addLast(ciudades_info["elements"][lugar_ciudad]["empresas"], oferta["company_name"])
                nf.addLast(ciudades_info["elements"][lugar_ciudad]["conteo_empresas"], 1)
            else:
                ciudades_info["elements"][lugar_ciudad]["conteo_empresas"]["elements"][lugar_empresa] += 1
                
            if (employment_types["elements"][conteo]['salary_to'] != "Unknown") and (employment_types["elements"][conteo]['salary_from'] != "Unknown"):
                valor = (int(employment_types["elements"][conteo]['salary_to']) + int(employment_types["elements"][conteo]['salary_from']))/2
            else:
                valor = None
                
            if country_code != None:
                nf.addLast(salarios_total, valor)
            ciudades_info["elements"][lugar_ciudad]["total_ofertas"] += 1
            
            if valor != None:
                ciudades_info["elements"][lugar_ciudad]["salario"] += valor
            if nf.getElement(employment_types, conteo)["salary_to"] != "Unknown":
                ciudades_info["elements"][lugar_ciudad]["total_salario"] += 1
            
            #conseguir la mejor y peor oferta en cada caso
            if nf.getElement(employment_types, ciudades_info["elements"][lugar_ciudad]["ubi_mejor_oferta"])["salary_to"] != "Unknown":
                valor_mejor_oferta = (int(nf.getElement(employment_types, ciudades_info["elements"][lugar_ciudad]["ubi_mejor_oferta"])["salary_to"]) + int(nf.getElement(employment_types, ciudades_info["elements"][lugar_ciudad]["ubi_mejor_oferta"])["salary_from"]))/2
            else:
                valor_mejor_oferta = 0
                
            if nf.getElement(employment_types, ciudades_info["elements"][lugar_ciudad]["ubi_peor_oferta"])["salary_to"] != "Unknown":
                valor_peor_oferta = (int(nf.getElement(employment_types, ciudades_info["elements"][lugar_ciudad]["ubi_peor_oferta"])["salary_to"]) + int(nf.getElement(employment_types, ciudades_info["elements"][lugar_ciudad]["ubi_peor_oferta"])["salary_from"]))/2
            else:
                valor_peor_oferta = 1000000000000000000000000000000000

            if valor == None:
                pass
            elif valor > valor_mejor_oferta:
                ciudades_info["elements"][lugar_ciudad]["mejor_oferta"] = oferta
                ciudades_info["elements"][lugar_ciudad]["ubi_mejor_oferta"] = conteo
            elif valor < valor_peor_oferta:
                ciudades_info["elements"][lugar_ciudad]["peor_oferta"] = oferta
                ciudades_info["elements"][lugar_ciudad]["ubi_peor_oferta"] = conteo
                
        conteo += 1
                         
    for i in salarios_total["elements"]:
        if i != None:
            salarios_promedio_total += i
    if salarios_promedio_total != 0:
        salarios_promedio_total /= nf.get_size(salarios_total)
        
    ciudad_mayor_cantidad = nf.newList() 
    ciudad_menor_cantidad = nf.newList() 
      
    ubicacion_lista = 0  
    #cambiar el salario de todas las ciudades
    for ciudad in ciudades_info["elements"]:
        if ciudad["salario"] != 0:
            ciudad["salario"] = ciudad["salario"]/ciudad["total_salario"]
            
        valor_empresa = 0
        ubi_empresa = 0
        ubi_importante = 0
        #encontrar la empresa más importante por ciudad
        for i in (ciudad["conteo_empresas"]["elements"]):
            if i > valor_empresa:
                valor_empresa = i
                ubi_importante = ubi_empresa
            ubi_empresa += 1  
            
        nf.changeInfo(ciudades_info["elements"][ubicacion_lista]["mejor_empresa"], 1, valor_empresa)
        nf.changeInfo(ciudades_info["elements"][ubicacion_lista]["mejor_empresa"], 0, ciudad["empresas"]["elements"][ubi_importante])
        ubicacion_lista += 1

    #en caso de no tener ningúna ciudad se establen las variables necesarias
    if nf.get_size(ciudades_nombres) == 0:
        nf.addLast(ciudad_mayor_cantidad, "Ninguna")
        nf.addLast(ciudad_mayor_cantidad, 0)
        nf.addLast(ciudad_menor_cantidad, "Ninguna")
        nf.addLast(ciudad_menor_cantidad, 0)
        
    srt.MergeSort(ciudades_info, srt.organizar_ciudad)
    ubicacion_lista = 0
    #después de la organización de las ciudades se encuentra la de mayor y menor # de empleos
    if nf.get_size(ciudades_nombres) != 0:
        nf.addLast(ciudad_mayor_cantidad, ciudades_info["elements"][0]["nombre"])
        nf.addLast(ciudad_mayor_cantidad, ciudades_info["elements"][0]["total_ofertas"])
        nf.addLast(ciudad_menor_cantidad, ciudades_info["elements"][nf.get_size(ciudades_info)-1]["nombre"])
        nf.addLast(ciudad_menor_cantidad, ciudades_info["elements"][nf.get_size(ciudades_info)-1]["total_ofertas"])
        
    #retorno -> #ciudades, #empresas, #ofertas_publicadas, salarios_promedio_total, ciudad_mayor_cantidad, ciudad_menor_cantidad, diccionario ciudades_info
    return nf.get_size(ciudades_nombres), nf.get_size(empresas), ofertas_publicadas, salarios_promedio_total, ciudad_mayor_cantidad, ciudad_menor_cantidad, ciudades_info


def req_7(data_structs, n, fecha_in, fecha_fin):
    """
    Función que soluciona el requerimiento 7
    """
    fecha_in = datetime.strptime(fecha_in, "%Y-%m-%d")
    fecha_fin = datetime.strptime(fecha_fin, "%Y-%m-%d")
    
    en_rango = nf.newList()
    jobs = data_structs['jobs']
    skills = data_structs['skills']
    multilocations = data_structs['multilocation']
    
    paises = {}
    ciudades = {}
    id_compania = {}
    habilidades = {'senior': {}, 'mid': {}, 'junior': {}}
    niveles = {'senior': nf.newList() , 'mid': nf.newList(), 'junior': nf.newList()}
    empresas_por_nivel = {'senior': {}, 'mid': {}, 'junior': {}}
    sedes_por_nivel= {'senior': {}, 'mid': {}, 'junior': {}}

    for i in range(nf.get_size(jobs)): 
        job = nf.getElement(jobs, i)
        #Verifica que este dentro del rango de fechas
        fecha = datetime.strptime(job["published_at"], '%Y-%m-%dT%H:%M:%S.%fZ')
        if fecha >= fecha_in and fecha <= fecha_fin:
            pais = job['country_code'] 
            #Verifica que el pais es en el diccionario paises
            if pais not in paises:
                paises[pais] = 0
            if pais in paises: 
                paises[pais] += 1
                ciudad = job['city']
                if ciudad not in ciudades:
                    ciudades[ciudad] = 0
                ciudades[ciudad] += 1
                nf.addLast(en_rango, job)
                empresa= job['company_name']
                empresa_id = job['id']
                id_compania[empresa_id] = empresa
                nivel = job['experience_level']
                habilidades_nivel = habilidades[nivel]
                if empresa_id not in empresas_por_nivel[nivel]:
                    empresas_por_nivel[nivel][empresa_id] = 0
                empresas_por_nivel[nivel][empresa_id] += 1
                
    tuplas_paises= nf.newList()
    
    for pais, conteo in paises.items():
        tupla= (pais,conteo)
        nf.addLast(tuplas_paises,tupla)
    
    srt.ShellSort_tupla(tuplas_paises,srt.comparacion_diccionarios)
    
    for i in range(nf.get_size(skills)):
        skill = skills['elements'][i]
        job_id = skill['id']
        for nivel in habilidades:
            habilidades_nivel = habilidades[nivel]
            if job_id in id_compania:
                empresa_id = job_id
                habilidad = skill['name']
                if habilidad not in habilidades_nivel:
                    habilidades_nivel[habilidad] = 0
                habilidades_nivel[habilidad] += 1
                nf.addLast(niveles[nivel], int(skill['level']))
    
    
    total_ofertas = nf.get_size(en_rango)
    total_ciudades = len(ciudades)
    
    mayor = 0
    p_mayor = None
    cc_mayor = 0
    c_mayor = None
    
    for pais in paises:
        if paises[pais] > mayor:
            mayor = paises[pais]
            p_mayor = pais
            
    for ciudad in ciudades:
        if ciudades[ciudad] > cc_mayor:
            cc_mayor = ciudades[ciudad]
            c_mayor = ciudad
    
    total_habilidades= {'senior': [], 'mid': [], 'junior': []}
    promedio_nivel_minimo= {'senior': [], 'mid': [], 'junior': []}
    habilidad_mas_solicitada= {'senior': [], 'mid': [], 'junior': []}
    conteo_habilidad_mas_solicitada= {'senior': [], 'mid': [], 'junior': []}
    habilidad_menos_solicitada= {'senior': [], 'mid': [], 'junior': []}
    conteo_habilidad_menos_solicitada= {'senior': [], 'mid': [], 'junior': []}
    total_empresas_ofertas= {'senior': [], 'mid': [], 'junior': []} 
    conteo_mas_ofertas= {'senior': [], 'mid': [], 'junior': []} 
    empresa_con_mas_ofertas= {'senior': [], 'mid': [], 'junior': []} 
    empresa_con_menos_ofertas= {'senior': [], 'mid': [], 'junior': []} 
    conteo_menos_ofertas= {'senior': [], 'mid': [], 'junior': []} 
    total_sedes_por_nivel= {'senior': [], 'mid': [], 'junior': []}
    
    sedes={}
    for i in range(nf.get_size(multilocations)): 
        oferta = multilocations['elements'][i]
        if oferta['id'] not in sedes:
            sedes[oferta['id']]=0
        sedes[oferta['id']]+=1
    
    for nivel in habilidades:
        habilidades_nivel = habilidades[nivel]
        if habilidades_nivel:
            total_habilidades[nivel] = len(habilidades_nivel)
            
            # Encontrar la habilidad más solicitada
            habilidad_mas_solicitada[nivel] = None
            conteo_habilidad_mas_solicitada[nivel] = 0
            for habilidad, conteo in habilidades_nivel.items():
                if conteo > conteo_habilidad_mas_solicitada[nivel]:
                    habilidad_mas_solicitada[nivel] = habilidad
                    conteo_habilidad_mas_solicitada[nivel] = conteo
            
            # Encontrar la habilidad menos solicitada
            habilidad_menos_solicitada[nivel] = None
            conteo_habilidad_menos_solicitada[nivel] = float('inf')
            for habilidad, conteo in habilidades_nivel.items():
                if conteo < conteo_habilidad_menos_solicitada[nivel]:
                    habilidad_menos_solicitada[nivel] = habilidad
                    conteo_habilidad_menos_solicitada[nivel] = conteo
            
            # Calcular el promedio del nivel mínimo requerido
            promedio_nivel_minimo[nivel] = sum(niveles[nivel]['elements']) / nf.get_size(niveles[nivel])
            print(promedio_nivel_minimo[nivel])
            # Calcular el total de empresas que ofrecen trabajos de este nivel
            total_empresas_ofertas[nivel] = len(empresas_por_nivel[nivel])
    
            # Encontrar la empresa con más ofertas
            empresa_con_mas_ofertas[nivel] = None
            conteo_mas_ofertas[nivel] = 0
            for empresa_id, conteo in empresas_por_nivel[nivel].items():
                if conteo > conteo_mas_ofertas[nivel]:
                    empresa_con_mas_ofertas[nivel] = id_compania[empresa_id]
                    conteo_mas_ofertas[nivel] = conteo
            
            # Encontrar la empresa con menos ofertas
            empresa_con_menos_ofertas[nivel] = None
            conteo_menos_ofertas[nivel] = float('inf')
            for empresa_id, conteo in empresas_por_nivel[nivel].items():
                if conteo < conteo_menos_ofertas[nivel]:
                    empresa_con_menos_ofertas[nivel] = id_compania[empresa_id]
                    conteo_menos_ofertas[nivel] = conteo
                    
            #Encontrar número de empresas que publicaron una oferta en este nivel que tienen una o más sedes
            for empresa_id, conteo in empresas_por_nivel[nivel].items(): 
                if empresa_id not in sedes_por_nivel[nivel]:
                    sedes_por_nivel[nivel][empresa_id]= 0
                sedes_por_nivel[nivel][empresa_id]= sedes[empresa_id]
            total_sedes_por_nivel[nivel]= len(sedes_por_nivel[nivel])
            
    para_tabular = nf.newList()

    fila = nf.newList()
    for nivel in habilidades:
        print(total_habilidades)
        nf.addLast(fila, total_habilidades[nivel])
    nf.addLast(para_tabular, fila['elements'])
    
    fila1 = nf.newList()    
    for nivel in habilidades:
        nf.addLast(fila1, habilidad_mas_solicitada[nivel])
    nf.addLast(para_tabular, fila1['elements'])
   
    fila2 = nf.newList()
    for nivel in habilidades:
        nf.addLast(fila2, conteo_habilidad_mas_solicitada[nivel])
    nf.addLast(para_tabular, fila2['elements'])
    
    fila3 = nf.newList()
    for nivel in habilidades:
        nf.addLast(fila3, habilidad_menos_solicitada[nivel])
    nf.addLast(para_tabular, fila3['elements'])
    
    fila4 = nf.newList()
    for nivel in habilidades:
        nf.addLast(fila4, conteo_habilidad_menos_solicitada[nivel])
    nf.addLast(para_tabular, fila4['elements'])
    
    fila5 = nf.newList()
    for nivel in habilidades:
        nf.addLast(fila5, promedio_nivel_minimo[nivel])
    nf.addLast(para_tabular, fila5['elements'])
    
    fila6 = nf.newList()
    for nivel in habilidades:
        nf.addLast(fila6, total_empresas_ofertas[nivel])
    nf.addLast(para_tabular, fila6['elements'])
    
    fila7 = nf.newList()
    for nivel in habilidades:
        nf.addLast(fila7, " "  + empresa_con_mas_ofertas[nivel] +  ':' +  str(conteo_mas_ofertas[nivel]))
    nf.addLast(para_tabular, fila7['elements'])
    
    fila8 = nf.newList()
    for nivel in habilidades:
        nf.addLast(fila8, " " + empresa_con_menos_ofertas[nivel] + ':' + str(conteo_menos_ofertas[nivel]))
    nf.addLast(para_tabular, fila8['elements'])
    
    fila9 = nf.newList()
    for nivel in habilidades:
        nf.addLast(fila9, total_sedes_por_nivel[nivel])
    nf.addLast(para_tabular, fila9['elements'])
    row_index = ['Conteo habilidades solicitadas', 'Habilidad más solicitada', 'Conteo habilidad más solicitada', 'Habilidad menos solicitada', 'Conteo habilidad menos solicitada', 'Promedio nivel mínimo', 'Empresas con ofertas de este nivel', 'Empresa con más ofertas y conteo', 'Empresa con menos ofertas y conteo', 'Empresas con una o más sedes']
    headers= ['Senior', 'Mid', 'Junior']
    return total_ofertas, total_ciudades, p_mayor, mayor, c_mayor, cc_mayor, (para_tabular, headers, row_index)    

def req_8(data_structs):
    """
    Función que soluciona el requerimiento 8
    """
    # TODO: Realizar el requerimiento 8
    pass