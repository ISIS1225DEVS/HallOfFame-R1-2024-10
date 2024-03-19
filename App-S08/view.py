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
import sys
from tabulate import tabulate
import threading
"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""
#Entrega Laboratorio 5
default_limit = 1000

def new_controller(seleccion:str):
    """
        Se crea una instancia del controlador
    returns:
    control: instancia del controlador con el modelo cargado en memoria
    """
    control= controller.new_controller(seleccion)
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
    print("10- Ejecutar pruebas de ordenamiento")
    print("0- Salir")
def tamanio_archivo():
    """
    Función que le pide al usuario que seleccione el tamaño del archivo que desea cargar

    Returns:
    retorno: string con el tamaño del archivo que se va a cargar
    """
    #Se le muestra al usuario las opciones de tamaño de archivo que puede cargar
    print("Seleccione el tamaño del archivo a cargar")
    opciones={"1": "10",
              "2": "20",
              "3": "30",
              "4": "40",
              "5": "50",
              "6": "60",
              "7": "70",
              "8": "80",
              "9": "90",
              "10": "small",
              "11": "medium",
              "12": "large"}
    #Se iteran las opciones y se imprimen
    for opcion in opciones:
        print(opcion + "- " + opciones[opcion])
    #Se le pide al usuario que seleccione una opción
    inputs = input('Seleccione una opción para continuar\n')
    #Se valida que la opción seleccionada sea válida y exista en el diccionario de opciones
    if inputs in opciones:
        retorno= opciones[inputs]
    else:
        print("Opción errónea, vuelva a elegir.\n")
        retorno= tamanio_archivo()
    return retorno
def load_data(control):
    """
    Carga los datos
    Args:
    control: instancia del controlador con el modelo cargado en memoria
    Returns:
    datos: diccionario con la información de los archivos cargados
    """
    #Se inicia una variable donde la elección del tamaño del archivo es False
    eleccion=False
    tamanio=None
    #Se itera hasta que el usuario seleccione un tamaño de archivo
    while eleccion==False:
        tamanio=tamanio_archivo()
        if tamanio_archivo!=None:
            eleccion=True
    #Se le muestra al usuario el tamaño de archivo que seleccionó
    print("-"*20)
    print("El tamaño elegido es "+ tamanio)
    print("-"*20)
    print("Cargando información de los archivos ....\n")
    #Se llama la función load_data del controlador
    datos=controller.load_data(control, tamanio)
    return datos


def print_req_1(control):
    """
        Función que imprime la solución del Requerimiento 1 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 1
    #Se le pide al usuario que ingrese el numero de ofertas que desea ver, el codigo del pais y el nivel de experticia
    num_ofertas=int(input("Ingrese el numero de ofertas que desea ver: "))
    cod_pais=input("Ingrese el codigo del pais que desea ver: ")
    lvl_exp=input("Ingrese el nivel de experticia que desea ver: ")
    #Se hace un print de cargando para que el usuario sepa que el programa esta trabajando
    print("-"*20+"Cargando..."+"-"*20)
    #Se llama la función req_1 del controlador
    retorno=controller.req_1(control, cod_pais, lvl_exp)
    datos=retorno[0]
    #Se crea una tabla con los datos que se van a imprimir
    header=["#","Fecha publicación", "Titulo oferta", "Nombre empresa", "Nivel experticia", "Pais oferta", "Ciudad oferta","Tamaño empresa","Tipo ubicación","Contrata ucranianos"]
    tabla=[]
    tamanio=lt.size(datos)
    #Se imprime el numero de ofertas que se encontraron
    print("Se encontraron "+str(tamanio)+" ofertas"+" en "+cod_pais+" con nivel de experticia "+lvl_exp)
    #Se valida que el numero de ofertas que se quieren imprimir no sea mayor al numero de ofertas que se encontraron
    if tamanio<num_ofertas:
        num_ofertas=tamanio
    #Se itera sobre el numero de ofertas que se quieren imprimir y se agregan a la tabla
    for i in range(1,num_ofertas+1):
        tabla.append([i,lt.getElement(datos,i)["published_at"],
                      lt.getElement(datos,i)["title"],
                      lt.getElement(datos,i)["company_name"],
                      lt.getElement(datos,i)["experience_level"],
                      lt.getElement(datos,i)["country_code"], 
                      lt.getElement(datos,i)["city"],
                      lt.getElement(datos,i)["company_size"],
                      lt.getElement(datos,i)["workplace_type"],
                      lt.getElement(datos,i)["open_to_hire_ukrainians"]])
    #Se imprime la tabla
    print(tabulate(tabla, headers=header, tablefmt="grid"))
    print("El tiempo total es de "+ str(round(retorno[1],2))+" ms")


def print_req_2(control):
    """
        Función que imprime la solución del Requerimiento 2 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 2
    #Se le pide al usuario que ingrese el numero de ofertas que desea ver, el nombre de la empresa y la ciudad
    num_ofertas=int(input("Ingrese el numero de ofertas a listar: "))
    nombre_empresa=input("Ingrese el nombre COMPLETO de la empresa a consultar: ")
    ciudad=input("Ingrese la ciudad a buscar en las ofertas: ")
    
    #Se hace un print de cargando para que el usuario sepa que el programa esta trabajando
    print("-"*20+"Cargando..."+"-"*20)
    
    #Se llama la función req_2 del controlador
    datos=controller.req_2(control, num_ofertas,nombre_empresa,ciudad)
    resultado=datos[0]
    
    #Se crea una tabla con los datos que se van a imprimir
    header=["#","Fecha publicación", "Pais oferta", "Ciudad oferta","Nombre empresa","Titulo oferta", "Nivel experticia","Formato aplicación", "Tipo trabajo"]
    tabla=[]
    tamanio=lt.size(resultado)
    #Se imprime el numero de ofertas que se encontraron
    print("Se encontraron "+str(tamanio)+" ofertas en "+nombre_empresa+" y en la ciudad "+ciudad)
    #Se valida que el numero de ofertas que se quieren imprimir no sea mayor al numero de ofertas que se encontraron
    if tamanio<num_ofertas:
        num_ofertas=tamanio
    #Se itera sobre el numero de ofertas que se quieren imprimir y se agregan a la tabla
    for i in range(1,num_ofertas+1):
        tabla.append([i,lt.getElement(resultado,i)["published_at"], lt.getElement(resultado,i)["country_code"], lt.getElement(resultado,i)["city"], lt.getElement(resultado,i)["company_name"], lt.getElement(resultado,i)["title"], lt.getElement(resultado,i)["experience_level"], lt.getElement(resultado,i)["remote_interview"], lt.getElement(resultado,i)["workplace_type"]])
    #Se imprime la tabla
    print(tabulate(tabla, headers=header, tablefmt="grid"))
    print("El tiempo total es de "+ str(round(datos[1],2))+" ms")
    
def print_req_3(control):
    """
        Función que imprime la solución del Requerimiento 3 en consola
    """
    #Se le pide al usuario que ingrese el nombre de la empresa y el intervalo de las fechas
    nombre_emp=input("Ingrese el nombre de la empresa a consultar: ")
    fecha_1=input("Ingrese la fehca inicial del periodo a consultar: ")
    fecha_2=input("Ingrese la fecha final del periodo a consultar: ")
    
    #Se llama la función req_3 del controlador
    datos=controller.req_3(control,nombre_emp,fecha_1, fecha_2)
     
    #Se imprime el numero de ofertas que se encontraron
    print("Se encontraron "+str(datos["total_ofertas"])+" ofertas en "+nombre_emp)
    # Se imprime el numero de ofertas que se encontraron en cada nivel de experiencia
    print("Se encontraron "+str(datos["ofertas_junior"])+" ofertas para el nivel de experiencia junior")
    print("Se encontraron "+str(datos["ofertas_mid"])+" ofertas para el nivel de experiencia mid")
    print("Se encontraron "+str(datos["ofertas_senior"])+" ofertas para el nivel de experiencia senior")
    
    #Se crea una lista que contenga el listado de empresas ordenados cronologicamente por fecha y pais
    lista_emp =[]
    for i in range(1,datos["total_ofertas"]+1):
       lista_emp.append([lt.getElement(datos["listado_ofertas"],i)["published_at"],
                         lt.getElement(datos["listado_ofertas"],i)["title"],
                         lt.getElement(datos["listado_ofertas"],i)["experience_level"],
                         lt.getElement(datos["listado_ofertas"],i)["city"],
                         lt.getElement(datos["listado_ofertas"],i)["country_code"],
                         lt.getElement(datos["listado_ofertas"],i)["company_size"], 
                         lt.getElement(datos["listado_ofertas"],i)["workplace_type"], 
                         lt.getElement(datos["listado_ofertas"],i)["open_to_hire_ukrainians"]])

    #Se imprime el listado de empresas ordenados cronologicamente por fecha y pais
    print(tabulate(lista_emp, headers=["Fecha publicación","Titulo", "Nivel de experticia", "Ciudad", "Pais", "Tamaño empresa", "Tipo de lugar", "Contrata ucranianos"], tablefmt="grid"))

def print_req_4(control):
    """
        Función que imprime la solución del Requerimiento 4 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 4
        
    # El usuario ingresa el codigo del país y las fechas que desea consultar 
    codigo=str(input("Ingrese el codigo del país que desea consultar: "))
    fecha_inicial=str(input("Ingrese desde que fecha desea consultar:(año-mes-día)"))
    fecha_final=str(input("Ingrese hasta que fecha desea consultar:(año-mes-día) "))
     
     #Se hace un print de cargando para que el usuario sepa que el programa esta trabajando
    print("-"*20+"Cargando..."+"-"*20)
    
    #Se llama la función req_4 del controlador
    retorno=controller.req_4(control,codigo,fecha_inicial,fecha_final)
    resultado,empresa,totalc,mayor,menor= retorno[0]
    tamanio= lt.size(resultado)
    #Se imprime el numero de ofertas que se encontraron
    print("Se encontraron "+str(tamanio)+" oferta(s) en "+codigo +" entre "+fecha_inicial+" y "+ fecha_final)
    #Se imprime el numero de empresas  que publicaron al menos una oferta en el país de consulta
    print("Se encontraron "+str(empresa)+" empresa(s) que publicaron al menos una oferta en "+codigo +" entre "+fecha_inicial+" y "+ fecha_final)  
    #Se imprime el numero de ciudades del país de consulta en las que se publicaron ofertas
    print("Se encontraron "+ str(totalc)+" ciudad(es)  en "+codigo +" que tuvieron al menos una oferta entre "+fecha_inicial+" y "+ fecha_final)
    #Se imprime Ciudad del país de consulta con mayor número de ofertas y su conteo
    print("La ciudad con mayor numero de ofertas es "+ str(mayor["city"])+" con "+str(mayor["cantidad"]))
    print("La ciudad con menor numero de ofertas es "+ str(menor["city"])+ " con "+str(menor["cantidad"]))
    #Se crea una tabla
    header=["#","Fecha publicación", "Título de la oferta.", "Nivel de experticia requerido","Nombre empresa","Ciudad de la empresa", "Tipo de lugar de trabajo", "Tipo trabajo","Disponible a contratar ucranianos"]
    tabla=[]
    for i in range(1,tamanio+1):
        tabla.append([i,lt.getElement(resultado,i)["published_at"], lt.getElement(resultado,i)["title"], lt.getElement(resultado,i)["experience_level"], lt.getElement(resultado,i)["company_name"], lt.getElement(resultado,i)["city"], lt.getElement(resultado,i)["workplace_type"], lt.getElement(resultado,i)["remote_interview"], lt.getElement(resultado,i)["open_to_hire_ukrainians"]])
    #Se imprime la tabla
    print(tabulate(tabla, headers=header, tablefmt="grid"))
    print("El tiempo total es de "+ str(round(retorno[1],2))+" ms")


def print_req_5(control):
    """
        Función que imprime la solución del Requerimiento 5 en consola
    """
    ciudad=input("Ingrese la ciudad que desea consultar: ")
    fecha_1=input("Ingrese la fecha de inicio en formato YYYY-MM-DD: ")
    fecha_2=input("Ingrese la fecha de fin en formato YYYY-MM-DD: ")
    print("-"*20+"Cargando..."+"-"*20)
    datos=controller.req_5(control, ciudad, fecha_1, fecha_2)
    retorno=datos[0]
    
    print("El total de ofertas publicadas en "+str(ciudad)+" entre las fechas "+str(fecha_1)+" y "+str(fecha_2)+" es de "+str(lt.size(retorno[0]))+" ofertas")
    print("El total de empresas que publicaron ofertas en la ciudad "+str(ciudad)+" entre las fechas "+str(fecha_1)+" y "+str(fecha_2)+" son: "+str(lt.size(retorno[1]))+" empresas")
    print("La empresa con más ofertas publicadas en "+str(ciudad)+" entre las fechas "+str(fecha_1)+" y "+str(fecha_2)+" es: "+str(lt.getElement(retorno[1],1)["company_name"])+ " con "+str(lt.getElement(retorno[1],1)["cantidad"])+" ofertas")
    print("La empresa con menos ofertas publicadas en "+str(ciudad)+" entre las fechas "+str(fecha_1)+" y "+str(fecha_2)+" es: "+str(lt.getElement(retorno[1],lt.size(retorno[1]))["company_name"])+ " con "+str(lt.getElement(retorno[1],lt.size(retorno[1]))["cantidad"])+" ofertas y un salario de "+str(lt.getElement(retorno[1],lt.size(retorno[1]))["average"])+" dolares")
    print("Los datos ordenados son:")
    header=["#","Fecha de publicacion","Titulo oferta", "Nombre empresa", "Tipo lugar", "tamaño empresa"]
    tabla=[]
    for i in range(1,4):
        tabla.append([i,lt.getElement(retorno[0],i)["published_at"], lt.getElement(retorno[0],i)["title"], lt.getElement(retorno[0],i)["company_name"], lt.getElement(retorno[0],i)["workplace_type"], lt.getElement(retorno[0],i)["company_size"]])
    print(tabulate(tabla, headers=header, tablefmt="grid"))
    tabla=[]
    for i in range(lt.size(retorno[0])-2, lt.size(retorno[0])+1):
        print(".")
        tabla.append([i,lt.getElement(retorno[0],i)["published_at"], lt.getElement(retorno[0],i)["title"], lt.getElement(retorno[0],i)["company_name"], lt.getElement(retorno[0],i)["workplace_type"], lt.getElement(retorno[0],i)["company_size"]])
    print(tabulate(tabla, headers=header, tablefmt="grid"))
    print("El tiempo total es de "+ str(round(datos[1],2))+" ms")

def print_req_6(control):
    """
        Función que imprime la solución del Requerimiento 6 en consola
    """
    #Le pide los datos al usuario
    num_ciudades=int(input("Ingrese el numero de ciudades que desea ver: "))
    nivel_exp=input("Ingrese el nivel de experticia que desea ver (junior, mid, senior): ")
    fecha_ini=input("Ingrese la fecha de inicio en formato YYYY-MM-DD: ")
    fecha_fin=input("Ingrese la fecha de fin en formato YYYY-MM-DD: ")
    codigo_pais=input("Desea ver los datos de un pais en especifico (S/N): ")
    #Si el usuario desea ver los datos de un pais en especifico se le pide que ingrese el codigo del pais
    if codigo_pais.lower()=="s":
        codigo_pais=input("Ingrese el codigo del pais que desea ver: ")
    #Sino, se le asigna None a la variable
    else:
        codigo_pais=None
    #Se imprime cargando para que el usuario sepa que el programa esta trabajando
    print("-"*20+"Cargando..."+"-"*20)
    datos=controller.req_6(control, num_ciudades, nivel_exp, fecha_ini, fecha_fin, codigo_pais)
    retorno=datos[0]
    #Se imprime el total de ofertas publicadas
    print("El total de ciudades es: "+str(retorno["total_ciudades"]))
    print("El total de empresas es: "+str(retorno["total_empresas"]))
    print("El total de ofertas publicadas entre las fechas "+str(fecha_ini)+" y "+str(fecha_fin)+" es de "+str(retorno["total_ofertas"])+" ofertas")
    print("El promedio de salario para el nivel "+nivel_exp+" entre las fechas "+str(fecha_ini)+" y "+str(fecha_fin)+" es de: "+str(retorno["promedio_salario"])+" dolares")
    print("La ciudad con más ofertas publicadas entre las fechas "+str(fecha_ini)+" y "+str(fecha_fin)+" es: "+str(retorno["ciudad_mas_ofertas"][0])+" con "+str(retorno["ciudad_mas_ofertas"][1])+" ofertas")
    print("La ciudad con menos ofertas publicadas entre las fechas "+str(fecha_ini)+" y "+str(fecha_fin)+" es: "+str(retorno["ciudad_menos_ofertas"][0])+" con "+str(retorno["ciudad_menos_ofertas"][1])+" ofertas")
    for i in range(1,num_ciudades+1):
        print("======="+lt.getElement(retorno["lista_ciudades"],i)["ciudad"]+"=======")
        print("El total de ofertas publicadas en "+str(lt.getElement(retorno["lista_ciudades"],i)["ciudad"])+" entre las fechas "+str(fecha_ini)+" y "+str(fecha_fin)+" es de "+str(lt.getElement(retorno["lista_ciudades"],i)["cantidad"])+" ofertas")
        print("El salario promedio en "+str(lt.getElement(retorno["lista_ciudades"],i)["ciudad"])+" entre las fechas "+str(fecha_ini)+" y "+str(fecha_fin)+" es de: "+str(lt.getElement(retorno["lista_ciudades"],i)["salario_promedio"])+" dolares")
        print("El total de empresas en "+str(lt.getElement(retorno["lista_ciudades"],i)["ciudad"])+" entre las fechas "+str(fecha_ini)+" y "+str(fecha_fin)+" es de: "+str(lt.getElement(retorno["lista_ciudades"],i)["empresas"])+" empresas")
        print("La empresa con más ofertas publicadas en "+str(lt.getElement(retorno["lista_ciudades"],i)["ciudad"])+" entre las fechas "+str(fecha_ini)+" y "+str(fecha_fin)+" es:"+str(lt.getElement(retorno["lista_ciudades"],i)["empresa_alta"]["company_name"])+" con un salario de "+str(lt.getElement(retorno["lista_ciudades"],i)["salario_alto"]))
        print("La empresa con menos ofertas publicadas en "+str(lt.getElement(retorno["lista_ciudades"],i)["ciudad"])+" entre las fechas "+str(fecha_ini)+" y "+str(fecha_fin)+" es:"+str(lt.getElement(retorno["lista_ciudades"],i)["empresa_baja"]["company_name"])+" con un salario de "+str(lt.getElement(retorno["lista_ciudades"],i)["salario_bajo"]))
    print("\n""El tiempo total es de "+ str(round(datos[1],2))+" ms")


def print_req_7(control):
    """
        Función que imprime la solución del Requerimiento 7 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 7
    num_paises=int(input("Ingrese el numero de paises que desea ver: "))
    fecha_ini=input("Ingrese la fecha de inicio en formato YYYY-MM-DD: ")
    fecha_fin=input("Ingrese la fecha de fin en formato YYYY-MM-DD: ")
    datos=controller.req_7(control, num_paises, fecha_ini, fecha_fin)
    retorno=datos[0]
    tupla=("junior","mid","senior")
    otros=retorno["otros"]
    
    print("\n"+"="*20+"Cargando..."+"="*20+"\n")
    
    print("El total de ofertas publicadas entre las fechas "+str(fecha_ini)+" y "+str(fecha_fin)+" es de "+str(otros["total_ofertas"])+" ofertas")
    print("El total de ciudades que publicaron ofertas entre las fechas "+str(fecha_ini)+" y "+str(fecha_fin)+" son: "+str(otros["num_ciudades"])+" ciudades")
    print("El pais con más ofertas publicadas entre las fechas "+str(fecha_ini)+" y "+str(fecha_fin)+" es: "+str(otros["pais_mas_ofertas"][0])+" con "+str(otros["pais_mas_ofertas"][1])+" ofertas")
    print("La ciudad con más ofertas publicadas entre las fechas "+str(fecha_ini)+" y "+str(fecha_fin)+" es: "+str(otros["ciudad_mas_ofertas"][0])+" con "+str(otros["ciudad_mas_ofertas"][1])+" ofertas")
    print("\n"+"="*20+"Ofertas por nivel de experticia"+"="*20+"\n")
    
    for i in range(3):
        print("="*20+tupla[i]+"="*20)
        print("La cantidad de habilidades requeridas para el nivel "+tupla[i]+" es de: "+str(retorno[tupla[i]]["conteo_habilidades"]))
        print("La habilidad mas solicitada para el nivel "+tupla[i]+" es: "+str(retorno[tupla[i]]["habilidad_mas_solicitada"][0])+" con "+str(retorno[tupla[i]]["habilidad_mas_solicitada"][1])+" solicitudes")
        print("La habilidad menos solicitada para el nivel "+tupla[i]+" es: "+str(retorno[tupla[i]]["habilidad_menos_solicitada"][0])+" con "+str(retorno[tupla[i]]["habilidad_menos_solicitada"][1])+" solicitudes")
        print("El nivel promedio de habilidades requeridas para el nivel "+tupla[i]+" es de: "+str(retorno[tupla[i]]["nivel_promedio"]))
        print("La cantidad de empresas que publicaron ofertas para el nivel "+tupla[i]+" es de: "+str(retorno[tupla[i]]["conteo_empresas"]))
        print("La empresa con más ofertas publicadas para el nivel "+tupla[i]+" es de: "+str(retorno[tupla[i]]["empresa_mas_solicitada"][0])+" con "+str(retorno[tupla[i]]["empresa_mas_solicitada"][1])+" ofertas")
        print("La empresa con menos ofertas publicadas para el nivel "+tupla[i]+" es de: "+str(retorno[tupla[i]]["empresa_menos_solicitada"][0])+" con "+str(retorno[tupla[i]]["empresa_menos_solicitada"][1])+" ofertas")
        print("La cantidad de empresas con una o mas sedes para el nivel "+tupla[i]+" es de: "+str(retorno[tupla[i]]["conteo_empresas_skills"]))
        print("\n")
    print("El tiempo total es de "+ str(round(datos[1],2))+" ms")
   


def print_req_8(control):
    """
        Función que imprime la solución del Requerimiento 8 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 8
    pass
def seleccionar_tipo_estructura():
    print("Seleccione el tipo de estructura que desea usar")
    opciones={"1": "Array",
              "2": "Single-Linked List",
              "3": "Double-Linked List"}
    for opcion in opciones:
        print(opcion + "- " + opciones[opcion])
    inputs = input('Seleccione una opción para continuar\n')
    valido=False
    while valido==False:
        retorno=None
        if inputs in opciones:
            if inputs=="1":
                print("Se ha seleccionado Array")
                retorno="ARRAY_LIST"
            elif inputs=="2":
                print("Se ha seleccionado Single-Linked List")
                retorno="SINGLE_LINKED"
            elif inputs=="3":
                print("Se ha seleccionado Double-Linked List")
                retorno="DOUBLE_LINKED"
            valido=True
        else:
            print("Opción errónea, vuelva a elegir.\n")
            inputs = input('Seleccione una opción para continuar\n')
    return retorno
def tipo_ordenamiento(control):
    opciones={"1": "Selection Sort",
              "2": "Insertion Sort",
              "3": "Shell Sort",
              "4": "Merge Sort",
              "5": "Quick Sort",
              "6": "Tim Sort"}
    for opcion in opciones:
        print(opcion + "- " + opciones[opcion])
    inputs = input('Seleccione una opción para continuar\n')
    valido=False
    while valido==False:
        retorno=None
        if inputs in opciones:
            if inputs=="1":
                print("Se ha seleccionado Selection Sort")
                retorno=controller.ordenamiento_selection(control)
            elif inputs=="2":
                print("Se ha seleccionado Insertion Sort")
                retorno=controller.ordenamiento_insertion(control)
            elif inputs=="3":
                print("Se ha seleccionado Shell Sort")
                retorno=controller.ordenamiento_shell(control)
            elif inputs=="4":
                print("Se ha seleccionado Merge Sort")
                retorno=controller.ordenamiento_merge(control)
            elif inputs=="5":
                print("Se ha seleccionado Quick Sort")
                retorno=controller.ordenamiento_quick(control)
            elif inputs=="6":
                print("Se ha seleccionado Tim Sort")
                retorno=controller.ordenamiento_tim(control)
            valido=True
        else:
            print("Opción errónea, vuelva a elegir.\n")
            inputs = input('Seleccione una opción para continuar\n')
    print("Los datos ordenados son:")
    header=["#","Titulo oferta",
            "Calle", "Ciudad",
            "Codigo_pais", "Direccion",
            "Icono","Tipo de trabajo",
            "Nombre empresa","Sitio web",
            "Tamanio Empresa","Nivel experticia",
            "Fecha publicacion","Entrevista Remota",
            "Contrata ucranianos", "id","Display Offer"]
    if inputs=="6":
        if lt.size(retorno[0])>6:
            tabla=[]
            for i in range(0,3):
                tabla.append([i+1,lt.getElement(retorno[0],i)["title"], lt.getElement(retorno[0],i)["street"], lt.getElement(retorno[0],i)["city"], lt.getElement(retorno[0],i)["country_code"], lt.getElement(retorno[0],i)["address_text"], lt.getElement(retorno[0],i)["marker_icon"], lt.getElement(retorno[0],i)["workplace_type"], lt.getElement(retorno[0],i)["company_name"], lt.getElement(retorno[0],i)["company_url"], lt.getElement(retorno[0],i)["company_size"], lt.getElement(retorno[0],i)["experience_level"], lt.getElement(retorno[0],i)["published_at"], lt.getElement(retorno[0],i)["remote_interview"], lt.getElement(retorno[0],i)["open_to_hire_ukrainians"], lt.getElement(retorno[0],i)["id"], lt.getElement(retorno[0],i)["display_offer"]])
            print(tabulate(tabla, headers=header, tablefmt="grid"))
            tabla=[]
            for i in range(lt.size(retorno[0])-3, lt.size(retorno[0])):
                tabla.append([i+1,lt.getElement(retorno[0],i)["title"], lt.getElement(retorno[0],i)["street"], lt.getElement(retorno[0],i)["city"], lt.getElement(retorno[0],i)["country_code"], lt.getElement(retorno[0],i)["address_text"], lt.getElement(retorno[0],i)["marker_icon"], lt.getElement(retorno[0],i)["workplace_type"], lt.getElement(retorno[0],i)["company_name"], lt.getElement(retorno[0],i)["company_url"], lt.getElement(retorno[0],i)["company_size"], lt.getElement(retorno[0],i)["experience_level"], lt.getElement(retorno[0],i)["published_at"], lt.getElement(retorno[0],i)["remote_interview"], lt.getElement(retorno[0],i)["open_to_hire_ukrainians"], lt.getElement(retorno[0],i)["id"], lt.getElement(retorno[0],i)["display_offer"]])
            print(tabulate(tabla, headers=header, tablefmt="grid"))
        else:
            tabla=[]
            for i in range(0,lt.size(retorno[0])):
                tabla.append([i+1,lt.getElement(retorno[0],i)["title"], lt.getElement(retorno[0],i)["street"], lt.getElement(retorno[0],i)["city"], lt.getElement(retorno[0],i)["country_code"], lt.getElement(retorno[0],i)["address_text"], lt.getElement(retorno[0],i)["marker_icon"], lt.getElement(retorno[0],i)["workplace_type"], lt.getElement(retorno[0],i)["company_name"], lt.getElement(retorno[0],i)["company_url"], lt.getElement(retorno[0],i)["company_size"], lt.getElement(retorno[0],i)["experience_level"], lt.getElement(retorno[0],i)["published_at"], lt.getElement(retorno[0],i)["remote_interview"], lt.getElement(retorno[0],i)["open_to_hire_ukrainians"], lt.getElement(retorno[0],i)["id"], lt.getElement(retorno[0],i)["display_offer"]])
            print(tabulate(tabla, headers=header, tablefmt="grid"))
    else:
        if lt.size(retorno[0])>6:
            tabla=[]
            for i in range(1,4):
                tabla.append([i,lt.getElement(retorno[0],i)["title"], lt.getElement(retorno[0],i)["street"], lt.getElement(retorno[0],i)["city"], lt.getElement(retorno[0],i)["country_code"], lt.getElement(retorno[0],i)["address_text"], lt.getElement(retorno[0],i)["marker_icon"], lt.getElement(retorno[0],i)["workplace_type"], lt.getElement(retorno[0],i)["company_name"], lt.getElement(retorno[0],i)["company_url"], lt.getElement(retorno[0],i)["company_size"], lt.getElement(retorno[0],i)["experience_level"], lt.getElement(retorno[0],i)["published_at"], lt.getElement(retorno[0],i)["remote_interview"], lt.getElement(retorno[0],i)["open_to_hire_ukrainians"], lt.getElement(retorno[0],i)["id"], lt.getElement(retorno[0],i)["display_offer"]])
            print(tabulate(tabla, headers=header, tablefmt="grid"))
            tabla=[]
            for i in range(lt.size(retorno[0])-2, lt.size(retorno[0])+1):
                tabla.append([i,lt.getElement(retorno[0],i)["title"], lt.getElement(retorno[0],i)["street"], lt.getElement(retorno[0],i)["city"], lt.getElement(retorno[0],i)["country_code"], lt.getElement(retorno[0],i)["address_text"], lt.getElement(retorno[0],i)["marker_icon"], lt.getElement(retorno[0],i)["workplace_type"], lt.getElement(retorno[0],i)["company_name"], lt.getElement(retorno[0],i)["company_url"], lt.getElement(retorno[0],i)["company_size"], lt.getElement(retorno[0],i)["experience_level"], lt.getElement(retorno[0],i)["published_at"], lt.getElement(retorno[0],i)["remote_interview"], lt.getElement(retorno[0],i)["open_to_hire_ukrainians"], lt.getElement(retorno[0],i)["id"], lt.getElement(retorno[0],i)["display_offer"]])
            print(tabulate(tabla, headers=header, tablefmt="grid"))
        else:
            tabla=[]
            for i in range(1,lt.size(retorno[0])+1):
                tabla.append([i,lt.getElement(retorno[0],i)["title"], lt.getElement(retorno[0],i)["street"], lt.getElement(retorno[0],i)["city"], lt.getElement(retorno[0],i)["country_code"], lt.getElement(retorno[0],i)["address_text"], lt.getElement(retorno[0],i)["marker_icon"], lt.getElement(retorno[0],i)["workplace_type"], lt.getElement(retorno[0],i)["company_name"], lt.getElement(retorno[0],i)["company_url"], lt.getElement(retorno[0],i)["company_size"], lt.getElement(retorno[0],i)["experience_level"], lt.getElement(retorno[0],i)["published_at"], lt.getElement(retorno[0],i)["remote_interview"], lt.getElement(retorno[0],i)["open_to_hire_ukrainians"], lt.getElement(retorno[0],i)["id"], lt.getElement(retorno[0],i)["display_offer"]])
            print(tabulate(tabla, headers=header, tablefmt="grid"))
    print("El tiempo total es de "+ str(round(retorno[1],2))+" ms")

# Se crea el controlador asociado a la vista

# main del reto
if __name__ == "__main__":
    """
    Menu principal
    """
    #ciclo del menu
    def menu_principal():
        datos_cargados = False
        working = True
        algoritmo_orden_seleccionado = False
        while working:
            print_menu()
            inputs = input('Seleccione una opción para continuar\n')
            if int(inputs) == 1:
                if datos_cargados==False:
                    seleccion=seleccionar_tipo_estructura()
                    control = new_controller(seleccion)
                    data = load_data(control)
                    print("-"*10+"Carga de datos exitosa"+"-"*10)
                    size=lt.size(data["jobs"])
                    print("Se han cargado "+str(size)+" trabajos")
                    header=["#","Fecha publicacion","Titulo oferta", "Nombre empresa", "Nivel experticia", "Pais de oferta", "Ciudad de oferta"]
                    tabla=[]
                    for i in range(3):
                        tabla.append([i+1,lt.getElement(data["jobs"],i)["published_at"], lt.getElement(data["jobs"],i)["title"], lt.getElement(data["jobs"],i)["company_name"], lt.getElement(data["jobs"],i)["experience_level"], lt.getElement(data["jobs"],i)["country_code"], lt.getElement(data["jobs"],i)["city"]])
                    print(tabulate(tabla, headers=header, tablefmt="grid"))
                    tabla=[]
                    for i in range(size-3, size):
                        print(".")
                        tabla.append([i+1,lt.getElement(data["jobs"],i)["published_at"], lt.getElement(data["jobs"],i)["title"], lt.getElement(data["jobs"],i)["company_name"], lt.getElement(data["jobs"],i)["experience_level"], lt.getElement(data["jobs"],i)["country_code"], lt.getElement(data["jobs"],i)["city"]])
                    print(tabulate(tabla, headers=header, tablefmt="grid"))
                    datos_cargados=True
                    print("="*40)
                    sub_datos=input("Desea obtener un fragmento de los datos (S/N): ")
                    print("="*40)
                    if sub_datos.lower()=="s":
                        cantidad=int(input("Ingrese la cantidad de datos que desea hasta "+str(size)+" datos: "))
                        control["model"]["jobs"]=controller.sublista(control["model"]["jobs"],cantidad)
                        print("="*20+"¡El fragmento se ha cargado!"+"="*20)
                else:
                    print("Los datos ya han sido cargados")
            elif int(inputs) == 2:  
                print_req_1(control)
                
            elif int(inputs) == 3:
                print_req_2(control)

            elif int(inputs) == 4:
                print_req_3(control)

            elif int(inputs) == 5:
                print_req_4(control)

            elif int(inputs) == 6:
                print_req_5(control)

            elif int(inputs) == 7:
                print_req_6(control)

            elif int(inputs) == 8:
                print_req_7(control)

            elif int(inputs) == 9:
                print_req_8(control)
            elif int(inputs) == 10:
                print("Ingrese el algoritmo de ordenamiento que desea utilizar")
                seleccion=tipo_ordenamiento(control)
            elif int(inputs)==0:
                working=False
                print("\nGracias por utilizar el programa") 
            else:
                print("Opción errónea, vuelva a elegir.\n")
        sys.exit(0)
    threading.stack_size(67108864*2)
    sys.setrecursionlimit(default_limit*10)
    thread=threading.Thread(target=menu_principal)
    menu_principal()