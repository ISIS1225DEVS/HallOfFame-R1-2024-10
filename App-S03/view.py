"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
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
import sys
import controller
from DISClib.ADT import list as lt
from DISClib.ADT import stack as st
from DISClib.ADT import queue as qu
assert cf
from datetime import datetime 
import threading

import traceback
from tabulate import tabulate

"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""


def new_controller():
    """
        Se crea una instancia del controlador
    """
    #TODO: Llamar la función del controlador donde se crean las estructuras de datos
    control =controller.new_controller()
    return control


def print_menu():
    print("Bienvenido")
    print("1- Cargar información")
    print("2- Ejecutar Requerimiento 1")
    print("3- Ejecutar Requerimiento 2")
    print("4- Ejecutar Requerimiento 3")
    print("5- Ejecutar Requerimiento 4")
    print("6- Ejecutar Requerimiento 5")
    print("7- Ejecutar Requerimiento 6")
    print("8- Ejecutar Requerimiento 7")
    print("9- Ejecutar Requerimiento 8")
    print("10- Cambiar estructura de datos con la que se carga el catalogo (ARRAY_LIST/SINGLE_LINKED)")
    print("11- Cambiar el algoritmo de ordenamiento para ordenar la lista de ofertas de trabajo del catalogo")
    print("12- Cambiar el tamaño de la muestra que desea imprimir en consola")
    print("0- Salir")


def load_data(control):
    """
    Carga los datos
    """
    
    #TODO: Realizar la carga de datos
    #carga de datos iterativa
    data , time= controller.load_data(control)
    #Carga de datos recursiva:
    #data= controller.mascaraLoadData(control)
    return data , time


def print_data(control, id):
    """
        Función que imprime un dato dado su ID
    """
    #TODO: Realizar la función para imprimir un elemento
    pass

def print_req_1(control):
    """
        Función que imprime la solución del Requerimiento 1 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 1
    pass


def print_req_2(control, offer_number, company_name, city):
    """
        Función que imprime la solución del Requerimiento 2 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 2
    print("\nCon este requerimiento podrá listar las últimas N ofertas de trabajo por empresa y ciudad.\n")
    offer = controller.req_2(control, offer_number, company_name, city)
    return offer
    


def print_req_3(control):
    """
        Función que imprime la solución del Requerimiento 3 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 3
    pass


def print_req_4(control):
    """
        Función que imprime la solución del Requerimiento 4 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 4
    codigo_pais = input("\nPor favor digite el código del país para el que desea consultar las ofertas de trabajo publicadas en un rango de fechas... ")
    print("\nPor favor digite desde que fecha desea consultar las ofertas publicadas...\n")
    yeari = input("Año... ")
    monthi =  input("Mes... ")
    dayi = input("Día... ")
    
    print("\nPor favor digite hasta que fecha desea consultar las ofertas publicadas... \n")
    yearf = input("Año... ")
    monthf =  input("Mes... ")
    dayf = input("Día... ")

    if len(dayi) == 1:
        dayi = "0"+dayi
    elif len(dayf) == 1:
        dayf = "0"+dayf
    if len(monthi) == 1:
        monthi = "0"+monthi
    elif len(monthf) == 1:
        monthf = "0"+monthf
        
    if int(monthi) >12 or int(monthf) >12:
        print("No hay más de doce meses") 
    else:
        data , empresas , ciudades, delta_time, max_empresa, min_ciudad= controller.req_4(control, codigo_pais,f"{yeari}-{monthi}-{dayi}",f"{yearf}-{monthf}-{dayf}")
        print(f"Ha demorado {delta_time} [ms]")
        print(f"\nHubo un total de {lt.size(data)} ofertas en el país en el periodo de consulta")
        print(f"Un total de {len(empresas)} empresas publicaron al menos una oferta en el país de consulta.")
        print(f"Número total de ciudades del país de consulta en las que se publicaron ofertas: {len(ciudades)}")
        
        print(f"Ciudad del país de consulta con mayor número de ofertas: {max_empresa[0]} con un total de {max_empresa[1]} ofertas")
        print(f"Ciudad del país de consulta con menor número de ofertas: {min_ciudad[0]} con un total de {min_ciudad[1]}")
        
        
    


def print_req_5(control,city, first_date, last_date):
    """
        Función que imprime la solución del Requerimiento 5 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 5
    print("\nCon este requerimiento podrá consultar las ofertas que publicó una empresa durante un periodo especifico de tiempo \n")
    pub = controller.req_5(control,city, first_date, last_date)
    return pub


def print_req_6(control):
    """
        Función que imprime la solución del Requerimiento 6 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 6
    print("\nCon este requerimiento podrá clasficiar N ciudades con mayor cantidad de ofertas de trabajo en un país entre un rango de fechas y nivel de experticia de la oferta.\n")
    N = input("Cúantas ciudades desea clasificar... ")
    respuesta = input("¿Desea consultar algún país en específico? (Si/No) ")
    if respuesta in "No,no,N,n":
        codigo_pais=None
    else:
        codigo_pais = input("Por favor digite el código del país para el que desea realizar la consulta... ")
    
    
    lvl_experticia = input("Por favor digite el nivel de experticia (junior, mid, senior)... ")
    print("\nPor favor digite desde que fecha desea consultar las ofertas publicadas...\n")
    yeari = input("Año... ")
    monthi =  input("Mes... ")
    dayi = input("Día... ")
    
    print("\nPor favor digite hasta que fecha desea consultar las ofertas publicadas... \n")
    yearf = input("Año... ")
    monthf =  input("Mes... ")
    dayf = input("Día... ")

    if len(dayi) == 1:
        dayi = "0"+dayi
    elif len(dayf) == 1:
        dayf = "0"+dayf
    if len(monthi) == 1:
        monthi = "0"+monthi
    elif len(monthf) == 1:
        monthf = "0"+monthf
        
    if int(monthi) >12 or int(monthf) >12:
        print("No hay más de doce meses") 
    else:
        NjobOffers , total_ciudades,total_empresas,total_ofertas, avg_salary_total_offers,nombre_ciudad_mayor, conteo_ciudad_mayor, nombre_ciudad_menor, conteo_ciudad_menor, delta_time = controller.req_6(control, N, codigo_pais, lvl_experticia ,f"{yeari}-{monthi}-{dayi}",f"{yearf}-{monthf}-{dayf}")
        print(f"Ha demorado {delta_time} [ms]")
        print("\nRESULTADOS CONSULTA\n")
        print(f"\nTotal de ciudades que cumplen con las condiciones de la consulta = {total_ciudades}")  
        print(f"Total de empresas que cumplen con las condiciones de la consulta= {total_empresas}")
        print(f"Total de ofertas publicadas que cumplen con las condiciones de la consulta que ofrecen un salario= {total_ofertas}")
        print(f"Promedio del salario ofertado de todas las ofertas que cumplen con las condiciones de la consulta = {avg_salary_total_offers}")
        print(f"Ciudad con mayor cantidad de ofertas de empleos y su conteo = {nombre_ciudad_mayor}, {conteo_ciudad_mayor}")
        print(f"Ciudad con menor cantidad de ofertas de empleos y su conteo = {nombre_ciudad_menor}, {conteo_ciudad_menor}\n")
        #print(NjobOffers)
    


def print_req_7(control, country_number, limite_inicial, limite_final):
    """
        Función que imprime la solución del Requerimiento 7 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 7
    print("\nCon este requerimiento podrá clasificar los N países con mayor número de ofertas de trabajo \n")
    cn = controller.req_7(control, country_number, limite_inicial, limite_final)
    return cn


def print_req_8(control):
    """
        Función que imprime la solución del Requerimiento 8 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 8
    print("\nCon este requerimiento podrá identificar los países con mayores y menores ofertas de trabajo\n")
    print("\nPorfavor diligencie los siguientes datos de consulta\n")

    lvl_experticia = input("Por favor digite el nivel de experticia (junior, mid, senior)... ")
    print("\nPor favor digite desde que fecha desea consultar las ofertas publicadas...\n")
    yeari = input("Año... ")
    monthi =  input("Mes... ")
    dayi = input("Día... ")
    
    print("\nPor favor digite hasta que fecha desea consultar las ofertas publicadas... \n")
    yearf = input("Año... ")
    monthf =  input("Mes... ")
    dayf = input("Día... ")

    if len(dayi) == 1:
        dayi = "0"+dayi
    elif len(dayf) == 1:
        dayf = "0"+dayf
    if len(monthi) == 1:
        monthi = "0"+monthi
    elif len(monthf) == 1:
        monthf = "0"+monthf
        
    if int(monthi) >12 or int(monthf) >12:
        print("No hay más de doce meses") 
    else:
        
        total_empresas, ofertas_rango_salarial,ofertas_fijas,ofertas_sin_salario,total_ofertas,total_paises,total_ciudades, total_divisas, paises, delta_time= controller.req_8(control,lvl_experticia ,f"{yeari}-{monthi}-{dayi}",f"{yearf}-{monthf}-{dayf}")
        print(f"Ha demorado {delta_time} [ms]")
        print("-----------RESULTADOS DE LA CONSULTA GENERAL---------------")
        print(f"\n-El total de empresas para las cuales se cumplio la consulta fueron: {total_empresas}")
        print(f"-El total de ofertas para las cuales se cumplio la consulta fueron: {total_ofertas}")
        print(f"-Dentro de la consulta se clasificaron {total_paises} paises")
        print(f"En la consulta se consideraron un total de {total_ciudades} ciudades")
        print(f"En esta consulta se tuvieron en consideración un total de {total_divisas} divisas diferentes")
        print(f"Ofertas publicadas con rango salarial = {ofertas_rango_salarial}")
        print(f"Ofertas con valor fijo de salario = {ofertas_fijas}")
        print(f"Ofertas sin salario = {ofertas_sin_salario}")
        
        print("\n-----------RESULTADOS DE LA CONSULTA (país con mayor promedio salarial)---------------\n")
        codigo1,total_ofertas_pais1, promedio_salario_ofertado1, numero_ciudades1, numero_empresas1, mayor_salario1, menor_salario1, divisas1, avg_skills1=controller.resultados_pais(paises, True)
        print(f"El código del país con mayor oferta salarial es {codigo1}")
        print(f"Hubo un total de {total_ofertas_pais1} ofertas en este país")
        print(f"El promedio de salario ofertado en este país es {promedio_salario_ofertado1}")
        print(f"El número de ciudades en este país es: {numero_ciudades1}")
        print(f"El número de empresas en este país es: {numero_empresas1}")
        print(f"El mayor salario de este país fue de {mayor_salario1} USD")
        print(f"El menor salario de este país fue de {menor_salario1} USD")
        print(f"En este país hay un total de {divisas1} divisas")
        print(f"El numero de habilidades promedio solicitado por oferta es {avg_skills1}")
        print("\n-----------RESULTADOS DE LA CONSULTA (país con menor promedio salarial)---------------\n")
        
        codigo2,total_ofertas_pais2, promedio_salario_ofertado2, numero_ciudades2, numero_empresas2, mayor_salario2, menor_salario2, divisas2, avg_skills2=controller.resultados_pais(paises, False)
        print(f"El código del país con menor oferta salarial es {codigo2}")
        print(f"Hubo un total de {total_ofertas_pais2} ofertas en este país")
        print(f"El promedio de salario ofertado en este país es {promedio_salario_ofertado2}")
        print(f"El número de ciudades en este país es: {numero_ciudades2}")
        print(f"El número de empresas en este país es: {numero_empresas2}")
        print(f"El mayor salario de este país fue de {mayor_salario2} USD")
        print(f"El menor salario de este país fue de {menor_salario2} USD")
        print(f"En este país hay un total de {divisas2} divisas")
        print(f"El numero de habilidades promedio solicitado por oferta es {avg_skills2}")
        print("----------------------------------------------------------------------------------------\n")
def menu_cycle():
    
    working = True
    #ciclo del menu
    while working:
        print_menu()
        inputs = input('Seleccione una opción para continuar\n')
        if int(inputs) == 1:
            print("Cargando información de los archivos ....\n")
            control = new_controller()
            
            data , time = load_data(control)
            
            
            print(f"La carga de datos se demoro un total de {time}[ms]")
            """
            Imprime los valores de tamaño, los tres primeros y tres ultimos registros
            """
            print("_"*150)
            print("\nEMPLOYMENTS TYPES\n")
            
            
            EmploTypesSize = controller.data_size(data, "employments_types")
            print("Size")
            print(EmploTypesSize)
            firstEmploTypes,lastEmploTypes = controller.three_first_last(data, "employments_types")
            print("\nFirst three elements\n")
            llaves=["type","id","currency_salary","salary_from","salary_to"]
            valores_a_imprimir1 = []
            conteo=1
            for offer in lt.iterator(firstEmploTypes):
                lst_provisional = [conteo]
                for llave in llaves:
                    lst_provisional.append(offer[llave])
                valores_a_imprimir1.append(lst_provisional)
                conteo += 1
            print(tabulate(valores_a_imprimir1, headers=llaves))
            print("\nLast three element\n")
            valores_a_imprimir1 = []
            conteo=EmploTypesSize-2
            for offer in lt.iterator(lastEmploTypes):
                lst_provisional = [conteo]
                for llave in llaves:
                    lst_provisional.append(offer[llave])
                valores_a_imprimir1.append(lst_provisional)
                conteo += 1
            print(tabulate(valores_a_imprimir1, headers=llaves))
            
            
            print("_"*150)
            print("\nJOBS\n")
            
            #headersJobs = list(lt.getElement(data["jobs"],1).keys())
           
            
            JobsSize = controller.data_size(data, "jobs")
            print("Size")
            print(JobsSize)
            firstJobs,lastJobs = controller.three_first_last(data, "jobs")
            print("\nFirst three elements\n")
            #print(firstJobs)
            llaves=["published_at","title", "company_name", "experience_level", "country_code", "city"]
            valores_a_imprimir1 = []
            conteo=1
            for offer in lt.iterator(firstJobs):
                lst_provisional = [conteo]
                for llave in llaves:
                    lst_provisional.append(offer[llave])
                valores_a_imprimir1.append(lst_provisional)
                conteo += 1
            print(tabulate(valores_a_imprimir1, headers=llaves))
            
            print("\nLast three elements\n")
            valores_a_imprimir1 = []
            conteo=JobsSize-2
            for offer in lt.iterator(lastJobs):
                lst_provisional = [conteo]
                for llave in llaves:
                    lst_provisional.append(offer[llave])
                valores_a_imprimir1.append(lst_provisional)
                conteo += 1
            print(tabulate(valores_a_imprimir1, headers=llaves))
            
            print("_"*150)
            #table = tabulate( headers, tabular_data=firstJobs["elements"], tablefmt="grid")
            #print(table)
            
            
            print("\nMULTILOCATIONS\n")
            
            
            MulitlocationsSize = controller.data_size(data, "multilocations")
            print("Size")
            print(MulitlocationsSize)
            firstMultilocations,lastMultilocations = controller.three_first_last(data, "multilocations")
            print("\nFirst three elements\n")
            
            llaves=["city", "street", "id"]
            valores_a_imprimir1 = []
            conteo=1
            for offer in lt.iterator(firstMultilocations):
                lst_provisional = [conteo]
                for llave in llaves:
                    lst_provisional.append(offer[llave])
                valores_a_imprimir1.append(lst_provisional)
                conteo += 1
            print(tabulate(valores_a_imprimir1, headers=llaves))
            
            print("\nLast three elements\n")
            valores_a_imprimir1 = []
            conteo=MulitlocationsSize-2
            for offer in lt.iterator(lastMultilocations):
                lst_provisional = [conteo]
                for llave in llaves:
                    lst_provisional.append(offer[llave])
                valores_a_imprimir1.append(lst_provisional)
                conteo += 1
            print(tabulate(valores_a_imprimir1, headers=llaves))
                
            print("_"*150)
                
            print("\nSKILLS\n")
            
            
            SkillsSize = controller.data_size(data, "skills")
            print("SIZE")
            print(SkillsSize)
            firstSkills,lastSkills = controller.three_first_last(data, "skills")
            print("\nFirst three elements\n")
            llaves=["name", "level", "id"]
            valores_a_imprimir1 = []
            conteo=1
            for offer in lt.iterator(firstSkills):
                lst_provisional = [conteo]
                for llave in llaves:
                    lst_provisional.append(offer[llave])
                valores_a_imprimir1.append(lst_provisional)
                conteo += 1
            print(tabulate(valores_a_imprimir1, headers=llaves))
            print("\nLast three elements\n")
            valores_a_imprimir1 = []
            conteo=SkillsSize-2
            for offer in lt.iterator(lastSkills):
                lst_provisional = [conteo]
                for llave in llaves:
                    lst_provisional.append(offer[llave])
                valores_a_imprimir1.append(lst_provisional)
                conteo += 1
            print(tabulate(valores_a_imprimir1, headers=llaves))
            print("_"*150)
            

            
        elif int(inputs) == 2:
            print_req_1(control)

        elif int(inputs) == 3:
            
            offer_number = input("Por favor digite el numero de ofertas a imprimir: ")
            company_name = input( "Por favor digite el nombre de la compañia: ")
            city = input("Por favor digite el nombre de la ciudad: ")
            function = print_req_2(control, offer_number, company_name, city)
            
            
            print("Total de ofertas ofrecida por la empresa y ciudad:", function[0] )
            
            if function[0]!=0:
                for i in function[1]["elements"]:
                    print()
                    fecha = i["published_at"]
                    fecha0= datetime.strptime(fecha, "%Y-%m-%dT%H:%M:%S.%fZ")
                    fecha1 = fecha0.strftime("%d %B, %Y")
                    print("Fecha de publicacion:", fecha1)
                    print("Pais de la oferta: ", i["country_code"])
                    print("Ciudad de la oferta: ", i["city"])
                    print("Nombre de la empresa de la oferta: ", i["company_name"])
                    print("Titulo de la oferta: ", i["title"])
                    print("Nivel de experticia de la oferta: ", i["experience_level"])
                    if i["remote_interview"]== False:
                        print("Formato de aplicación de la oferta: presencial")
                    else:
                        print("Formato de aplicación de la oferta: remota")
                    print("Tipo de trabajo: ", i["workplace_type"])
                    print()
            else:
                print("No se encontraron",offer_number,"ofertas")
            print(f"Ha demorado {function[2]} [ms]")
            print()

        elif int(inputs) == 4:
            print_req_3(control)

        elif int(inputs) == 5:
            print_req_4(control)

        elif int(inputs) == 6:
            limite_inicial = input("Por favor digite la fecha inicial del periodo a consultar: ")
            limite_final = input("Por favor digite la fecha final del periodo a consultar: ")
            city = input("Por favor digite el nombre de la ciudad: ")
            function = print_req_5(control, city, limite_inicial, limite_final)
            print()
            print("Total de ofertas publicadas en la ciudad en el periodo de consulta: ", function[0] )
            print("Total de empresas que publicaron por lo menos una oferta en la ciudad de consulta: ", function[2])
            if function[0] == 0:
                print("Empresa con mayor número de ofertas: Ninguna","......Numero de ofertas: Ninguna" )
                print("Empresa con menor número de ofertas: Ninguna",".......Numero de ofertas: Ninguna"  )
                print()
                print("................................")
                print()
                print("No encontramos ofertas en esta ciudad en estas fechas, porfavor intenta de nuevo ")
                print()
                print("................................")
                print()
                
                
            else:
                print("Empresa con mayor número de ofertas: ", function[5],"......Numero de ofertas: ", function[3] )
                print("Empresa con menor número de ofertas: ",function[6],".......Numero de ofertas: ", function[4]  )
        
            for i in function[1]["elements"]:
                print()
                fecha = i["published_at"]
                fecha0= datetime.strptime(fecha, "%Y-%m-%dT%H:%M:%S.%fZ")
                fecha1 = fecha0.strftime("%d %B, %Y")
                print("Fecha de publicacion:", fecha1)
                print("Titulo de la oferta: ", i["title"])
                print("Nombre de la empresa de la oferta: ", i["company_name"])
                print("Tipo de lugar de trabajo de la oferta: ", i["workplace_type"])
                print("Tamaño de la empresa de la oferta: ",  i["company_size"])
            print(f"Ha demorado {function[7]} [ms]")
            print()

        elif int(inputs) == 7:
            print_req_6(control)

        elif int(inputs) == 8:
            limite_inicial = input("Por favor digite la fecha inicial del periodo a consultar (Y-M-D): ")
            limite_final = input("Por favor digite la fecha final del periodo a consultar (Y-M-D): ")
            country_number = input("Por favor digite el numero de paises que desea consultar:  ")
            function = print_req_7(control, country_number, limite_inicial, limite_final)
            print()
            print("Total de ofertas de empleo: ", function[0] )
            print("Total de ciudades donde se ofertó en los países resultantes de la consulta: ", function[2])
            print("País con mayor cantidad de ofertas: ", function[4], ".......Numero de ofertas: ", function[3]  )
            print("Ciudad con mayor cantidad de ofertas: ", function[6], ".......Numero de ofertas: ", function[5]  )
            
            
            for i in function[1][2].items():
                
                print()
                print("................................")
                print()
                print("Nivel de epxerticia: ", i[0])
                print()
                print("................................")
                print()
                llave = i[0]
                print("Numero de habilidades: ", len(function[1][2][llave]))
                
                
                if llave in function[7]:
                    
                    
                    may = max(function[7][llave].values())
                    for i in function[7][llave.lower()].items():
                        if i[1]==may:
                            may0 = i[0]

                    print("Habilidad más solicitada: ",may0,".......Numero de ofertas: ", may )
                    
                
            
                if llave in function[8]:
                    
                    men = min(function[8][llave].values())
                    for i in function[8][llave.lower()].items():
                        if i[1]==men:
                            men0 = i[0]

                    print("Habilidad menos solicitada: ",men0,".......Numero de ofertas: ", men )
                
          
    
                
    
                
                mayores = max(function[9][llave].values())
                menores = min(function[9][llave].values())
                cont = 0
                for i in function[9][llave].items():
                    if i[1]==mayores:
                        mayores0 = i[0]
                    if i[1]==menores:
                        menores0 = i[0]
                        
                    cont +=1
                    
                    print("Conteo de empresas que publicaron una oferta: ", cont)
                    print("Empresa con mayor número de ofertas: ", mayores0,"......Numero de ofertas: ", mayores)
                    print("Empresa con menor número de ofertas: ", menores0,".......Numero de ofertas: ", menores )
                    print()
                    print("................................")
                    print()
            print(f"Ha demorado {function[10]} [ms]")
            print()
                
            
            
            
            
            
            
            
            
            
            

        elif int(inputs) == 9:
            print_req_8(control)

        elif int(inputs) == 10:
            print("\n a continuación se despliegan las posibles estructuras de datos con que puede cargar el catalogo...\n")
            print("(1) Array list")
            print("(2) Single linked")
            selection = int(input("Por favor digite el número de la opción que desea escoger... "))
            while selection != 1 and selection != 2:
                print("No existe esa opción, intente de nuevo")
                selection = int(input("Por favor digite el número de la opción que desea escoger... "))
                
            
            controller.changeGlobalTAD(selection)
            control = new_controller()
        
        elif int(inputs) ==  11:
            print("\nA CONTINUACIÓN SE DESPLIEGA UN MENÚ QUE CONTIENE LOS ALGORTIMOS DE ORDENAMIENTO QUE PUEDE ESCOGER PARA ORDENAR LA LISTA DE OFERTAS DE TRABAJO\n")
            print("(1) shellsort")
            print("(2) insertionsort")
            print("(3) selectionsort")
            print("(4) mergesort")
            print("(5) quicksort")
            print("(6) Timsort")
            selection = int(input("Por favor digite el número de la opción que desea escoger... "))
            while selection != 1 and selection != 2 and selection != 3 and selection != 4 and selection != 5 and selection!=6:
                print("No existe esa opción, intente de nuevo")
                selection = int(input("Por favor digite el número de la opción que desea escoger... "))
            controller.changeGlobalSort(selection)
        
        elif int(inputs) == 12:
            print("\nPOR FAVOR DIGITE A CONTINUACIÓN EL SUFIJO DEL ARCHIVO PARA EL QUE DESEA MANIPULAR LA MUESTRA\n")
            sufijo = input("sufijo : ")
            
            if sufijo in ["10-por", "20-por", "30-por","40-por","50-por", "60-por", "70-por", "80-por","90-por","small","medium", "large"]:
                controller.cambiarTamañoMuestra(sufijo)
            else:
                print("\n no existen archivos con ese sufijo, intente nuevamente\n")
            
        elif int(inputs) == 0:
            working = False
            print("\nGracias por utilizar el programa") 
        else:
            print("Opción errónea, vuelva a elegir.\n")
    sys.exit(0)

# Se crea el controlador asociado a la vista
control = new_controller()

# main del reto
if __name__ == "__main__":
    """
    Menu principal
    """
    threading.stack_size(67108864*2) # 128MB stack
    default_limit = 10000000
    sys.setrecursionlimit(default_limit*10)
    thread = threading.Thread(target=menu_cycle)
    thread.start()
    
 
 