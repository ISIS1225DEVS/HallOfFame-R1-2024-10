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
from DISClib.ADT import list as lt


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""
globalSufijo = "small"

def new_controller():
    """
    Crea una instancia del modelo
    """
    #TODO: Llamar la función del modelo que crea las estructuras de datos
    control = {
        'model': None
    }
    control['model'] = model.new_data_structs()
    return control
    
def changeGlobalTAD(selection):
    
    if selection == 1:
        model.changeGlobalTAD("ARRAY_LIST")
    else:
        model.changeGlobalTAD("SINGLE_LINKED")
    
def changeGlobalSort(selection):
    model.changeGlobalSort(selection)
    
def cambiarTamañoMuestra(sufijo):
    global globalSufijo
    globalSufijo = sufijo
    

# Funciones para la carga de datos

def load_data(control):
    """
    Carga los datos del reto
    """
    # TODO: Realizar la carga de datos
    start_time = get_time()
    catalog = control['model']
    employments_types = loadEmployments_types(catalog)
    jobs = loadJobs(catalog)
    multilocations = loadMultilocations(catalog)
    skills = loadSkills(catalog)
    model.sort_jobs(catalog["jobs"])
    global globalSufijo
    print(globalSufijo)
    end_time = get_time()
    time= delta_time(start_time, end_time)
    return catalog, time
    

def mascaraLoadData(catalog):
    i=0
    
    file1 = cf.data_dir + 'data/'+globalSufijo+'-employments_types.csv'
    input_file1 = list(csv.DictReader(open(file1, encoding='utf-8'), delimiter=";"))
    model.recurLoadData(catalog["model"]["employments_types"],i,len(input_file1),input_file1)
    
    file2 = cf.data_dir + 'data/'+globalSufijo+'-jobs.csv'
    input_file2 = list(csv.DictReader(open(file2, encoding='utf-8'), delimiter=";"))
    model.recurLoadData(catalog["model"]["jobs"],i,len(input_file2), input_file2)
    
    file3 = cf.data_dir + 'data/'+globalSufijo+'-multilocations.csv'
    input_file3 = list(csv.DictReader(open(file3, encoding='utf-8'), delimiter=";"))
    model.recurLoadData(catalog["model"]["multilocations"],i,len(input_file3),input_file3)
    
    file4 = cf.data_dir + 'data/'+globalSufijo+'-skills.csv'
    input_file4 = list(csv.DictReader(open(file4, encoding='utf-8'), delimiter=";"))
    model.recurLoadData(catalog["model"]["skills"],i,len(input_file4),input_file4)
    
    return catalog["model"]
    
    

    
    
def loadEmployments_types(catalog):
    file = cf.data_dir + 'data/'+globalSufijo+'-employments_types.csv'
    
    input_file = csv.DictReader(open(file, encoding='utf-8'), delimiter=";")
    
    for employment_type in input_file:
        model.add_employment_type(catalog, employment_type)
    return catalog

def loadJobs(catalog):
    file = cf.data_dir + 'data/'+globalSufijo+'-jobs.csv'
    input_file = csv.DictReader(open(file, encoding='utf-8'), delimiter=";")
    conteo = 0
    for job in input_file:
        conteo += 1
        model.add_job(catalog, job)
        #if conteo == 200:
        #    break
    return catalog



def loadMultilocations(catalog):
    file = cf.data_dir + 'data/'+globalSufijo+'-multilocations.csv'
    input_file = csv.DictReader(open(file, encoding='utf-8'),delimiter=";")
    for multilocation in input_file:
        model.add_multilocations(catalog, multilocation)
    return catalog

def loadSkills(catalog):
    file = cf.data_dir + 'data/'+globalSufijo+'-skills.csv'
    input_file = csv.DictReader(open(file, encoding='utf-8'), delimiter=";")
    for skill in input_file:
        model.add_skills(catalog, skill)
    return catalog

def three_first_last(data_structs, name):
    ft, lt=model.three_first_last(data_structs, name)
    return ft,lt

def data_size(data_structs, name):
    size = model.data_size(data_structs, name)
    return size
    
    
    
    
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


def req_1(control):
    """
    Retorna el resultado del requerimiento 1
    """
    # TODO: Modificar el requerimiento 1
    pass


def req_2(control, offer_number, company_name, city):
    """
    Retorna el resultado del requerimiento 2
    """
    # TODO: Modificar el requerimiento 2
    start_time = get_time()
    catalog = control["model"]["jobs"]
    function = model.req_2(catalog, offer_number, company_name, city)
    if function !=None:
        size = model.lt.size(function)
    else:
        size = 0
    end_time = get_time()
    time= delta_time(start_time, end_time)
    return size, function, time


def req_3(control):
    """
    Retorna el resultado del requerimiento 3
    """
    # TODO: Modificar el requerimiento 3
    pass


def req_4(control, codigo_pais,fecha_inicial, fecha_final):
    """
    Retorna el resultado del requerimiento 4
    """
    # TODO: Modificar el requerimiento 4
    start_time = get_time()
    catalog = control["model"]
    data , empresas , ciudades, max_empresa, min_ciudad= model.req_4(catalog, codigo_pais,fecha_inicial, fecha_final)
    #max_empresas = model.max_min_conteo_ofertas(conteo_empresa, True)
    #min_ciudades = model.max_min_conteo_ofertas(conteo_ciudad, False)
    end_time = get_time()
    time= delta_time(start_time, end_time)
    
    return data , empresas , ciudades, time , max_empresa, min_ciudad


def req_5(control,city, first_date, last_date):
    """
    Retorna el resultado del requerimiento 5
    """
    # TODO: Modificar el requerimiento 5
    
    """
    Incializamos todo lo que vamos a utilizar mas abajo
    
    """
    start_time = get_time()
    catalog = control["model"]["jobs"]
    function = model.req_5(catalog, city, first_date, last_date)
    size = model.lt.size(function)
    dicc_aux = {}
    cont = 0
    """
    Guardamos los nombres de las compañias y las veces que se repiten en un diccionario
    para luego sacar la compañia con mas numero de ofertas y 
    la compañia con menor numero de ofertas
    """
    #-------------------------------------------------------
    for i in lt.iterator(function):
        if i["company_name"] not in dicc_aux:
            dicc_aux[i["company_name"]] = 1 
            cont +=1
           
        else:
            dicc_aux[i["company_name"]] += 1
    #-------------------------------------------------------
    """
    Sacamos la ciudad con mayor y menor numero de ofertas
    """
    #-------------------------------------------------------
    if len(dicc_aux)>0:
      
        upper_offer = max(dicc_aux.values())
        
        minor_offer = min(dicc_aux.values())

        for i in dicc_aux.items():

            if i[1] == upper_offer:
                 upper_offer0 = i[0]
            if i[1] == minor_offer: 
                minor_offer0 = i[0]
                
            
    else: 
        upper_offer = None
        minor_offer = None
        upper_offer0 =  None
        minor_offer0 = None
    end_time = get_time()
    time= delta_time(start_time, end_time)
    #-------------------------------------------------------
    return int(size), function, cont, upper_offer, minor_offer, upper_offer0, minor_offer0, time


def req_6(control, N, codigo_pais, lvl_experticia ,fecha_inicial, fecha_final):
    """
    Retorna el resultado del requerimiento 6
    """
    # TODO: Modificar el requerimiento 6
    start_time = get_time()
    catalog = control["model"]
    
    NjobOffers = model.req_6(catalog, int(N), codigo_pais, lvl_experticia ,fecha_inicial, fecha_final)
    total_ciudades,total_empresas,total_ofertas, avg_salary_total_offers,nombre_ciudad_mayor, conteo_ciudad_mayor, nombre_ciudad_menor, conteo_ciudad_menor = model.manipular_NJobOffers_req6(NjobOffers)
    end_time = get_time()
    time= delta_time(start_time, end_time)
    return NjobOffers, total_ciudades,total_empresas,total_ofertas, avg_salary_total_offers,nombre_ciudad_mayor, conteo_ciudad_mayor, nombre_ciudad_menor, conteo_ciudad_menor, time
    


def req_7(control, country_number, first_date, last_date ):
    """
    Retorna el resultado del requerimiento 7
    """
    # TODO: Modificar el requerimiento 7
    """
    Incializamos todo lo que vamos a utilizar mas abajo
    
    """
    #-------------------------------------------------------
    start_time = get_time()
    catalog = control["model"]
    function = model.req_7(catalog, country_number, first_date, last_date )
    dicc_aux = {}
    cont = 0
    dicc_skillsXExpertiz = {}
    dicc_skillsXExpertizLess = {}
    dicc_empresas = {}
    #-------------------------------------------------------
    size = model.lt.size(function[0]) #Sacamos el numero de ofertas totales
    #-------------------------------------------------------
    """
    Agregamos las ciudades y las veces que se repiten a un diccionario para luego contarlas
    y sacar la ciudad con mayor numero de ofertas
    """
    #-------------------------------------------------------
    for i in lt.iterator(function[0]):
        if i["city"] not in dicc_aux:
            dicc_aux[i["city"]] = 1 
            cont +=1

           
        else:
            dicc_aux[i["city"]] += 1
    #-------------------------------------------------------
    """
    Realizamos el mismo proceso pero con los paises, esta vez es mas facil 
    porque ya los habiamos tratado en el model
    """    
    if len(function[1])>0:
        max_country = max(function[1].values())
        for i in function[1].items():
            if i[1] == max_country:
                 max_country0 = i[0]
    else:
        max_country = None
        max_country0 = None
    #-------------------------------------------------------
    """
    Sacamos la ciudad con mayor y menor numero de ofertas
    """
    #-------------------------------------------------------
    if len(dicc_aux)>0:
        max_city = max(dicc_aux.values())       
        for i in dicc_aux.items():
            if i[1] == max_city:
                 max_city0 = i[0]   
    else:
        max_city = None
        max_city0 = None
    #-------------------------------------------------------
    """
    Sacamos la habilidad mas y menos solicitada por nivel de experticia
    """  
    #-------------------------------------------------------
    
    if len(function[2])>0:
        for i in function[2].items():
            mayores = max(i[1].values())
            menores = min(i[1].values())
            auxxx ={}
            auxx2 = {}
        
            for j in i[1].items():
                if j[1]==mayores:
                    auxxx[j[0]]= mayores
                if j[1]==menores:
                    auxx2[j[0]]=menores

            dicc_skillsXExpertiz[i[0]] = auxxx
            dicc_skillsXExpertizLess[i[0]] = auxx2
    
    #-------------------------------------------------------
    """
    Agregamos el numero de ofertas de trabajo por nivel de experticia
    --------OJO: como estoy utilizando diccionarios de diccionarios
                  no saco el mayor y menor aqui, sino en view para facilitarlo
    
    """
    #-------------------------------------------------------
   
    
    
    for i in lt.iterator(function[0]):
        aux = {}
        
        for j in function[2].items():
            if j[0] == i["experience_level"]:
                

                if i["company_name"] not in aux :
                    aux[i["company_name"]]=1
                else:
                    aux[i["company_name"]]=+1
            else:
                if i["company_name"] not in aux :
                    aux[i["company_name"]]=1
                else:
                    aux[i["company_name"]]=+1
            dicc_empresas[j[0]] = aux
            
    end_time = get_time()
    time= delta_time(start_time, end_time)
            
        
            
    #-------------------------------------------------------

    return int(size), function, cont, max_country, max_country0, max_city, max_city0, dicc_skillsXExpertiz, dicc_skillsXExpertizLess, dicc_empresas, time

def req_8(control, lvl_experticia ,fecha_inicial, fecha_final):
    """
    Retorna el resultado del requerimiento 8
    """
    # TODO: Modificar el requerimiento 8
    start_time = get_time()
    catalog = control["model"]
    data, divisas = model.req_8(catalog, fecha_inicial, fecha_final, lvl_experticia)
    total_empresas, ofertas_rango_salarial,ofertas_fijas,ofertas_sin_salario,total_ofertas,total_paises,total_ciudades, paises = model.manipular_data_req8(data)
    end_time = get_time()
    time= delta_time(start_time, end_time)
    return total_empresas, ofertas_rango_salarial,ofertas_fijas,ofertas_sin_salario,total_ofertas,total_paises,total_ciudades, len(divisas), paises, time

def resultados_pais(paises, prim_ultim):
    codigo,total_ofertas, promedio_salario_ofertado, numero_ciudades, numero_empresas, mayor_salario, menor_salario, divisas, avg_skills=model.resultados_pais(paises, prim_ultim)
    return codigo,total_ofertas, promedio_salario_ofertado, numero_ciudades, numero_empresas, mayor_salario, menor_salario, divisas, avg_skills
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
