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

import datetime
import config as cf
#from forex_python.converter import CurrencyRates
from currency_converter import CurrencyConverter
from DISClib.ADT import list as lt
from DISClib.ADT import stack as st
from DISClib.ADT import queue as qu
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.Algorithms.Sorting import insertionsort as ins
from DISClib.Algorithms.Sorting import selectionsort as se
from DISClib.Algorithms.Sorting import mergesort as merg
from DISClib.Algorithms.Sorting import quicksort as quk
from DISClib.Algorithms.Sorting import customsort as tm
assert cf
from datetime import datetime 


"""
Se define la estructura de un catálogo de videos. El catálogo tendrá
dos listas, una para los videos, otra para las categorias de los mismos.
"""

# Construccion de modelos
c = CurrencyConverter()
global_TAD = "ARRAY_LIST"
global_sort = quk

def new_data_structs():
    """
    Inicializa las estructuras de datos del modelo. Las crea de
    manera vacía para posteriormente almacenar la información.
    """
    #TODO: Inicializar las estructuras de datos
    catalog = {'employments_types': None,
               'jobs': None,
               'multilocations': None,
               'skills': None}

    catalog['employments_types'] = lt.newList(global_TAD)
    catalog['jobs'] = lt.newList(global_TAD)
    catalog['multilocations'] = lt.newList(global_TAD)
    catalog['skills'] = lt.newList(global_TAD)

    return catalog

def changeGlobalTAD(TAD):
    global global_TAD
    global_TAD = TAD

def changeGlobalSort(selection):
    global global_sort
    if selection == 1:
    
        global_sort = sa
    elif selection == 2:
        global_sort = ins
    elif selection == 3:
        global_sort = se
    elif selection == 4:
        global_sort = merg
    elif selection == 5:
        global_sort = quk
    else:
        global_sort = tm
    

# Funciones para agregar informacion al modelo
def recurLoadData(lst,i,f, file):
    #Divido entre cuatro la longitud de la lista porque sino supera el límite de recursión lo excede pero esta bien implementado
    if i < f//4:
        add_data(lst, file[i])
        recurLoadData(lst, i+1,f, file)
    else:
        return None

def add_data(data_structs, data):
    """
    Función para agregar nuevos elementos a la lista
    """
    
    #TODO: Crear la función para agregar elementos a una lista
    lt.addLast(data_structs, data)
    return data_structs
    
    

def add_employment_type(data_structs, data):
    """
    Agrega un tipo de empleo al final de la estrutura utilizando
    la funcion addLast
    """
    lt.addLast(data_structs['employments_types'], data)
    return data_structs

def add_job(data_structs, data):
    """
    Agrega un trabajo al final de la estrutura utilizando
    la funcion addLast
    """
    lt.addLast(data_structs['jobs'], data)
    return data_structs

def add_multilocations(data_structs, data):
    """
    Agrega una locacion al final de la estructura utilizando
    la funcion addLast
    """
    lt.addLast(data_structs['multilocations'], data)
    return data_structs

def add_skills(data_structs, data):
    """
    Agrega una habilidad al final de la estructura utilizando
    la funcion addLast
    """
    lt.addLast(data_structs['skills'], data)
    return data_structs

def three_first_last(data_structs, name):
    first_three = lt.subList(data_structs[name], 1, 3)
    last_three = lt.subList(data_structs[name],data_structs[name]["size"]-3,3)
    return first_three, last_three
    
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
|   """

    #fecha1 = datetime.datetime.strptime(oferta1["published_at"][:10],"%Y-%m-%d")
    #fecha2 = datetime.datetime.strptime(oferta2["published_at"][:10],"%Y-%m-%d")
    Y1,M1,D1 = oferta1["published_at"].split("-")
    Y1 = int(Y1)
    M1 = int(M1)
    D1 = int(D1[:2])
    Y2,M2,D2 = oferta2["published_at"].split("-")
    Y2 = int(Y2)
    M2 = int(M2)
    D2 = int(D2[:2])
    
    if oferta1["company_name"].strip() < oferta2["company_name"].strip():
        return True
    elif oferta1["company_name"].strip() == oferta2["company_name"].strip():
        """
        if fecha1.year < fecha2.year and fecha1.month < fecha2.month and fecha1.day < fecha2.day:
            return True
        elif fecha1.year > fecha2.year and fecha1.month > fecha2.month and fecha1.day > fecha2.day:
            return False
        else:
            return True
        
        """
        
        if Y1 < Y2:
            return True
        elif Y1 > Y2:
            return False
        else:
            if M1 < M2:
                return True
            elif M1 > M2:
                return False
            else:
                if D1 < D2:
                    return True
                elif D1 > D2:
                    return False
                else:
                    return True
                    
        
        #return True
    else:
        return False
        
def  evalRatings(book1, book2):
    # TODO modificar operador de comparacion del lab 5
    return (float(book1["id"]) < float(book2["id"]))

def sort_jobs(jobs):
    global_sort.sort(jobs, cmp_ofertas_by_empresa_y_fecha)
    #print("\n ----------------------------------\n")
    #conteo = 0
    #for i in lt.iterator(jobs):
    #    conteo +=1
    #    if conteo < 100:
    #        print(i["company_name"])
    #print("\n ----------------------------------\n")
    #print("IntelligINTS" > "Droptica")
    
# Funciones para creacion de datos


def new_data(id, info):
    """
    Crea una nueva estructura para modelar los datos
    """
    #TODO: Crear la función para estructurar los datos
    


# Funciones de consulta

def get_data(data_structs, id):
    """
    Retorna un dato a partir de su ID
    """
    #TODO: Crear la función para obtener un dato de una lista
    pass


def data_size(data_structs, name):
    """
    Retorna el tamaño de la lista de datos
    """
    #TODO: Crear la función para obtener el tamaño de una lista
    return lt.size(data_structs[name])


def req_1(data_structs):
    """
    Función que soluciona el requerimiento 1
    """
    # TODO: Realizar el requerimiento 1
    pass


def req_2(data_structs, offer_number, company_name, city):
    """
    Función que soluciona el requerimiento 2
    """
    # TODO: Realizar el requerimiento 2
    lista = lt.newList("ARRAY_LIST")
    for offer in lt.iterator(data_structs):
        if offer["company_name"]==company_name:
            if offer["city"]==city:
                lt.addLast(lista, offer)
    if lt.size(lista)>= (int(offer_number)):
        return lt.subList(lista, 1, int(offer_number))
    else:
        return None


def req_3(data_structs):
    """
    Función que soluciona el requerimiento 3
    """
    # TODO: Realizar el requerimiento 3
    pass


def req_4(data_structs, codigo_pais,fecha_inicial, fecha_final):
    """
    Función que soluciona el requerimiento 4
    """
    # TODO: Realizar el requerimiento 4
    
    YearIn,MonthIn,DayIn = map(int, fecha_inicial.split("-"))
    YearFin,MonthFin,DayFin = map(int, fecha_final.split("-"))
    
    lstJobsFit = lt.newList("ARRAY_LIST")
    
    empresas = {}
    ciudades = {}
    
    empresa_base = None
    ciudad_base = None
    
    for job_offer in lt.iterator(data_structs["jobs"]):
        Y,M,D = job_offer["published_at"].split("-")
        Y = int(Y)
        M = int(M)
        D= int(D[:2])
        
        
        if (Y >= YearIn and M >= MonthIn and D >= DayIn) and (Y<=YearFin and M <= MonthFin and D <= DayFin) and (job_offer["country_code"] == codigo_pais):
            lt.addLast(lstJobsFit, job_offer)
            
            
            if job_offer["company_name"] not in empresas:

                empresas[job_offer["company_name"]] = 0
                
            if job_offer["city"] not in ciudades:
                ciudades[job_offer["city"]] = 0

            
            empresa_base = job_offer["company_name"]
            ciudad_base = job_offer["city"]
            empresas[job_offer["company_name"]] += 1
            ciudades[job_offer["city"]] += 1
            

    max_empresa = max_min_conteo_ofertas(empresas, empresa_base,True)
    min_ciudad = max_min_conteo_ofertas(ciudades, ciudad_base,False)
    sorted_lstJobsFit = quk.sort(lstJobsFit,compare_jobs_fit)
    
    return sorted_lstJobsFit , empresas , ciudades, max_empresa, min_ciudad
            
#               !FUNCIONES ASOCIADAS AL REQUERIMIENTO 4!
#------------------------------------------------------------------------->
def max_min_conteo_ofertas(data_conteo, base, max):
    if max == True:
        empresa = None
        maximo=0
        for key in data_conteo.keys():
            if data_conteo[key] > maximo:
                maximo= data_conteo[key]
                empresa = key
        return (empresa,maximo)
    else:
        ciudad = None
        min = data_conteo[base]
        for key in data_conteo.keys():
            if data_conteo[key] <= min:
                min= data_conteo[key]
                ciudad = key
        return (ciudad,min)
    
def compare_jobs_fit(job1, job2):
    Y1,M1,D1 = job1["published_at"].split("-")
    Y1 = int(Y1)
    M1 = int(M1)
    D1= int(D1[:2])
    Y2,M2,D2 = job2["published_at"].split("-")
    Y2 = int(Y2)
    M2= int(M2)
    D2= int(D2[:2])
    
    if Y1 < Y2:
        return True
    elif Y1 > Y2:
        return False
    else:
        if M1 < M2:
            return True
        elif M1 > M2:
            return False
        else:
            if D1 < D2:
                return True
            elif D1 > D2:
                return False
            else:
                
                if job1["company_name"] < job2["company_name"]:
                    return True
                elif job1["company_name"] > job2["company_name"]:
                    return False
                else:
                    return True
#--------------------------------------------------------------------------^
        


def req_5(data_structs, city, first_date, last_date):
    """
    Función que soluciona el requerimiento 5
    """
    # TODO: Realizar el requerimiento 5
    
    """
    Pasamos y comparamos los datos en formato datetime.datetime para luego agregarlos en nuestro ARRAY-LIST
    Utilizamos el algoritmo de ordenamiento quick sort para organizar las ofertas cronologicamente y les pasamos la funcion de comparacion como parametro, esta 
    organiza cronologicamente y si tienen la misma fecha, organiza alfabeticamente.
    """



    lista = lt.newList("ARRAY_LIST")
    primer_limite = first_date
    primer_limite0= datetime.strptime(primer_limite, "%Y-%m-%d")

    ultimo_limite = last_date
    ultimo_limite0 = datetime.strptime(ultimo_limite, "%Y-%m-%d")
    
    
    for pub in lt.iterator(data_structs):
        if pub["city"]==city:
            
            fecha = pub["published_at"]
            fecha0 = datetime.strptime(fecha, "%Y-%m-%dT%H:%M:%S.%fZ")
            
            

            if primer_limite0 <= fecha0 and fecha0 <= ultimo_limite0:
                lt.addLast(lista, pub)
            
    lista_or = quk.sort(lista,compare_jobs_fit)
                
    return lista_or
                      
        



def req_6(data_structs, N, codigo_pais, lvl_experticia ,fecha_inicial, fecha_final):
    """
    Función que soluciona el requerimiento 6
    """
    # TODO: Realizar el requerimiento 6
    job_offers = lt.newList("ARRAY_LIST")
    
    YearIn,MonthIn,DayIn = map(int, fecha_inicial.split("-"))
    YearFin,MonthFin,DayFin = map(int, fecha_final.split("-"))
    
    newCatalog = {"model":{}}
    
            #           ¡SALARIO POR TIPO DE EMPLEO!
        
    #A partir de aquí hago un diccionario que tenga como llaves el id de un trabajo y como valores debe tener de cuanto a cuanto va el salario

    salario_x_empleo = {}
    for employment_type in lt.iterator(data_structs["employments_types"]):
        if(employment_type["salary_from"]!="") and (employment_type["salary_to"]!=""):
            salario_medio = (float(employment_type["salary_from"]) + float(employment_type["salary_to"]))/2
            salario_x_empleo[employment_type["id"]]=salario_medio
        else:
            salario_x_empleo[employment_type["id"]]=0
            
    #NO DAN CÓDIGO DE PAÍS
    #A partir de aquí se escribe el código en relación a meter todas las ofertas de una ciudad en una lista separada y luego meter todas esas listas en otro ARRAY_LIST
    if codigo_pais == None:
        
        #           ¡SEPARAR OFERTAS POR CIUDAD!
        
        #A partir de aquí hago todo relacionado con jobs para separar ofertas por ciudad
        for job_offer in lt.iterator(data_structs["jobs"]):
            
            Y,M,D = job_offer["published_at"].split("-")
            Y = int(Y)
            M = int(M)
            D= int(D[:2])
        
            if  (job_offer["experience_level"] == lvl_experticia):
                if (Y >= YearIn and M >= MonthIn and D >= DayIn) and (Y<=YearFin and M <= MonthFin and D <= DayFin):
                    job_offer["offer_salary"] = salario_x_empleo[job_offer["id"]]
                    
                    
                    
                    if job_offer["city"] not in newCatalog["model"].keys():
                        newCatalog["model"][job_offer["city"]]=lt.newList("ARRAY_LIST")
                        newCatalog["model"][job_offer["city"]]["belongs_to"] = job_offer["city"]
                        
                        newCatalog["model"][job_offer["city"]]["sum_salary"] = 0
                        newCatalog["model"][job_offer["city"]]["avg_salary"] = 0
                        newCatalog["model"][job_offer["city"]]["cant_ofertas_con_salario"] = 0
                        
                        newCatalog["model"][job_offer["city"]]["empresas_presentes"] = []
                        
                       
                    
                    if job_offer["company_name"] not in newCatalog["model"][job_offer["city"]]["empresas_presentes"]:
                        newCatalog["model"][job_offer["city"]]["empresas_presentes"].append(job_offer["company_name"])
                    if    salario_x_empleo[job_offer["id"]] != 0:
                        newCatalog["model"][job_offer["city"]]["cant_ofertas_con_salario"] +=1
                        newCatalog["model"][job_offer["city"]]["sum_salary"] += salario_x_empleo[job_offer["id"]]
                    
                    lt.addLast(newCatalog["model"][job_offer["city"]], job_offer)
    
    else:
        #SÍ DAN CÓDIGO DE PAÍSES

        
        #           ¡SEPARAR OFERTAS POR CIUDAD!
        
        #A partir de aquí hago todo relacionado con jobs para separar ofertas por ciudad
        for job_offer in lt.iterator(data_structs["jobs"]):
            
            Y,M,D = job_offer["published_at"].split("-")
            Y = int(Y)
            M = int(M)
            D= int(D[:2])
        
            if  (job_offer["experience_level"] == lvl_experticia) and (job_offer["country_code"] == codigo_pais):
                if (Y >= YearIn and M >= MonthIn and D >= DayIn) and (Y<=YearFin and M <= MonthFin and D <= DayFin):
                    job_offer["offer_salary"] = salario_x_empleo[job_offer["id"]]
                    
                    
                    
                    if job_offer["city"] not in newCatalog["model"].keys():
                        newCatalog["model"][job_offer["city"]]=lt.newList("ARRAY_LIST")
                        newCatalog["model"][job_offer["city"]]["belongs_to"] = job_offer["city"]
                        
                        newCatalog["model"][job_offer["city"]]["sum_salary"] = 0
                        newCatalog["model"][job_offer["city"]]["avg_salary"] = 0
                        newCatalog["model"][job_offer["city"]]["cant_ofertas_con_salario"] = 0
                        
                        newCatalog["model"][job_offer["city"]]["empresas_presentes"] = []
                        
                       
                    
                    if job_offer["company_name"] not in newCatalog["model"][job_offer["city"]]["empresas_presentes"]:
                        newCatalog["model"][job_offer["city"]]["empresas_presentes"].append(job_offer["company_name"])
                    if    salario_x_empleo[job_offer["id"]] != 0:
                        newCatalog["model"][job_offer["city"]]["cant_ofertas_con_salario"] +=1
                        newCatalog["model"][job_offer["city"]]["sum_salary"] += salario_x_empleo[job_offer["id"]]
                    
                    lt.addLast(newCatalog["model"][job_offer["city"]], job_offer)
                   
        
        #           ¡PROCESAR LAS CIUDADES Y TRANSFORMALAS EN ARRAY_LIST PARA PODER USAR EL SORT!
        
    data = convertir_dict_TAD(newCatalog)
        
    encontrar_promedio_ofertas_ciudad(data)
        
        #sorted_list = quk.sort(data,compare_conteo_ciudades)
    sorted_list = sa.sort(data,compare_ciudades)
    for city in lt.iterator(sorted_list):
        sa.sort(city,compare_ofertas_en_ciudades)
        
        """
        for city in lt.iterator(sorted_list):
           print(city["size"])
           print(city["belongs_to"])
           print(city["avg_salary"])
        """
    
    if lt.size(sorted_list) < N:
        return lt.subList(sorted_list,1,lt.size(sorted_list))
    
    else:
        return lt.subList(sorted_list,1,N)

    #¡FUNCIONES ASOCIADAS AL REQUERIMIENTO 6!
    #..................................................................>
    
def encontrar_promedio_ofertas_ciudad(data):
    
    for city in lt.iterator(data):
        #city["avg_salary"] = city["sum_salary"]/lt.size(city)
        if city["cant_ofertas_con_salario"] != 0:
            city["avg_salary"] = city["sum_salary"]/city["cant_ofertas_con_salario"]
        else:
            city["avg_salary"] = 0
        
        
def convertir_dict_TAD(newCatalog):
    data = lt.newList("ARRAY_LIST")
    for key in newCatalog["model"].keys():
        lt.addLast(data, newCatalog["model"][key])
        
    return data
    
    
def compare_ciudades(ciudad1,ciudad2):
    if int(lt.size(ciudad1)) < int(lt.size(ciudad2)):
        return False
    elif int(lt.size(ciudad1)) > int(lt.size(ciudad2)):
        return True
    else:
        if int(ciudad1["avg_salary"]) < int(ciudad2["avg_salary"]):
            return False
        elif int(ciudad1["avg_salary"]) > int(ciudad2["avg_salary"]):
            return True
        else:
            return False
        
        
def compare_ofertas_en_ciudades(oferta1, oferta2):
    if int(oferta1["offer_salary"]) < int(oferta2["offer_salary"]):
        return False
    elif int(oferta1["offer_salary"]) > int(oferta2["offer_salary"]):
        return True
    
        
def manipular_NJobOffers_req6(NJobOffers):
    total_ciudades= lt.size(NJobOffers)
    total_empresas= []
    total_ofertas=0
    avg_salary_total_offers = 0
    
    for city in lt.iterator(NJobOffers):
        total_ofertas += city["cant_ofertas_con_salario"]
        
        total_empresas += city["empresas_presentes"]
    
    
    
    for city in lt.iterator(NJobOffers):
        avg_salary_total_offers += city["avg_salary"]/total_ciudades
    
    nombre_ciudad_mayor = NJobOffers["elements"][0]["belongs_to"]
    conteo_ciudad_mayor = lt.size(NJobOffers["elements"][0])
    
    nombre_ciudad_menor = NJobOffers["elements"][total_ciudades-1]["belongs_to"]
    conteo_ciudad_menor = lt.size(NJobOffers["elements"][total_ciudades-1])
    
    for city in lt.iterator(NJobOffers):
        city["oferta_mayor"] = (city["elements"][0]["company_name"],city["elements"][0]["offer_salary"])
        city["oferta_menor"] = (city["elements"][lt.size(city)-1]["company_name"],city["elements"][lt.size(city)-1]["offer_salary"])
    
    return total_ciudades,len(set(total_empresas)),total_ofertas, avg_salary_total_offers,nombre_ciudad_mayor, conteo_ciudad_mayor, nombre_ciudad_menor, conteo_ciudad_menor
    
    #^.............................................................................^





def req_7(data_structs, country_number, first_date, last_date ):
    """
    Función que soluciona el requerimiento 7
    """
    # TODO: Realizar el requerimiento 7
    listax = lt.newList("ARRAY_LIST")
    dicc_country = {}
    conteo_countries= {}
    dicc_final = {}
    dicc_experience = {}
    lista_final = lt.newList("ARRAY_LIST")
    first = datetime.strptime(first_date, "%Y-%m-%d")
    last = datetime.strptime(last_date, "%Y-%m-%d")
    
    """
    Tomamos el ARRAY-LIST original y guardamos las ofertas de trabajo por pais en un diccionario 
    y otro diccionario que contenga el pais y el numero de ofertas de trabajo.
    
    Al diccionario de pais X numero de ofertas de trabajo lo pasamos a otro diccionario con solo los N paises que
    nos pidio el usuario.
    
    Unimos todo en un ARRAY-LIST el cual tendra como condicion que el pais se encuentre en el diccionario de N paises, despues pasara 
    toda la informacion de ofertas X pais a ese ARRAY-LIST
    
    Despues de obtener la ultima version del ARRAY-LIST buscamos en ella los tres niveles de experticia solicitados y los vamos organizando en otro diccionario,
    donde la llave sera el nivel de experticia y el valor sera otro diccionario con el nivel de experiencia-numero de veces que se repitio.
    """

    
    for cn in lt.iterator(data_structs["jobs"]):
        fecha = cn["published_at"]
        fecha0= datetime.strptime(fecha, "%Y-%m-%dT%H:%M:%S.%fZ")
        
        
        if first <= fecha0 and fecha0 <= last:
            lt.addLast(listax, cn)
            
            
        
            
            if cn["country_code"]not in dicc_country:
                lista = []
                lista.append(cn)
                dicc_country[cn["country_code"]] = lista
                
            else:
                dicc_country[cn["country_code"]].append(cn)
                
            if cn["country_code"]not in conteo_countries:
                conteo_countries[cn["country_code"]]=1
            else:
                
                conteo_countries[cn["country_code"]]+=1
                
                
            
                
                
    if len(conteo_countries)>0:
        for i in range(int(country_number)):
            if len(conteo_countries)>0:
                maximo = max(conteo_countries.values())
                for i in conteo_countries.items():
                    if i[1]==maximo:
                        nombre_maximo = i[0]
                dicc_final[nombre_maximo]=maximo
                conteo_countries.pop(nombre_maximo)
            
    for i in dicc_country.items():
        if i[0] in dicc_final:
            for j in i[1]:
                lt.addLast(lista_final, j)
        
        
        
        
        
        
    for i in lt.iterator(lista_final):
        
        if "junior" == i["experience_level"]:
            
            
            if i["experience_level"] not in dicc_experience:
                dicc_sec = {}
                dicc_experience["junior"] = dicc_sec
            else:
                dicc_sec = dicc_experience["junior"]
                #dicc_experience[i["experience_level"]] = dicc_sec
            
            for j in lt.iterator(data_structs["skills"]):
                if i["id"] == j["id"]:
                    if j["name"] not in dicc_sec:
                        dicc_sec[j["name"]] = 1
                    else:
                        dicc_sec[j["name"]] += 1
            dicc_experience["junior"] = dicc_sec
            #print(dicc_experience)

        if "mid" == i["experience_level"]:
            

            if i["experience_level"] not in dicc_experience:
                dicc_sec1 = {}
                dicc_experience["mid"] = dicc_sec1
            else:
                dicc_sec1 = dicc_experience["mid"]
                #dicc_experience[i["experience_level"]] = dicc_sec1
            
                
            for j in lt.iterator(data_structs["skills"]):
                if i["id"] == j["id"]:
                
                    if j["name"] not in dicc_sec1:
                        dicc_sec1[j["name"]] = 1
                    else:
                        dicc_sec1[j["name"]] += 1
            dicc_experience["mid"] = dicc_sec1
            #print(dicc_experience)
        
        if "senior" == i["experience_level"]:
            

            if i["experience_level"] not in dicc_experience:
                dicc_sec2 = {}
                dicc_experience["senior"] = dicc_sec2
            else:
                dicc_sec2 = dicc_experience["senior"]
                #dicc_experience[i["experience_level"]] = dicc_sec2
                
                
            for j in lt.iterator(data_structs["skills"]):
                if i["id"] == j["id"]:
                    if j["name"] not in dicc_sec2:
                        dicc_sec2[j["name"]] = 1
                    else:
                        dicc_sec2[j["name"]] += 1
            dicc_experience["senior"] = dicc_sec2
            #print(dicc_experience)
    
    #print(dicc_experience)                

       
    

    return lista_final, dicc_final, dicc_experience

        
        
    
        
        




def req_8(data_structs,fecha_inicial, fecha_final, lvl_experticia):
    """
    Función que soluciona el requerimiento 8
    """
    # TODO: Realizar el requerimiento 8
    job_offers = lt.newList("ARRAY_LIST")
    
    YearIn,MonthIn,DayIn = map(int, fecha_inicial.split("-"))
    YearFin,MonthFin,DayFin = map(int, fecha_final.split("-"))
    
    
    newCatalog = {"model":{}}
    
            #           ¡SALARIO POR TIPO DE EMPLEO!
        
    #A partir de aquí hago un diccionario que tenga como llaves el id de un trabajo y como valores debe tener de cuanto a cuanto va el salario

    salario_x_empleo = {}
    #salario_x_empleo["salarios_fijos"] = []
    
    for employment_type in lt.iterator(data_structs["employments_types"]):
        if(employment_type["salary_from"]!="") and (employment_type["salary_to"]!=""):
            fijo = False
            if float(employment_type["salary_from"]) == float(employment_type["salary_to"]):
                fijo = True
            
            salario_medio = (float(employment_type["salary_from"]) + float(employment_type["salary_to"]))/2
            nuevo_salario = convertir_divisas(salario_medio, employment_type["currency_salary"])
            
            salario_x_empleo[employment_type["id"]]=(nuevo_salario,fijo, employment_type["currency_salary"])
        else:
            salario_x_empleo[employment_type["id"]]=(0, None, None)
    
    
    habilidades_x_empleo = {}
    divisas=[]
    
    for skill in lt.iterator(data_structs["skills"]):
        habilidades_x_empleo[skill["id"]] = float(skill["level"])
    conteoBorrar = 0
    for job_offer in lt.iterator(data_structs["jobs"]):
            
            Y,M,D = job_offer["published_at"].split("-")
            Y = int(Y)
            M = int(M)
            D= int(D[:2])
            
            if  (job_offer["experience_level"] == lvl_experticia):
                if (Y >= YearIn and M >= MonthIn and D >= DayIn) and (Y<=YearFin and M <= MonthFin and D <= DayFin):
                    
                    job_offer["offer_salary"] = salario_x_empleo[job_offer["id"]][0]
                    job_offer["divisa"] =  salario_x_empleo[job_offer["id"]][2]
                    
                    if job_offer["city"] not in newCatalog["model"].keys():
                        
                        newCatalog["model"][job_offer["city"]]=lt.newList("ARRAY_LIST")
                        newCatalog["model"][job_offer["city"]]["belongs_to"] = job_offer["city"]
                        
                        newCatalog["model"][job_offer["city"]]["sum_salary"] = 0
                        newCatalog["model"][job_offer["city"]]["avg_salary"] = 0
                        newCatalog["model"][job_offer["city"]]["cant_ofertas_con_salario"] = 0
                        newCatalog["model"][job_offer["city"]]["cant_ofertas_con_salario_fijo"] = 0
                        newCatalog["model"][job_offer["city"]]["cant_ofertas_sin_salario"] = 0
                        
                        newCatalog["model"][job_offer["city"]]["country"] = job_offer["country_code"]
                        newCatalog["model"][job_offer["city"]]["divisa"] =  salario_x_empleo[job_offer["id"]][2]
                        
                        newCatalog["model"][job_offer["city"]]["divisas_ciudad"] = {}
                        
                        
                        newCatalog["model"][job_offer["city"]]["empresas_presentes"] = []
                    
                        #
                        newCatalog["model"][job_offer["city"]]["suma_habilidades"] = 0 
                        newCatalog["model"][job_offer["city"]]["cant_habilidades"] = 0
                        
                    if job_offer["divisa"] != None:
                        newCatalog["model"][job_offer["city"]]["divisas_ciudad"][job_offer["divisa"]] = 0
                    if job_offer["company_name"] not in newCatalog["model"][job_offer["city"]]["empresas_presentes"]:
                        newCatalog["model"][job_offer["city"]]["empresas_presentes"].append(job_offer["company_name"])
                    #
                    newCatalog["model"][job_offer["city"]]["suma_habilidades"] += habilidades_x_empleo[job_offer["id"]] 
                    newCatalog["model"][job_offer["city"]]["cant_habilidades"] += 1
                    
                    
                    if    salario_x_empleo[job_offer["id"]][0] != 0:
                        newCatalog["model"][job_offer["city"]]["divisa"] =  job_offer["divisa"]
                        if salario_x_empleo[job_offer["id"]][1] == False:  
                            
                            newCatalog["model"][job_offer["city"]]["cant_ofertas_con_salario"] +=1
                            
                        else:
                            
                            newCatalog["model"][job_offer["city"]]["cant_ofertas_con_salario_fijo"] +=1
                        
                        
                        newCatalog["model"][job_offer["city"]]["sum_salary"] += salario_x_empleo[job_offer["id"]][0]
                        
                    else:
                        
                        newCatalog["model"][job_offer["city"]]["cant_ofertas_sin_salario"] += 1
                    if newCatalog["model"][job_offer["city"]]["divisa"] not in divisas and newCatalog["model"][job_offer["city"]]["divisa"] != None:
                            divisas.append(newCatalog["model"][job_offer["city"]]["divisa"])
                            
                    lt.addLast(newCatalog["model"][job_offer["city"]], job_offer)
                    
    """           
    print(f"{conteoBorrar} CONTEO BORRAR")
    borrar5 = []
    for key in newCatalog["model"].keys():
        if newCatalog["model"][key]["divisa"] == "usd":
            print(f"porfavor mira este punto")
        if newCatalog["model"][key]["divisa"] not in borrar5:
            borrar5.append(newCatalog["model"][key]["divisa"])
    """
    data = convertir_dict_TAD(newCatalog)
    encontrar_promedio_ofertas_ciudad(data)
    
    sorted_list = sa.sort(data,compare_ciudades)
    for city in lt.iterator(sorted_list):
        sa.sort(city,compare_ofertas_en_ciudades)
    
    
    
    
    return sorted_list , divisas

#               FUNCIONES ASOCIADAS AL REQUERIMIENTO 8
#-------------------------------------------------------------------------------------------------
def convertir_divisas(salario_a_convertir, divisa):
    #print(divisa)
    
    if divisa == "usd":
        return salario_a_convertir
    else:
        
        divisa = str.upper(divisa)
        salario_convertido = c.convert(salario_a_convertir, divisa, 'USD')
        #print(salario_a_convertir)
        return salario_convertido
    
      
def manipular_data_req8(data):  
    total_empresas= []
    
    paises = {"model":{}}
    ofertas_rango_salarial = 0
    ofertas_fijas = 0
    ofertas_sin_salario = 0
    avg_salary_total_offers = 0
    borrar1= []
    
    for city in lt.iterator(data):
        if city["country"] not in paises.keys():
            paises["model"][city["country"]] = lt.newList("ARRAY_LIST")
            paises["model"][city["country"]]["sum_skills"] = 0
            paises["model"][city["country"]]["país"] = city["country"]
            paises["model"][city["country"]]["sum_avg_salaries"] = 0
            
        avg_salary_total_offers += city["avg_salary"]/lt.size(data)
        
        city["promedio_habilidades"] = city["suma_habilidades"]/city["cant_habilidades"]
        
        #print(city["promedio_habilidades"])
        total_empresas += city["empresas_presentes"]
        ofertas_rango_salarial += city["cant_ofertas_con_salario"]
        ofertas_fijas += city["cant_ofertas_con_salario_fijo"]
        ofertas_sin_salario += city["cant_ofertas_sin_salario"]
        #print(city["divisa"])
        lt.addLast(paises["model"][city["country"]],city)
        paises["model"][city["country"]]["sum_skills"] += city["promedio_habilidades"]
        paises["model"][city["country"]]["sum_avg_salaries"] += avg_salary_total_offers
    paises = convertir_dict_TAD(paises)
    

    
    total_ofertas = ofertas_rango_salarial + ofertas_fijas + ofertas_sin_salario
    total_paises = lt.size(paises)
    total_ciudades = lt.size(data)
    
    
    for pais in lt.iterator(paises):
        pais["avg_skills"] = pais["sum_skills"] / lt.size(pais)
        pais["avg_salary"] = pais["sum_avg_salaries"]/lt.size(pais)
        
    global_sort.sort(paises, sort_crit_req8)
    
    
    return len(total_empresas),ofertas_rango_salarial,ofertas_fijas,ofertas_sin_salario,total_ofertas,total_paises,total_ciudades, paises
        
def sort_crit_req8(pais1, pais2):
    if pais1["sum_avg_salaries"] < pais2["sum_avg_salaries"]:
        return False
    elif pais1["sum_avg_salaries"] > pais2["sum_avg_salaries"]: 
        return True
    else:
        if pais1["país"] < pais2["país"]:
            return False
        elif pais1["país"] > pais2["país"]:
            return True
        else:
            return False

def resultados_pais(paises, ultimo):
    if ultimo == True:
        pais_menor = lt.lastElement(paises)
        total_ofertas = 0
        avg_salary_total_offers = 0
        empresas_presentes = {}
        oferta_mayor = None
        oferta_menor = None
        cantidad_divisas_pais = 0
        for city in lt.iterator(pais_menor):
            if oferta_menor == None and lt.getElement(city, city["cant_ofertas_con_salario"]+city["cant_ofertas_con_salario_fijo"])["offer_salary"] != 0:
                oferta_menor = lt.getElement(city, city["cant_ofertas_con_salario"]+city["cant_ofertas_con_salario_fijo"])["offer_salary"]
            if oferta_mayor == None:
                oferta_mayor = lt.firstElement(city)["offer_salary"]
            total_ofertas += city["cant_ofertas_con_salario"]
            total_ofertas += city["cant_ofertas_con_salario_fijo"]
            total_ofertas +=  city["cant_ofertas_sin_salario"]
        
            avg_salary_total_offers += city["avg_salary"]/lt.size(pais_menor)
            for empresa in city["empresas_presentes"]:
                empresas_presentes[empresa] = 0
            
            nuevo_mayor = lt.firstElement(city)["offer_salary"]
            if nuevo_mayor > oferta_mayor:
                oferta_mayor = nuevo_mayor
            if oferta_menor != None:
                nuevo_menor = lt.getElement(city, city["cant_ofertas_con_salario"]+city["cant_ofertas_con_salario_fijo"])["offer_salary"]
                if nuevo_menor < oferta_menor and nuevo_menor != 0:
                    oferta_menor = nuevo_menor
            #print(f"acáaaaa {lt.getElement(city, city["cant_ofertas_con_salario"]+city["cant_ofertas_con_salario_fijo"]+1)["offer_salary"]}")
            cantidad_divisas_pais += len(city["divisas_ciudad"])
        
                
        return pais_menor["país"],  total_ofertas, avg_salary_total_offers, lt.size(pais_menor), len(empresas_presentes),oferta_mayor, oferta_menor,cantidad_divisas_pais, pais_menor["avg_skills"]
        
    if ultimo == False:
        pais_menor = lt.firstElement(paises)
    
        total_ofertas = 0
        avg_salary_total_offers = 0
        empresas_presentes = {}
        oferta_mayor = None
        oferta_menor = None
        cantidad_divisas_pais = 0
        for city in lt.iterator(pais_menor):
            if oferta_menor == None:
                oferta_menor = lt.getElement(city, city["cant_ofertas_con_salario"]+city["cant_ofertas_con_salario_fijo"])["offer_salary"]
            if oferta_mayor == None:
                oferta_mayor = lt.firstElement(city)["offer_salary"]
            total_ofertas += city["cant_ofertas_con_salario"]
            total_ofertas += city["cant_ofertas_con_salario_fijo"]
            total_ofertas +=  city["cant_ofertas_sin_salario"]
        
            avg_salary_total_offers += city["avg_salary"]/lt.size(pais_menor)
            for empresa in city["empresas_presentes"]:
                empresas_presentes[empresa] = 0
            
            
            nuevo_mayor = lt.firstElement(city)["offer_salary"]
            if nuevo_mayor > oferta_mayor:
                oferta_mayor = nuevo_mayor
            
            nuevo_menor = lt.getElement(city, city["cant_ofertas_con_salario"]+city["cant_ofertas_con_salario_fijo"])["offer_salary"]
            if nuevo_menor < oferta_menor:
                oferta_menor = nuevo_menor
            #print(f"acáaaaa {lt.getElement(city, city["cant_ofertas_con_salario"]+city["cant_ofertas_con_salario_fijo"]+1)["offer_salary"]}")
            
            cantidad_divisas_pais += len(city["divisas_ciudad"])
        
                
        return pais_menor["país"],  total_ofertas, avg_salary_total_offers, lt.size(pais_menor), len(empresas_presentes),oferta_mayor, oferta_menor,cantidad_divisas_pais, pais_menor["avg_skills"]
#-------------------------------------------------------------------------------------------------                   
# Funciones utilizadas para comparar elementos dentro de una lista

def compare(data_1, data_2):
    """
    Función encargada de comparar dos datos
    """
    #TODO: Crear función comparadora de la lista
    pass

# Funciones de ordenamiento


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


def sort(data_structs):
    """
    Función encargada de ordenar la lista con los datos
    """
    #TODO: Crear función de ordenamiento
    pass

