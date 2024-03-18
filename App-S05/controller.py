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
import datetime
from DISClib.Algorithms.Sorting import selectionsort as ses
from DISClib.Algorithms.Sorting import insertionsort as ins
from DISClib.Algorithms.Sorting import shellsort as shs
from DISClib.Algorithms.Sorting import mergesort as mes
from DISClib.Algorithms.Sorting import quicksort as qus
from DISClib.Algorithms.Sorting import heapsort as hes
from DISClib.Algorithms.Sorting import bogosort as bos
from DISClib.Algorithms.Sorting import customsort as cus
from DISClib.ADT import list as lt

csv.field_size_limit(2147483647)


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

sort_algorithm=None


def new_Controller(tipo_lst):
    """
    Crea una instancia del modelo
    """
    control = {
        'model': None
    }
    control['model'] = model.new_data_structs(tipo_lst)
    return control

    #TODO: Llamar la función del modelo que crea las estructuras de datos
    
def tipo_lista (tipo_lst):
    tipo = model.new_data_structs(tipo_lst)

# Funciones para la carga de datos

def loadData(control, muestra):
    """
    Carga los datos del reto
    """
    # TODO: Realizar la carga de datos
    data_struct = control['model']
    
    
    loadSkills(data_struct, muestra)
    
    loadEmployment_types(data_struct, muestra)
     
    loadMultilocations(data_struct, muestra)
    
    numJobs = loadJobs(data_struct, muestra)
    
    
    #Sublistas necesarias para hacer la imprisión de carga de de datos
    sublist_primeros3=model.newSublist(data_struct['jobs'],1,3)
    sublist_ultimos3=model.newSublist(data_struct['jobs'],(numJobs-2),3)
    
    
    return numJobs, sublist_primeros3, sublist_ultimos3

def loadJobs(data_struct, muestra):
    jobfile = cf.data_dir + muestra + '-jobs.csv'
    input_file = csv.DictReader(open(jobfile, encoding='utf-8'),delimiter=';')
    
    
    for job in input_file:
        temp=job["published_at"].split("T")
        job['published_at']=temp[0]
        
        #Añado los salarios de ese trabajo para que después no tenga que recorrer el archivo employementType
        
        jobEmploymentType=model.searchJob_byID(data_struct["employment_types"], job["id"])
       
        if jobEmploymentType != -1:
            if type(jobEmploymentType["salary_from"]) is float or type(jobEmploymentType["salary_from"]) is str:
                job['salary_from']=jobEmploymentType["salary_from"]
                job['salary_to']=jobEmploymentType["salary_to"]
            else:
                job['salary_from']=None
                job['salary_to']=None
        else:
            job['salary_from']=None
            job['salary_to']=None
        
        model.addJob(data_struct, job.copy())

    model.sortJobsDate(data_struct)

    return model.jobSize(data_struct)


def loadSkills(data_struct, muestra):
    skillsFile = cf.data_dir + muestra + '-skills.csv'
    input_file = csv.DictReader(open(skillsFile, encoding='utf-8'),delimiter=';')
    for skill in input_file:
        model.addSkills(data_struct, skill)
    
    model.sort_loadSkills(data_struct)

    return None

def loadEmployment_types(data_struct, muestra):
    skillsFile = cf.data_dir + muestra + '-employments_types.csv'
    input_file = csv.DictReader(open(skillsFile, encoding='utf-8'),delimiter=';')
    for employType in input_file:  
        model.addEmployment_types(data_struct, employType)
  
    model.sort_EmploymentTypes(data_struct)
    return None

def loadMultilocations(data_struct, muestra):
    skillsFile = cf.data_dir + muestra + '-multilocations.csv'
    input_file = csv.DictReader(open(skillsFile, encoding='utf-8'),delimiter=';')
    
    pre_prev={"id":None}
    prev={"id":None}
    
    for multilocation in input_file:
        model.addMultilocation(data_struct, multilocation)
        current=multilocation
        
        #añado el elemento a multilocationResumido si tiene más de una location y solo una vez
        if prev["id"]==pre_prev["id"] and current["id"]!=prev["id"] and prev["id"]!=None:
            model.addMultilocationResumido(data_struct, prev)
            
        pre_prev=prev
        prev=current
    
    model.sortMultilocation_resumido(data_struct)
            
    return None


# Funciones de ordenamiento


def sortJobsDate(data_struct):
    """
    Ordena los datos del modelo
    """
    #TODO: Llamar la función del modelo para ordenar los datos
    
    
    start_time = get_time()
    sorted_jobs=model.sortJobsDate(data_struct["model"])
    end_time = get_time()
    tiempo = delta_time(start_time, end_time)
    
    return sorted_jobs, tiempo



def setSortAlgorithm (picked):
    
    ans = model.selectSortAlgorithm(picked)
    algorithm = ans[0]
    model.sort_algorithm = algorithm
    algoritm_msg = ans[1]
    
    return algoritm_msg




# Funciones de consulta sobre el catálogo

def get_data(control, id):
    """
    Retorna un dato por su ID.
    """
    #TODO: Llamar la función del modelo para obtener un dato
    pass


def ultimosNPaisExp(control, codPais, exp, n):
    """
    Retorna el resultado del requerimiento 1
    """
    # TODO: Modificar el requerimiento 1
    start_time = get_time()
    struct = control['model']
    a, size= model.ultimosNPaisExp(struct, codPais, exp, n)
    end_time = get_time()
    tiempo = delta_time(start_time, end_time)
    return a, size, tiempo


def req_2(control, n, city, emp):
    """
    Retorna el resultado del requerimiento 2
    """
    # TODO: Modificar el requerimiento 2
    start_time = get_time()
    ofertas, size = model.req_2(control["model"], n, city, emp)
    end_time = get_time()
    tiempo = delta_time(start_time, end_time)

    return ofertas, size, tiempo


def req_3(control, empresa, fecha_i, fecha_f):
    """
    Retorna el resultado del requerimiento 3
    """
    # TODO: Modificar el requerimiento 3
    start_time = get_time()
    struct = control['model']
    ofer = model.req_3(struct, empresa, fecha_i, fecha_f)
    end_time = get_time()
    tiempo = delta_time(start_time, end_time)
    return ofer,  tiempo

def paisRangoT(control, codPais, datei, datef):
    """
    Retorna el resultado del requerimiento 4
    """
    # TODO: Modificar el requerimiento 4
    start_time = get_time()
    rango, empresas, cities = model.paisRangoT(control ["model"], codPais, datei, datef)
    end_time = get_time()
    tiempo = delta_time(start_time, end_time)
    return rango, empresas, cities, tiempo
    


def req_5(control, ciudad, fecha_inicial, fecha_final):
    """
    Retorna el resultado del requerimiento 5
    """
    start_time = get_time()
    ans = model.req_5(control["model"], ciudad, fecha_inicial, fecha_final)
    end_time = get_time()
    tiempo = delta_time(start_time, end_time)
    answer = [ans, tiempo]
    return answer

def req_6(control, numCiudades, codPais, exp_level, fecha_inicial, fecha_final):
    """
    Retorna el resultado del requerimiento 6
    """
    # TODO: Modificar el requerimiento 6
    start_time = get_time()
    ans=model.req_6(control["model"], numCiudades, codPais, exp_level, fecha_inicial, fecha_final)
    end_time = get_time()
    tiempo = delta_time(start_time, end_time)
    answer = [ans, tiempo]
    return answer


def req_7(control, numPaises, fecha_inicial, fecha_final):
    """
    Retorna el resultado del requerimiento 7
    """
    # TODO: Modificar el requerimiento 7
    start_time = get_time()
    ans=model.req_7(control["model"], numPaises, fecha_inicial, fecha_final)
    end_time = get_time()
    tiempo = delta_time(start_time, end_time)
    answer = [ans, tiempo]
    return answer


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
