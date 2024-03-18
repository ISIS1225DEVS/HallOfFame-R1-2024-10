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
from DISClib.Algorithms.Sorting import selectionsort as ses
from DISClib.Algorithms.Sorting import insertionsort as ins
from DISClib.Algorithms.Sorting import shellsort as shs
from DISClib.Algorithms.Sorting import mergesort as mes
from DISClib.Algorithms.Sorting import quicksort as qus
from DISClib.Algorithms.Sorting import heapsort as hes
from DISClib.Algorithms.Sorting import bogosort as bos
from DISClib.Algorithms.Sorting import customsort as cus

import datetime


assert cf

sort_algorithm=shs


"""
Se define la estructura de un catálogo de videos. El catálogo tendrá
dos listas, una para los videos, otra para las categorias de los mismos.
"""

# Construccion de modelos


def new_data_structs(tipo_lst):
    """
    Inicializa las estructuras de datos del modelo. Las crea de
    manera vacía para posteriormente almacenar la información.
    """
    
    data_struct = {'jobs': None,
               'skills': None,
               'employment_types': None,
               'multilocation': None,
               "multilocation_resumido":None}
    
    #Una lista para cada archivo y asignamos el tipo de lista que será

    data_struct['jobs'] = lt.newList(tipo_lst)
    data_struct['skills'] = lt.newList(tipo_lst)
    data_struct['employment_types'] = lt.newList(tipo_lst)
    data_struct['multilocation'] = lt.newList(tipo_lst)
    #Esta lista auxiliar ayudar al req7, solo contiene las ofertas que tienen más de una sede
    data_struct['multilocation_resumido'] = lt.newList(tipo_lst)
    

    return data_struct



# Funciones para agregar informacion al modelo

def addJob(data_structs, job):
    """
    Función para agregar nuevos elementos a la lista
    """
    lt.addLast(data_structs['jobs'], job)
    #TODO: Crear la función para agregar elementos a una lista
    return data_structs

def addSkills(data_structs, skill):
    """
    Función para agregar nuevos elementos a la lista
    """
    lt.addLast(data_structs['skills'], skill)
    #TODO: Crear la función para agregar elementos a una lista
    return data_structs


def addEmployment_types(data_structs, employType):
    """
    Función para agregar nuevos elementos a la lista
    """
    #Cambio de divisa
    if  employType["currency_salary"] == "usd":
        employType["salary_from"] = float(employType["salary_from"]) * 3.98
        employType["salary_to"] = float(employType["salary_to"]) * 3.98


    elif  employType["currency_salary"] == "gbp":
        employType["salary_from"] = float(employType["salary_from"]) * 5.05
        employType["salary_to"] = float(employType["salary_to"]) * 5.05


    elif  employType["currency_salary"] == "eur":
        employType["salary_from"] = float(employType["salary_from"]) * 4.32
        employType["salary_to"] = float(employType["salary_to"]) * 4.32


    elif  employType["currency_salary"] == "chf":
        employType["salary_from"] = float(employType["salary_from"]) * 4.49
        employType["salary_to"] = float(employType["salary_to"]) * 4.49            


    lt.addLast(data_structs['employment_types'], employType)
    #TODO: Crear la función para agregar elementos a una lista
    return data_structs

def addMultilocation(data_structs, multilocation):
    """
    Función para agregar nuevos elementos a la lista
    """
    lt.addLast(data_structs['multilocation'], multilocation)
    #TODO: Crear la función para agregar elementos a una lista
    return data_structs

def addMultilocationResumido(data_struct, multilocation):
    """
    Función para agregar nuevos elementos a la lista
    """
    lt.addLast(data_struct['multilocation_resumido'], multilocation)
    #TODO: Crear la función para agregar elementos a una lista
    return data_struct
    
    
# Funciones para creacion de datos

def new_data(id, info):
    """
    Crea una nueva estructura para modelar los datos
    """
    #TODO: Crear la función para estructurar los datos
    pass

def newSublist(lst, pos, numelem):
    sublist=lt.subList(lst,pos,numelem)
    return sublist

def newIterator(lst):
    new_iterator=lt.iterator(lst)
    return new_iterator

# Funciones de consulta

def get_data(data_structs, id):
    """
    Retorna un dato a partir de su ID
    """
    #TODO: Crear la función para obtener un dato de una lista
    pass


def jobSize(data_structs):
    """
    Retorna el tamaño de la lista de datos
    """
    #TODO: Crear la función para obtener el tamaño de una lista
    return lt.size(data_structs['jobs'])

def skillsSize(data_structs):
    """
    retorna tamaño de la lista de skills
    """
    return lt.size(data_structs["skills"])

def Employment_typesSize(data_structs):
    """
    retorna tamaño de el tipo de trabajo
    """
    return lt.size(data_structs["Employment_types"])
    
def MultilocationSize(data_structs):
    """
    retorna tamaño de la lista de datos por ubicacion
    """
    return lt.size(data_structs["multilocation"])


#                                  ////////////requerimientos///////////////////



def ultimosNPaisExp(data_structs, codPais, exp, n):
    """

    Args:
    El número (N) de ofertas a listar (ej.: 3, 5, 10 o 20).
    Código del país (ej.: PL, CO, ES, etc).
    Nivel de experticia de las ofertas a consultar (junior, mid, o senior).
    Returns:
    El total de ofertas de trabajo ofrecidas según la condición (junior, mid, o senior).
     Para cada una de las ofertas de la consulta debe presentar la siguiente información:

   
    """
    
    ofertas_tot= lt.newList("ARRAY_LIST")
    a= lt.newList("ARRAY_LIST")
     
    for oferta in lt.iterator(data_structs["jobs"]):
        if oferta["experience_level"]== exp and oferta["country_code"]== codPais:
            lt.addLast(ofertas_tot, oferta)
        
    size = lt.size(ofertas_tot)
    
    i = size  
    while i > 0 and lt.size(a)< n: 
        lt.addLast(a, lt.getElement(ofertas_tot, i))
        i-= 1
    return a, size


def req_2(data_structs, n, city, nom_emp):
   
    # TODO: Realizar el requerimiento 2
    jobs = data_structs["jobs"]
    ofertas_totales  = lt.newList("ARRAY_LIST")
    ofertas  = lt.newList("ARRAY_LIST")

    for job in lt.iterator(jobs):
        if job["city"] == city and job["company_name"] == nom_emp:
            lt.addLast(ofertas_totales, job)

    size = lt.size(ofertas_totales)

    i = size
    while i > 0 and lt.size(ofertas) < n:
        lt.addLast(ofertas, lt.getElement(ofertas_totales, i))
        i -= 1


    return ofertas, size 


def organiza_fecha_pais(elem1, elem2):
    fecha1= datetime.strptime(elem1["Published_at"], "%Y-%m-%dT%H:%M:%S.%fZ").strftime("%y-%m-%d")
    fecha2= datetime.strptime(elem2["Published_at"], "%Y-%m-%dT%H:%M:%S.%fZ").strftime("%y-%m-%d")
    if fecha1 == fecha2: 
        if elem1["country_code"] > elem2["country_code"]:
           return True
        else:   
            return False  
    elif fecha1 > fecha2:
        return True
    else:
        return False 
def req_3(data_structs, empresa, fecha_i, fecha_f):
    """
    Función que soluciona el requerimiento 3
    entrada: nombre empresa, fecha inicio y fecha fin 
    retorna: total ofertas, total ofertas junior, total ofertas mid, total ofertas senior
    listado ofertss ordenados cronologicamente de 
    """
    td_fechas= lt.newList(datastructure="ARRAY_LIST")
    
    for nombre in lt.iterator(data_structs["jobs"]):
        if empresa == nombre["company_name"]:
            fecha_convertida = datetime.strptime(nombre["Published_at"], "%Y-%m-%dT%H:%M:%S.%fZ").strftime("%y-%m-%d")
            fecha_I = datetime.strptime(fecha_i, "%Y-%m-%d")
            fecha_F = datetime.strptime(fecha_f, "%Y-%m-%d")
            if fecha_I <= fecha_convertida and fecha_F >= fecha_convertida:
                lt.addFirst(td_fechas, nombre)
    
    shs.sort(td_fechas,organiza_fecha_pais)
    
    j_ofertas= lt.newList(datastructure="ARRAY_LIST")
    m_ofertas= lt.newList(datastructure="ARRAY_LIST")
    s_ofertas= lt.newList(datastructure="ARRAY_LIST")
    #listas pfertas j,m,s
    for oferta in lt.iterator(td_fechas):
        if oferta["Experience_level"] == "junior":
            lt.addLast(j_ofertas, oferta )
        elif oferta["Experience_level"] == "mid":
            lt.addLast(m_ofertas, oferta )
        elif oferta["Experience_level"] == "senior":
            lt.addLast(s_ofertas, oferta )
    ofer= lt.size(td_fechas)        
    ju= lt.size(j_ofertas)
    mi= lt.size(m_ofertas)
    se= lt.size(s_ofertas)
    return ofer, ju, mi, se, td_fechas
    
    
"""  
    
    filtro = sortbyeyd(jobs, empresa, Pos_datei, Pos_datef)
    a= lt.newList("ARRAY_LIST")
    size = lt.size(filtro)
    i = size  
    while i > 0 and lt.size(a)< n: 
        lt.addLast(a, lt.getElement(ofertas_tot, i))
        i-= 1
    return a, size
"""

def sortbyeyd(jobs, empresa, fecha_i, fecha_f):
    filtro = lt.new_list()
    for i in range( jobSize-1, -1, -1):
        d = lt.get_element(jobs, i)
        if empresa == d['company_name'] and (fecha_i <= d['published_at'] <= fecha_f):
            lt.addlast(filtro, d)
    return filtro
    
    
    
    """
    parametros entrada: datos, nombre empresa, fecha inicio rango, fecha fin
    busca encontrar n ofertas dentro de un rango de tiempo especifico
    devuelve: +listado ofertas ordenadas cornologicamente por fecha y paus  
              + num ofertas exjunior, num ofertas mid, num ofertas senior 
    """
    """
    Función que soluciona el requerimiento 3
    """
    # TODO: Realizar el requerimiento 3
    """
    lista_trabajos= lt.iterator(data_structs["jobs"])

    for ofertas in lista_trabajos: 
        if jobs["dates"] >= fecha_i and jobs["date"]: 
    

    """
    

def paisRangoT(data_structs, codPais, datei, datef):
    """
    Función que soluciona el requerimiento 4
    """
    # TODO: Realizar el requerimiento 4
    Pos_datei = searchFecha(data_structs, datei, True)
    Pos_datef = searchFecha(data_structs, datef, False)
    
    size_lst_fechas = Pos_datef - Pos_datei
    
    lst_fechas=lt.subList(data_structs["jobs"],Pos_datei, size_lst_fechas)
    rango = lt.newList("ARRAY_LIST")

    for job in lt.iterator(lst_fechas):
        if job["country_code"] == codPais:
            lt.addLast(rango, job)

    
    empresas = lt.newList("ARRAY_LIST")
    for job in lt.iterator(rango):
        if not(lt.isPresent(empresas, job["company_name"])):
            lt.addLast(empresas, job["company_name"])
    
    ciudades = {}
    for job in lt.iterator(rango):
        if job["city"] not in ciudades:
            ciudades[job["city"]] = 1
        elif job["city"] in ciudades:
            ciudades[job["city"]] += 1
    
    if len(ciudades) != 0:
        mayor = 0
        for city in ciudades:
            if ciudades[city] > mayor: 
                mayor = ciudades[city]
                city_may = city

        menor = mayor 
        for city in ciudades: 
            if ciudades[city] < menor:
                menor = ciudades[city]
                city_men = city 
        if menor == mayor:
            menor = mayor
            city_men = city_may

    else: 
        city_may = 0
        mayor = 0
        city_men = 0
        menor = 0
    
   
    cities = [city_may, mayor, city_men, menor]

    rango_ord = shs.sort(rango, sortCrit_companyName_MenorMayor)
    rango_ordenado = mes.sort(rango_ord, sortCrit_JobDates)

    return rango_ordenado, empresas, cities


def req_5(data_struct, ciudad, fecha_inicial, fecha_final):
    """
    Consulta las ofertas que se publicaron en una ciudad durante un periodo de tiempo
    
    Args:
       data_structs: data structure
       ciudad: Nombre de la ciudad.
       fecha_inicial: La fecha inicial del periodo a consultar (con formato "%Y-%m-%d").
       fecha_final: La fecha final del periodo a consultar (con formato "%Y-%m-%d").
       
    Returns:
        Una lista [sublistCities_final_sort, mayorNombre, mayorNum, menorNombre, menorNum, total_empresas]
        sublistCities_final_sort: Sublista de las ofertas que se publicaron en una ciudad durante un periodo de tiempo
        mayorNombre: empresa con más ofertas
        mayorNum: numero de ofertas de esa empresa
        menorNombre: empresa con menos ofertas
        menorNum: numero de ofertas de esa empresa
        total_empresas: numero de empresas totales

    """
    
    #Binary search del comienzo de fechas y el final
    Posjob_fechaInicial=searchFecha(data_struct, fecha_inicial, True)
    Posjob_fechaFinal=searchFecha(data_struct, fecha_final, False)
    
    size_sublistFechas=Posjob_fechaFinal-Posjob_fechaInicial
       
    #Saco el rango de fechas necesarias
    sublistFechas=lt.subList(data_struct["jobs"],Posjob_fechaInicial, size_sublistFechas)
    sublistCities=lt.newList("ARRAY_LIST")
    list_para_empresas=lt.newList("ARRAY_LIST")
    
    for job in lt.iterator(sublistFechas):
        if job["city"]==ciudad:
            lt.addLast(sublistCities, job)
            lt.addLast(list_para_empresas, job)
    
    #Ordeno alfabéticamente
    sublistCities_alfabetica=shs.sort(sublistCities, sortCrit_companyName_MenorMayor)
    #Ordeno otra vez por fechas pero esta vez usando merge que es estable para mantener el orden alfabético
    sublistCities_final_sort=mes.sort(sublistCities_alfabetica, sortCrit_JobDates)
    
    jobsxempresas=newList_jobsxempresas(list_para_empresas)
    
    menorNum=300000
    mayorNum=0
    #Recorro la lista de jobsxempresas para sacar el menor y mayor
    for empresa in lt.iterator(jobsxempresas):
        if empresa[1]>mayorNum:
            mayorNum=empresa[1]
            mayorNombre=empresa[0]
        if empresa[1]<menorNum:
            menorNum=empresa[1]
            menorNombre=empresa[0]
        
    total_empresas=lt.size(jobsxempresas)
    
    ans=[sublistCities_final_sort, mayorNombre, mayorNum, menorNombre, menorNum, total_empresas]

    return ans

def req_6(data_structs, numCiudades, codPais, exp_level, fecha_inicial, fecha_final):
    """
    Función que soluciona el requerimiento 6
    
    Returns:
        lista = [ultima_lista, size_sublistN_cities, empresas_totales, sumatoria_jobs, salario_promedio_total, 
         ciudad_más_ofertas, ciudad_menos_ofertas]
        ultima_lista: lista para impresion
        lista size_sublistN_cities: El total de ciudades que cumplen con las condiciones de la consulta
        empresas_totales: El total de empresas que cumplen con las condiciones de la consulta
        sumatoria_jobs: El total de ofertas publicadas que cumplen con las condiciones de la consulta
        salario_promedio_total: El promedio del salario ofertado de todas las ofertas que cumplen con las condiciones de la consulta
        ciudad_más_ofertas: Nombre de la ciudad con mayor cantidad de ofertas de empleos y su conteo
        ciudad_menos_ofertas: Nombre de la ciudad con menor cantidad de ofertas de empleos y su conteo
        
    """

    Posjob_fechaInicial=searchFecha(data_structs, fecha_inicial, True)
    Posjob_fechaFinal=searchFecha(data_structs, fecha_final, False)
    
    size_sublistFechas=Posjob_fechaFinal-Posjob_fechaInicial
    
    sublistFechas=lt.subList(data_structs["jobs"],Posjob_fechaInicial, size_sublistFechas)
    list_exp_pais = lt.newList("ARRAY_LIST")

    if codPais != None: 
        for job in sublistFechas["elements"]: 
            if job["experience_level"] == exp_level and job["country_code"] == codPais:
                lt.addLast(list_exp_pais, job)

    else: 
        for job in sublistFechas["elements"]: 
            if job["experience_level"] == exp_level:
                lt.addLast(list_exp_pais, job)            

    #Sorting de ciudades de mayor a menor para que después List Cities quede en orden alfabético
    sorted_Filtrada=shs.sort(list_exp_pais, sortCrit_Cities_MenorMayor)
    
    #Creo una lista de listas de ciudades
    ListCities=creador_lista_de_listas(sorted_Filtrada,"city")

    #Sorting por numero de ofertas. Uso de merge porque es estable para mantener orden alfabético
    sorted_ListCities=mes.sort(ListCities, sort_crit_sizeListas_MayorMenor)    
    
    #Si las ciudades quqe aplican a los criterios son menor que N, añado todas las quqe aplican
    if lt.size(sorted_ListCities)<numCiudades:
        size_sublistN_cities=lt.size(sorted_ListCities)
        sublistN_cities=lt.subList(sorted_ListCities,1,size_sublistN_cities)
    #Saco las primeras N ciudades con mayorees ofertas
    else:
        sublistN_cities=lt.subList(sorted_ListCities,1,numCiudades)
        size_sublistN_cities=numCiudades

    #Creo la lista que va a ser impresa para el usuario
    ultima_lista=lt.newList("ARRAY_LIST")
    #Lista de trabajo para sacar después numero de empresas
    jobs_list=lt.newList("ARRAY_LIST")
    #Cada elemento de esta lista va a ser un diccionario con la info de cada ciudad
    element={"Ciudad":None, "Numero_total_ofertas":None, "Salario_promedio":None, "Numero_total_empresas":None, "Empresa_con_mas_ofertas":None, 
             "Mejor_oferta":None, "Peor_oferta":None}
    
    #Contador de los salarios para sacar el promedio
    sumatoria_salario_totales=0
    #Contador de ofertas de trabajo
    sumatoria_jobs=0
    
    for CityList in lt.iterator(sublistN_cities):
        #Para sacar el promedio despues
        sum_salarios=0
    
        element["Ciudad"]=CityList["elements"][0]["city"]
        element["Numero_total_ofertas"]=lt.size(CityList)
        sumatoria_jobs+=lt.size(CityList)
        
        jobsxempresa=newList_jobsxempresas(CityList)
        element["Numero_total_empresas"]=lt.size(jobsxempresa)
        
        #Recorro la lista de jobsxempresas para sacar la empresa con mas ofertas
        mayorNum=0
        for empresa in lt.iterator(jobsxempresa):
            if empresa[1]>mayorNum:
                mayorNum=empresa[1]
                mayorNombre=empresa[0]
        
        element['Empresa_con_mas_ofertas']=mayorNombre,"con",mayorNum,"ofertas"

        #Recorro cada trabajo para después sacar empresas totales y sacar info de salarios
        peor_oferta=[None, 90000000]
        mejor_oferta=[None, 0]
        sizeCityList=lt.size(CityList)
        
        for job in lt.iterator(CityList):
            lt.addLast(jobs_list, job)
            
            #El try para que no saque error si esa oferta no tenía salario
            try:
                salarioJob_promedio=(int(job["salary_from"])+int(job["salary_to"]))/2
                sum_salarios+=salarioJob_promedio
                
                if peor_oferta[1]>salarioJob_promedio:
                    peor_oferta[1]=salarioJob_promedio
                    peor_oferta[0]=job["title"]
                if mejor_oferta[1]<salarioJob_promedio:
                    mejor_oferta[1]=salarioJob_promedio
                    mejor_oferta[0]=job["title"]
            except:
                #En ese caso no se tendra en cuenta para el promedio esa oferta
                sizeCityList-=1
            
            
        salarioCity_promedio=sum_salarios/sizeCityList
        sumatoria_salario_totales+=salarioCity_promedio
        
        element["Salario_promedio"]=salarioCity_promedio
        element['Peor_oferta']=peor_oferta
        element["Mejor_oferta"]=mejor_oferta
        
        lt.addLast(ultima_lista, element.copy())
        
    empresasList=newList_jobsxempresas(jobs_list)
    empresas_totales=lt.size(empresasList)

    #Tuple del nombre de la ciudad y su cantidad de ofertas
    ciudad_más_ofertas=lt.firstElement(ultima_lista)["Ciudad"], lt.firstElement(ultima_lista)["Numero_total_ofertas"]
    ciudad_menos_ofertas=lt.lastElement(ultima_lista)["Ciudad"], lt.lastElement(ultima_lista)["Numero_total_ofertas"]
    
    if codPais != None:
        salario_promedio_total=round((sumatoria_salario_totales/size_sublistN_cities))
    else:
        salario_promedio_total=None

    ans=[ultima_lista, size_sublistN_cities, empresas_totales, sumatoria_jobs, salario_promedio_total, 
         ciudad_más_ofertas, ciudad_menos_ofertas]
    
    return ans


def req_7(data_structs, numPaises, fecha_inicial, fecha_final):
    """
    Función que soluciona el requerimiento 7
    
    Returns:
        lista =[listImpresion, lt.size(listTotalJobs), lt.size(jobsxciudades), [ciudadMayorJobs, ciudadMayorJobs_Num], paisMayorOfertas]
        listImpresion: lista para imprimir de la info requerida
        lt.size(listTotalJobs):numero de ofertas totales
        lt.size(jobsxciudades): numero de ciudades donde se oferto
        [ciudadMayorJobs, ciudadMayorJobs_Num]: lista que tiene la ciudad con mayor ofertas y su conteo
        paisMayorOfertas: lista que contiene el páis con mas ofertas y su conteo
    """
    
    Posjob_fechaInicial=searchFecha(data_structs, fecha_inicial, True)
    Posjob_fechaFinal=searchFecha(data_structs, fecha_final, False)
    
    size_sublistFechas=Posjob_fechaFinal-Posjob_fechaInicial
    
    sublistFechas=lt.subList(data_structs["jobs"],Posjob_fechaInicial, size_sublistFechas)
    listPaises = lt.newList("ARRAY_LIST")
    
    sorted_sublistFechas=shs.sort(sublistFechas, sort_crit_Paises_MenorMayor)
    
    #Creo una lista de listas de países que cada uno contiene sus ofertas de trabajo
    listPaises=creador_lista_de_listas(sorted_sublistFechas, "country_code")

    #Sort de mayor a menor ofertas 
    sorted_listPaises=shs.sort(listPaises, sort_crit_sizeListas_MayorMenor)
    
    #Saco los N paises con mayores ofertas
    #Si las ciudades quqe aplican a los criterios son menor que N, añado todas las quqe aplican
    if lt.size(sorted_listPaises)<numPaises:
        sublist_NPaises=lt.subList(sorted_listPaises,1,lt.size(sorted_listPaises))
    #Saco las primeras N ciudades con mayorees ofertas
    else:
        sublist_NPaises=lt.subList(sorted_listPaises,1,numPaises)

        
    #contador para change info
    pos=1
    #Quiero que cada trabajo sea sorteado en una lista dependiendo de su experience level 
    for pais in lt.iterator(sublist_NPaises):
        sorted_jobs_byExp=shs.sort(pais, sortCrit_expLevel_MenorMayor)
        
        #Hago que el pais sea una lista de listas de experience level 
        listExpLevels_delPais=creador_lista_de_listas(sorted_jobs_byExp,"experience_level")
        lt.changeInfo(sublist_NPaises, pos, listExpLevels_delPais)
        
        pos+=1
    
    #Creo esta lista que va a ser utilizada para imprimir
    listImpresion=lt.newList("ARRAY_LIST")
    #Creo esta lista con todos los trabajos 
    listTotalJobs=lt.newList("ARRAY_LIST")

    for pais in lt.iterator(sublist_NPaises):
        paisImpresion=lt.newList("ARRAY_LIST")
        
        for expLevel_List in lt.iterator(pais):
            #Cada expLevelImpresion va a ser una fila en la tabla que le printea al usuario
            expLevelImpresion={"País": None, "Nivel de experiencia": None, "Numero_habilidades_solicitadas":None, "Habilidad_mas_solicitada":[0,1], "Habilidad_menos_solicitada":[0,1], 
                      "Promedio_nivel_mínimo_de_hablidades":None, "Numero_empresas_totales":None, "Empresa_mayor_ofertas":[0,1],
                      "Empresa_menor_ofertas":[0,1], "Numero_empresas_multisedes":None
                      }
            
            list_habilidades=lt.newList("ARRAY_LIST")
            jobsxempresas=newList_jobsxempresas(expLevel_List)
            
            expLevelImpresion["Nivel de experiencia"] = (lt.getElement(expLevel_List, 0))["experience_level"]
            expLevelImpresion["País"] = (lt.getElement(expLevel_List, 0))["country_code"]

            #Recorro la lista de jobsxempresas para sacar el menor y mayor
            menorNum=300000
            mayorNum=0
            for empresa in lt.iterator(jobsxempresas):
                if empresa[1]>mayorNum:
                    mayorNum=empresa[1]
                    mayorNombre=empresa[0]
                if empresa[1]<menorNum:
                    menorNum=empresa[1]
                    menorNombre=empresa[0]
                    
            #Añado al diccionario 
            expLevelImpresion["Numero_empresas_totales"]=lt.size(jobsxempresas)
            expLevelImpresion["Empresa_mayor_ofertas"]=[mayorNombre, mayorNum]
            expLevelImpresion["Empresa_menor_ofertas"]=[menorNombre, menorNum]

            numEmpresasMultisede=0
            
            #Para sacar numero de empresas con más de una sede, añadir a la lista de trabajos totales, y crear lista de habilidades
            for job in lt.iterator(expLevel_List):
                #Busco si el job tiene multilocation
                multiLocationJob=searchJob_byID(data_structs["multilocation_resumido"],job["id"])
                if multiLocationJob!=-1:
                    numEmpresasMultisede+=1
                    
                #Añado a lista toatl de ofertas
                lt.addLast(listTotalJobs,job)
                
                #Añado a lista de habilidades
                skillJob=searchJob_byIDSkill(data_structs["skills"],job["id"])
                if skillJob!=-1:
                    while lt.size(skillJob)>0:
                        lt.addLast(list_habilidades, lt.lastElement(skillJob))
                        lt.removeLast(skillJob)
            
            expLevelImpresion["Numero_empresas_multisedes"]=numEmpresasMultisede
                

            #Para sacar las habilidades de los trabajos
            jobsxhabiliades=newList_jobsxhabilidades(list_habilidades)
                        
            #Para sacar menor y mayor habilidad y promedio de nivel
            topSkill_Num=0
            topSkill_Name=None
            lastSkill_Num=90000
            lastSkill_Name=None
            sum_skillLevel=0
            for habilidad in lt.iterator(jobsxhabiliades):
                if habilidad[1]>topSkill_Num:
                    topSkill_Num=habilidad[1]
                    topSkill_Name=habilidad[0]
                if habilidad[1]<lastSkill_Num:
                    lastSkill_Num=habilidad[1]
                    lastSkill_Name=habilidad[0]
                sum_skillLevel+=habilidad[2]
                
            #Añado al diccionario
            expLevelImpresion["Promedio_nivel_mínimo_de_hablidades"]=sum_skillLevel/lt.size(jobsxhabiliades)
            expLevelImpresion["Habilidad_mas_solicitada"]=[topSkill_Name, topSkill_Num]
            expLevelImpresion["Habilidad_menos_solicitada"]=[lastSkill_Name, lastSkill_Num]
            expLevelImpresion["Numero_habilidades_solicitadas"]=lt.size(jobsxhabiliades)


            lt.addLast(paisImpresion, expLevelImpresion)
            
        lt.addLast(listImpresion, paisImpresion)
    
   
    #Para sacar la extra info de ciudades requeridas
    jobsxciudades=newList_jobsxciudades(listTotalJobs)
    ciudadMayorJobs=None
    ciudadMayorJobs_Num=0
    for ciudad in lt.iterator(jobsxciudades):
        if ciudad[1]>ciudadMayorJobs_Num:
            ciudadMayorJobs_Num=ciudad[1]
            ciudadMayorJobs=ciudad[0]
            
    #Lista [0]=nombre del pais con más ofertas, [1] su numero de ofertas
    paisMayor=lt.firstElement(sublist_NPaises)
    expPaisMayor=lt.firstElement(paisMayor)
    trabajoMayor=lt.firstElement(expPaisMayor)

    paisMayorOfertas=[trabajoMayor["country_code"], (lt.size(lt.getElement(paisMayor,1))+lt.size(lt.getElement(paisMayor,2))+lt.size(lt.getElement(paisMayor,3)))]
    
    ans=[listImpresion, lt.size(listTotalJobs), lt.size(jobsxciudades), [ciudadMayorJobs, ciudadMayorJobs_Num], paisMayorOfertas]
    
    return ans


def req_8(data_structs):
    """
    Función que soluciona el requerimiento 8
    """
    # TODO: Realizar el requerimiento 8
    pass

def creador_lista_de_listas(listOriginal, key):
    listaNueva=lt.newList("ARRAY_LIST")
    tempList=lt.newList("ARRAY_LIST"), None
    
    #Voy a crear listas del key, cuyos elementos son las ofertas, y añadirlas a la listaNueva como elementos
    for job in lt.iterator(listOriginal):        
        #Si se cambia a un nuevo tipo de la key en el recorrido
        if job[key]!=tempList[1]:

            #Guardo la info de ese tipo de key en listaNueva
            if tempList[1] is not None:
                lt.addLast(listaNueva, tempList[0])
            
            #Reinicio la lista temporal con el nombre de la nueva key de esta iteración
            tempList=lt.newList("ARRAY_LIST"),job[key]
            #Añado el primer trabajo de ese tipo de key
            lt.addLast(tempList[0],job)
        
        #Añade la oferta de trabajo en la lista temporal
        else:
            lt.addLast(tempList[0],job)
    
    #Añado la última lista temporal que no queda añadida
    
    lt.addLast(listaNueva, tempList[0])
    
    return listaNueva
    
    
def newList_jobsxempresas(lst):
    """
    Devuelve una lista de las empresas y sus numeros de ofertas
    
    Args:
       lst: lista de DISCLib con ofertas de trabajo para cada elemento
       
    Returns:
        lista DISClib que contiene como elementos [nombre empresa, numero de ofertas]
        
    """
    
    #Hago sort alfabético de todas las empresas
    list_empresas_ordenadas=shs.sort(lst, sortCrit_companyName_MenorMayor)
    list_jobsxempresas=lt.newList("ARRAY_LIST")
    
    #Recorro la lista de empresas ordenada para sumar las ofertas de cada empresa
    for job in lt.iterator(list_empresas_ordenadas):
        
        if lt.size(list_jobsxempresas)==0:
            #lt.lastElement saca error si la lista esta vacia, lo cual sucede en la primera iteración, y en este caso añado de una sin compararar
            lt.addLast(list_jobsxempresas, [job["company_name"], 1])
        
        else: 
            last_element_jobsxempresas=lt.lastElement(list_jobsxempresas)

            #Si el trabajo pertence a una empresa distinta que la del elemento pasado, añade uno nuevo
            if last_element_jobsxempresas[0]!=job["company_name"]: 
                lt.addLast(list_jobsxempresas, [job["company_name"], 1])
            
            #Si el trabajo tiene la misma empresa que el elemento pasado, le suma 1 a la cantidad de trabajos de la empresa
            elif lt.size(list_jobsxempresas)>0:
                last_element_jobsxempresas[1]+=1
                #Es por este changeInfo que escogí array list
                lt.changeInfo(list_jobsxempresas, lt.size(list_jobsxempresas), last_element_jobsxempresas)
            
    return list_jobsxempresas
    
def newList_jobsxhabilidades(lst):
    """
    Devuelve una lista de las habilidades con su conteo y promedio
    
    Args:
       lst: lista de DISCLib con ofertas de trabajo para cada elemento
       
    Returns:
        lista DISClib que contiene como elementos [nombre de la habilidad, numero de veces que aparecio, promedio del nivel]
        
    """
    
    #Hago sort alfabético de todas las habilidades
    list_habilidades_ordenadas=shs.sort(lst, sortCrit_skillName_MenorMayor)
    list_jobsxhabilidadess=lt.newList("ARRAY_LIST")
    
    #Recorro la lista de habilidades ordenada para sumar las las veces que aparece cada habilidad
    for job in lt.iterator(list_habilidades_ordenadas):
        
        if lt.size(list_jobsxhabilidadess)==0:
            #lt.lastElement saca error si la lista esta vacia, lo cual sucede en la primera iteración, y en este caso añado de una sin compararar
            lt.addLast(list_jobsxhabilidadess, [job["name"], 1, int(job["level"])])
        
        else: 
            last_element_jobsxhabilidades=lt.lastElement(list_jobsxhabilidadess)

            #Si el trabajo pertence a una skill distinta que la del elemento pasado, añade una nueva skill a la lista
            if last_element_jobsxhabilidades[0]!=job["name"]: 
                lt.addLast(list_jobsxhabilidadess, [job["name"], 1, int(job["level"])])
            
            #Si el trabajo tiene la misma skill que el elemento pasado, le suma 1 a la cantidad de trabajos del skill y actualiza el promedio
            elif lt.size(list_jobsxhabilidadess)>0:
                last_element_jobsxhabilidades[1]+=1
                promedio=(last_element_jobsxhabilidades[2]+int(job["level"]))/last_element_jobsxhabilidades[1]
                last_element_jobsxhabilidades[2]=promedio
                #Es por este changeInfo que escogí array list
                lt.changeInfo(list_jobsxhabilidadess, lt.size(list_jobsxhabilidadess), last_element_jobsxhabilidades)
            
    return list_jobsxhabilidadess

def newList_jobsxciudades(lst):
    """
    Devuelve una lista de las empresas y sus numeros de ofertas
    
    Args:
       lst: lista de DISCLib con ofertas de trabajo para cada elemento
       
    Returns:
        lista DISClib que contiene como elementos [nombre ciudad, numero de ofertas]
        
    """
    
    #Hago sort alfabético por las ciudades
    list_ciudades_ordenadas=shs.sort(lst, sortCrit_Cities_MenorMayor)
    list_jobsxciudades=lt.newList("ARRAY_LIST")
    
    #Recorro la lista de empresas ordenada para sumar las ofertas de cada empresa
    for job in lt.iterator(list_ciudades_ordenadas):
        
        if lt.size(list_jobsxciudades)==0:
            #lt.lastElement saca error si la lista esta vacia, lo cual sucede en la primera iteración, y en este caso añado de una sin compararar
            lt.addLast(list_jobsxciudades, [job["city"], 1])
        
        else: 
            last_element_jobsxciudades=lt.lastElement(list_jobsxciudades)

            #Si el trabajo pertence a una empresa distinta que la del elemento pasado, añade uno nuevo
            if last_element_jobsxciudades[0]!=job["city"]: 
                lt.addLast(list_jobsxciudades, [job["city"], 1])
            
            #Si el trabajo tiene la misma empresa que el elemento pasado, le suma 1 a la cantidad de trabajos de la empresa
            elif lt.size(list_jobsxciudades)>0:
                last_element_jobsxciudades[1]+=1
                #Es por este changeInfo que escogí array list
                lt.changeInfo(list_jobsxciudades, lt.size(list_jobsxciudades), last_element_jobsxciudades)
            
    return list_jobsxciudades

def buscar_salario (list_salario, job):
    pass

# Funciones utilizadas para comparar elementos dentro de una lista

def compare(data_1, data_2):
    """
    Función encargada de comparar dos datos
    """
    #TODO: Crear función comparadora de la lista
    pass

#Funciones de busqueda 

def searchFecha(data_struct, fecha, primera):
    """searchFecha es la MASCARA para la busqueda recursiva, recibe el
    data structure y la fecha a buscar y prepara las condiciones para la recursion

    Args:
        data_struct (dict): el data_struct
        fecha (str): la fecha buscada
        primera (bool): si True, da el primer trabajo de esa fecha. si False, da el último trabajo de ese fecha 

    Returns:
        pos: posición del diccionario que cumple con la fecha
    """
    
    idx=recursiveSearchFecha(data_struct["jobs"], fecha, 1, jobSize(data_struct)-1, primera)
    
    if idx==-1:
        return None
    else:
        return idx
    


def recursiveSearchFecha(jobs, fecha, low, high, primera):
    """recursiveSearchFecha ejecuta recursivamente la busqueda binaria
    de la fecha en la lista, si no lo encuentra retorna -1, utiliza la
    llave "published_at" para la comparacion

    Args:
        jobs (ADT List): lista de trabajos 
        fecha (str): fecha de la oferta que se busca
        low (int): rango inferior de busqueda
        high (int): rango superior de busqueda
        primera (bool): si True, te da el primer trabajo de esa fecha. si False, te da el último trabajo de esa fecha

    Returns:
        int: indice del trabajo en la lista. 
        Si primera=True, el primero de esa fecha si se encuentra, si no se encuentra el primer trabajo de la fecha después
        Si primera=False, el último de esa fecha si se encuentra, si no se encuentra el ultimo trabajo de la fecha antes
    """

    pos=(high+low)//2
    
    if low<=high:
        
        if fecha==(jobs['elements'][pos]['published_at']):
            if primera:
                while fecha==(jobs['elements'][pos-1]['published_at']):
                    pos=pos-1
                return pos
            else:
                while fecha==(jobs['elements'][pos+1]['published_at']):
                    pos=pos+1
                return pos
        
        elif jobs['elements'][pos]['published_at'] > fecha:
            high=pos-1
            return recursiveSearchFecha(jobs, fecha, low, high, primera)
            
        elif jobs['elements'][pos]['published_at'] < fecha:
            low=pos+1
            return recursiveSearchFecha(jobs, fecha, low, high, primera)

    else: 
        if primera:
            return pos+1
        else:
            return pos   
        
def searchJob_byID(lst, ID):
    """searchJob_byID es la MASCARA para la busqueda recursiva, recibe el
    data structure y el id a buscar y prepara las condiciones para la recursion

    Args:
        data_struct (dict): el data_struct
        ID (str): la fecha buscada

    Returns:
        el diccionario del job buscado, o -1 si no existe
    """
    
    idx=recursiveSearchJob_byID(lst, ID, 0, lt.size(lst)-1)
    
    if idx==-1:
        return -1
    else:
        return lt.getElement(lst, idx+1)


def recursiveSearchJob_byID(lst, ID, low, high):
    """recursiveSearchJob_byID ejecuta recursivamente la busqueda binaria
    del trabajo en la lista, si no lo encuentra retorna -1, utiliza la
    llave "id" para la comparacion

    Args:
        jobs (ADT List): lista de trabajos 
        ID (str): id de la oferta que se busca
        low (int): rango inferior de busqueda
        high (int): rango superior de busqueda

    Returns:
        int: indice del trabajo en la lista. 
    """

    pos=(high+low)//2
    
    if low<=high:
        #print(type(lst['elements'][pos]['id']), lst['elements'][pos]['id'])

        if ID==(lst['elements'][pos]['id']):
            return pos
        
        elif lst['elements'][pos]['id'] > ID:
            high=pos-1
            return recursiveSearchJob_byID(lst, ID, low, high)
            
        elif lst['elements'][pos]['id'] < ID:
            low=pos+1
            return recursiveSearchJob_byID(lst, ID, low, high)

    else: 
        return -1

def searchJob_byIDSkill(lst, ID):
    """searchJob_byID es la MASCARA para la busqueda recursiva, recibe el
    data structure y el id a buscar y prepara las condiciones para la recursion

    Args:
        data_struct (dict): el data_struct
        ID (str): la fecha buscada

    Returns:
        el diccionario del job buscado, o -1 si no existe
    """
    
    idx=recursiveSearchJob_byIDSkill(lst, ID, 0, lt.size(lst)-1)
    
    if idx==-1:
        return -1
    else:
        skills=lt.newList("ARRAY_LIST")
        first=idx+1
        while lt.getElement(lst, first)["id"]==ID:
            lt.addLast(skills, lt.getElement(lst, first))
            first+=1
            
        return skills 


def recursiveSearchJob_byIDSkill(lst, ID, low, high):
    """recursiveSearchJob_byID ejecuta recursivamente la busqueda binaria
    del trabajo en la lista, si no lo encuentra retorna -1, utiliza la
    llave "id" para la comparacion

    Args:
        jobs (ADT List): lista de trabajos 
        ID (str): id de la oferta que se busca
        low (int): rango inferior de busqueda
        high (int): rango superior de busqueda

    Returns:
        int: indice del trabajo en la lista. 
    """

    pos=(high+low)//2
    
    if low<=high:
        #print(type(lst['elements'][pos]['id']), lst['elements'][pos]['id'])

        if ID==(lst['elements'][pos]['id']):
            return pos
        
        elif lst['elements'][pos]['id'] > ID:
            high=pos-1
            return recursiveSearchJob_byIDSkill(lst, ID, low, high)
            
        elif lst['elements'][pos]['id'] < ID:
            low=pos+1
            return recursiveSearchJob_byIDSkill(lst, ID, low, high)

    else: 
        return -1







# Funciones de ordenamiento


def cmp_ofertas_by_empresa_y_fecha (oferta1, oferta2):
    if  oferta1["company_name"] == oferta2["company_name"]:
        return oferta1["published_at"] < oferta2["published_at"]
    return oferta1["company_name"] < oferta2["company_name"]


def sortCrit_JobDates(job1,job2):
    if job1['published_at']< job2['published_at']:
        return True
    elif job1['published_at']> job2['published_at']:
        return False
def sortJobsdate_min(oferta1, oferta2):
    oferta1= datetime.strptime(data_1["date"], "%Y-%m-%d")
    

def sortCrit_Cities_MayorMenor(job1,job2):
    """El sort crit de las ciudades de trabajo que ordena de orden anti-alfabéticamente"""
    if job1['city']> job2['city']:
        return True
    elif job1['city']< job2['city']:
        return False

def sortCrit_Cities_MenorMayor(job1,job2):
    """El sort crit de las ciudades de trabajo que ordena de orden anti-alfabéticamente"""
    if job1['city']< job2['city']:
        return True
    elif job1['city']> job2['city']:
        return False

def sortCrit_companyName_MayorMenor(job1,job2):
    """El sort crit de las ciudades de trabajo que ordena de orden anti-alfabéticamente"""
    if job1['company_name']> job2['company_name']:
        return True
    elif job1['company_name']< job2['company_name']:
        return False
    
def sortCrit_companyName_MenorMayor(job1,job2):
    """El sort crit de las ciudades de trabajo que ordena de orden alfabéticamente"""
    if job1['company_name']< job2['company_name']:
        return True
    elif job1['company_name']> job2['company_name']:
        return False
    

def sort_crit_sizeListas_MayorMenor(list1,list2):
    """El sort crit de los tamaños de listas"""
    if list1['size']> list2['size']:
        return True
    elif list1['size']< list2['size']:
        return False

def sort_crit_Paises_MenorMayor(job1,job2):
    """El sort crit de por orden alfabetico paises"""
    if job1['country_code']< job2['country_code']:
        return True
    elif job1['country_code']> job2['country_code']:
        return False

def sortCrit_ID_MenorMayor(job1,job2):
    if job1['id']< job2['id']:
        return True
    elif job1['id']> job2['id']:
        return False
    
def sortCrit_expLevel_MenorMayor(job1,job2):
     if job1['experience_level']< job2['experience_level']:
        return True
     elif job1['experience_level']> job2['experience_level']:
        return False
    
def sortCrit_skillName_MenorMayor(job1, job2):
    if job1['name']< job2['name']:
        return True
    elif job1['name']> job2['name']:
        return False

def sortJobsDate(data_struct):
    """
    Función encargada de ordenar la lista con los datos
    """
    data_struct['jobs']=sort_algorithm.sort(data_struct['jobs'], sortCrit_JobDates)
  
    return data_struct['jobs']

def sort_EmploymentTypes(data_struct):
    data_struct["employment_types"]=shs.sort(data_struct['employment_types'], sortCrit_ID_MenorMayor)
    return data_struct['employment_types']

def sortMultilocation_resumido(data_struct):
    data_struct["multilocation_resumido"]=shs.sort(data_struct['multilocation_resumido'], sortCrit_ID_MenorMayor)
    return data_struct["multilocation_resumido"]

def sort_loadSkills(data_struct):
    data_struct["skills"]=shs.sort(data_struct['skills'], sortCrit_ID_MenorMayor)
    return data_struct["skills"]

def selectSortAlgorithm(picked):
    sort_algorithm = None
    mensaje_picked = None

    # selecciona el algoritmo de ordenamiento
    # opcion 1: Selection Sort
    if picked == 1:
        sort_algorithm = ses
        mensaje_picked = "Seleccionó la configuración - Selection Sort"

    # opcion 2: Insertion Sort
    elif picked == 2:
        sort_algorithm = ins
        mensaje_picked = "Seleccionó la configuración - Insertion Sort"

    # opcion 3: Shell Sort
    elif picked == 3:
        sort_algorithm = shs
        mensaje_picked = "Seleccionó la configuración - Shell Sort"

    # opcion 4: Merge Sort
    elif picked == 4:
        sort_algorithm = mes
        mensaje_picked = "Seleccionó la configuración - Merge Sort"

    # opcion 5: Quick Sort
    elif picked == 5:
        sort_algorithm = qus
        mensaje_picked = "Seleccionó la configuración - Quick Sort"

    # opcion 6: Heap Sort
    elif picked == 6:
        sort_algorithm = hes
        mensaje_picked = "Seleccionó la configuración - Heap Sort"

    # opcion 7: Bogo Sort
    elif picked == 7:
        sort_algorithm = bos
        mensaje_picked = "Seleccionó la configuración - Bogo Sort"

    # opcion 6: Custom Sort, timsort o bucketsort
    elif picked == 8:
        sort_algorithm = cus
        mensaje_picked = "Seleccionó la configuración - Custom Sort (Tim)"
    # respuesta final: algoritmo de ordenamiento y texto de configuracion
        
    return sort_algorithm, mensaje_picked