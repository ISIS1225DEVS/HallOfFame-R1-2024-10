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

import csv
import config as cf
import sys
import controller
from DISClib.ADT import list as lt
from DISClib.ADT import stack as st
from DISClib.ADT import queue as qu
assert cf
from tabulate import tabulate
import traceback
import threading

csv.field_size_limit(2147483647)

"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""


def new_controller(decision):
    """
        Se crea una instancia del controlador
    """
    #TODO: Llamar la función del controlador donde se crean las estructuras de datos
    control = controller.new_controller(decision)
    return control



def print_menu():
    print("Bienvenido")
    print("1- Cargar información (decidir en que estructura de Datos guardar)")
    print("2- Ejecutar Requerimiento 1")
    print("3- Ejecutar Requerimiento 2")
    print("4- Ejecutar Requerimiento 3")
    print("5- Ejecutar Requerimiento 4")
    print("6- Ejecutar Requerimiento 5")
    print("7- Ejecutar Requerimiento 6")
    print("8- Ejecutar Requerimiento 7")
    print("9- Ejecutar Requerimiento 8")
    print("10- Decidir método ordenamiento de los datos ")
    print("0- Salir")


def load_data(control, tupla_nombre):
    """
    Carga los datos
    """
    jobs_size, jobs_lst, employments_types, multilocations, skills, tiempo = controller.load_data(control, tupla_nombre)
    return jobs_size, jobs_lst, employments_types, multilocations, skills, tiempo


def print_data(control, id):
    """
        Función que imprime un dato dado su ID
    """
    #TODO: Realizar la función para imprimir un elemento
    pass

def print_req_1(control):
    """
        Función que imprime la solución del Requerimiento 1 en consola
        El total de ofertas de trabajo ofrecidas según la condición (junior, mid, o senior).
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
    # TODO: Imprimir el resultado del requerimiento 1
    print("Listar las últimas N ofertas de trabajo según su país y nivel de experticia")
    n_ofertas = int(input("¿Cuántas ofertas desea consultar: "))
    codigo_pais = str(input("Digite el código del país: "))
    experiencia = str(input("Digite el nivel de experiencia (senior/mid/junior): ")).lower()
    lista, tiempo_total = controller.req_1(control,n_ofertas,codigo_pais,experiencia)
    resultado = []
    contador = 0
    headers = ["Fecha", "Título", "Empresa", "Experiencia", "País", "Ciudad", "Tamaño", "Ubicación de trabajo", "Contratar Ucranianos"]
    for job in lt.iterator(lista):
        fila = [
            job["published_at"],
            job["title"],
            job["company_name"],
            job["experience_level"],
            job["country_code"],
            job["city"],
            job["company_size"],
            job["workplace_type"],
            job["open_to_hire_ukrainians"]
        ]
        resultado.append(fila)
        contador += 1
        #print(resultado)
        #print(tabulate([resultado], headers=["Fecha", "Título", "Empresa", "Experiencia", "País", "Ciudad","Tamaño","Ubicación de trabajo","Contratar Ucranianos"], tablefmt="pretty"))
    print("")
    print(tabulate(resultado, headers=headers, tablefmt="pretty"))
    print("")
    print("Número total de ofertas de trabajo ofrecidas según la condición: " + str(contador))
    print("Tiempo de carga: " + str(tiempo_total))


def print_req_2(control):
    """
        Función que imprime la solución del Requerimiento 2 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 2
    pass


def print_req_3(control):
    """
        Función que imprime la solución del Requerimiento 3 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 3
    empresa = str(input("Digite el nombre de la empresa: "))
    fecha_inicial = input("Digite la fecha inicial del periodo a consultar: ")
    fecha_final = input("Digite la fecha final del periodo a consultar: ")
    
    total_ofertas, n_ofertas_experticia, ofertas_en_rango_ordenadas, tiempo_total = controller.req_3(control, empresa, fecha_inicial, fecha_final)
    
    print("Tiempo de carga: " +str(tiempo_total))
    print("Número total de ofertas: " + str(total_ofertas))
    print("Número total de ofertas con experticia junior: " +str(n_ofertas_experticia["junior"]))
    print("Número total de ofertas con experticia mid: " +str(n_ofertas_experticia["mid"]))
    print("Número total de ofertas con experticia senior: " +str(n_ofertas_experticia["senior"]))
    resultado = []
    headers = ["Fecha", "Título", "Experticia", "Ciudad", "País", "Tamaño", "Lugar Trabajo", "Contrata Ucranianos"]
    for job in lt.iterator(ofertas_en_rango_ordenadas):
        fila = [
            job["published_at"],
            job["title"],
            job["experience_level"],
            job["city"],
            job["country_code"],
            job["company_size"],
            job["workplace_type"],
            job["open_to_hire_ukrainians"]
        ]
        resultado.append(fila)
    print(tabulate(resultado, headers=headers, tablefmt="pretty"))


def print_req_4(control):
    """
        Función que imprime la solución del Requerimiento 4 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 4
    codigo_pais = input("Ingrese el código del país a consultar: ")
    fecha_inicial = input("Digite la fecha inicial del periodo a consultar: ")
    fecha_final = input("Digite la fecha final del periodo a consultar: ")
    check = input("Quiere ver impresas las listas en pantalla? (ponga \"si\" o \"no\")")
    
    resultado_req4 = controller.req_4(control, codigo_pais, fecha_inicial, fecha_final)
    
    if resultado_req4 == False:
        print("No hay ofertas de trbajo en el país solicitado y en el rango dado. ")
    else:  
    
        print("El total de ofertas en el país en el periodo de consulta es: " + str(resultado_req4[0]))
        print("El total de empresas que publicaron al menos una oferta en el país de consulta es: " + str(resultado_req4[1]))
        print("Número total de ciudades del país de consulta en las que se publicaron ofertas es: " + str(resultado_req4[2]))
        print("La ciudad del país con mayor número de ofertas es " + str(resultado_req4[3]) + ", con " + str(resultado_req4[4]) + " ofertas.")
        print("La ciudad del país con menor número de ofertas es " + str(resultado_req4[5]) + ", con " + str(resultado_req4[6]))
        if check == "si":
            print(mostrar_en_pantalla_requerimiento_4(resultado_req4[7]))
        
        print("El tiempo de carga fue de: " + str(resultado_req4[8]))


def print_req_5(control):
    """
        Función que imprime la solución del Requerimiento 5 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 5
    pass


def print_req_6(control):
    """
        Función que imprime la solución del Requerimiento 6 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 6
    cantidad_n_ciudades = int(input("Ingrese la cantidad de ciudades a clasificar: "))
    verificacion_pais = input("¿Quiere digitar un país para hacer la búsqueda? Responda \"True\" o \"False\".")
    if verificacion_pais == "True":
        codigo_pais = input("Digite el código del país de consulta: ")
    else:
        codigo_pais = False
    nivel_experticia = input("Digite el nivel de experticia: ")
    fecha_inicial = input("Digite la fecha inicial del periodo a consultar: ")
    fecha_final = input("Digite la fecha final del periodo a consultar: ")
    resultado_req_6 = controller.req_6(control, cantidad_n_ciudades, codigo_pais, nivel_experticia, fecha_inicial, fecha_final)
    check = input("Quiere ver impresas las ofertas de trabajo en pantalla? (digite \"si\" o \"no\")")
    print("El total de ciudades que cumplen con las condiciones de la consulta es: " + str(resultado_req_6[0]))
    print("El total de empresas que cumplen con las condiciones de la consulta es: " + str(resultado_req_6[1]))
    print("El total de ofertas publicadas que cumplen con las condiciones de la consulta es: " + str(resultado_req_6[2]))
    if verificacion_pais == "True":
        print("El promedio del salario ofertado de todas las ofertas que cumplen con las condiciones de la consulta es: " + str(resultado_req_6[3]))
    print("Nombre de la ciudad con mayor cantidad de ofertas de empleos es: " + str(resultado_req_6[4]) + ", con un conteo de: " + str(resultado_req_6[5]))
    print("Nombre de la ciudad con menor cantidad de ofertas de empleos es: " + str(resultado_req_6[6]) + ", con un conteo de: " + str(resultado_req_6[7]))
    if check == "si":
        print(mostrar_en_pantalla_requerimiento_6(resultado_req_6[8]))
        
    print("El tiempo de carga fue de: " + str(resultado_req_6[9]))


def print_req_7(control):
    """
        Función que imprime la solución del Requerimiento 7 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 7
    fecha_inicial = input("Digite la fecha inicial del periodo a consultar: ")
    fecha_final = input("Digite la fecha final del periodo a consultar: ")
    n_paises = int(input("Digite el número de paises: "))
    total_ofertas, pais_con_mas_ofertas, conteo_pais_con_mas_ofertas, lista_final, tiempo_total = controller.req_7(control, n_paises, fecha_inicial, fecha_final)
    print("Tiempo de carga: " + str(tiempo_total))
    print(" ")
    print("Total ofertas: " + str(total_ofertas))
    print(" ")
    print("Pais con mas ofertas: " + str(pais_con_mas_ofertas) + " Conteo: " +str(conteo_pais_con_mas_ofertas))
    print(" ")
    print(lista_final)
    
    


def print_req_8(control):
    """
        Función que imprime la solución del Requerimiento 8 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 8
    pass
def mostrar_en_pantalla(lst):
    
    resultado = []
    for x in lt.iterator(lst):
        for y in x:
            if(y == "published_at"):
                resultado.append(x["city"])
            if(y == "title"):
                resultado.append(x["published_at"])
            if(y == "company_name"):
                resultado.append(x["experience_level"])
            if(y == "experience_level"):
                resultado.append(x["country_code"])
            if(y == "country_code"):
                resultado.append(x["company_name"])
            if(y == "city"):
                resultado.append(x["title"])
        print("\n")
        print(tabulate([resultado], headers=["Fecha", "Título", "Empresa", "Experiencia", "País", "Ciudad"], tablefmt="pretty"))
        resultado = []

def mostrar_en_pantalla_requerimiento_4(lst):
    
    resultado = []
    for x in lt.iterator(lst):
        for y in x:
            if(y == "published_at"):
                resultado.append(x["city"])
            if(y == "title"):
                resultado.append(x["published_at"])
            if(y == "experience_level"):
                resultado.append(x["experience_level"])
            if(y == "company_name"):
                resultado.append(x["workplace_type"])
            if(y == "city"):
                resultado.append(x["company_name"])
            if(y == "workplace_type"):
                resultado.append(x["title"])
            if(y == "workplace_type"):
                if(x["workplace_type"] == "remote"):
                    resultado.append(True)
                else:
                    resultado.append(False)
            if(y == "open_to_hire_ukrainians"):
                resultado.append(x["open_to_hire_ukrainians"])
        print("\n")
        print(tabulate([resultado], headers=["Fecha", "Empresa", "Titulo", "Trabajo Remoto", "Tipo de Trabajo", "Experiencia", "Ciudad", "Abierto a contratar Ucranianos"], tablefmt="pretty"))
        resultado = []
        
def mostrar_en_pantalla_requerimiento_6(lst):
    
    resultado = []
    for x in lt.iterator(lst):
        for y in x:
            if(y == "Nombre ciudad"):
                resultado.append(x["Nombre ciudad"])
            if(y == "Conteo ofertas"):
                resultado.append(x["Conteo ofertas"])
            if(y == "Promedio del salario"):
                resultado.append(x["Promedio del salario"])
            if(y == "Cantidad empresas"):
                resultado.append(x["Cantidad empresas"])
            if(y == "Empresa con más ofertas"):
                resultado.append(x["Empresa con más ofertas"])
            if(y == "Conteo empresa con más ofertas"):
                resultado.append(x["Conteo empresa con más ofertas"])
            if(y == "Información mejor oferta"):
                resultado.append(x["Información mejor oferta"])
            if(y == "Información peor oferta"):
                resultado.append(x["Información peor oferta"])
        print("\n")
        print(tabulate([resultado], headers=["Nombre ciudad", "Conteo ofertas", "Promedio salario",
                                             "Cantidad empresas", "Empresa con más ofertas",
                                             "Conteo empresa con más ofertas", "Información mejor oferta", "Información peor oferta"], tablefmt="pretty", colalign="center"))
        resultado = []

def decidir_metodo_ordenamiento(control):
    print("Seleccione el metodo de ordenamiento: ")
    print("1. Insertion sort")
    print("2. Mergesort")
    print("3. Quicksort")
    print("4. Selectionsort")
    print("5. Shellsort")

    rta = int(input())
    print("Digite cuantos elementos quiere ver: ")
    cantidad = int(input())
    lista_ordenada = controller.decidir_metodo_sort(rta, control)
    cantidad_ordenada = lt.subList(lista_ordenada, 1, cantidad)
    
    return cantidad_ordenada

# main del reto
def menu_cycle():
    """
    Menu principal
    """
    working = True
    #ciclo del menu
    while working:
        print_menu()
        inputs = input('Seleccione una opción para continuar\n')
        if int(inputs) == 1:
            decisión = input("En qué estructura de datos quiere guardar la información: escriba ARRAY_LIST o SINGLE_LINKED. ")
            print("Seleccione que dimensiones quiere cargar de los datos: ")
            
            print("1. 10-por")
            print("2. 20-por")
            print("3. 30-por")
            print("4. 40-por")
            print("5. 50-por")
            print("6. 60-por")
            print("7. 70-por")
            print("8. 80-por")
            print("9. 90-por")
            print("10. small")
            print("11. medium")
            print("12. large")
            tamanio = input()
            if int(tamanio) == 1:
                tamanio_carga = "10-por-"
            elif int(tamanio) == 2:
                tamanio_carga = "20-por-"
            elif int(tamanio) == 3:
                tamanio_carga = "30-por-"
            elif int(tamanio) == 4:
                tamanio_carga = "40-por-"
            elif int(tamanio) == 5:
                tamanio_carga = "50-por-"
            elif int(tamanio) == 6:
                tamanio_carga = "60-por-"
            elif int(tamanio) == 7:
                tamanio_carga = "70-por-"
            elif int(tamanio) == 8:
                tamanio_carga = "80-por-"
            elif int(tamanio) == 9:
                tamanio_carga = "90-por-"
            elif int(tamanio) == 10:
                tamanio_carga = "small-"
            elif int(tamanio) == 11:
                tamanio_carga = "medium-"
            elif int(tamanio) == 12:
                tamanio_carga = "large-"
                
            nombre_archivo_jobs = tamanio_carga + "jobs.csv"
            nombre_archivo_employment = tamanio_carga + "employments_types.csv"
            nombre_archivo_skills = tamanio_carga + "skills.csv"
            nombre_archivo_multilocations = tamanio_carga + "multilocations.csv"
            
            tupla_nombres = nombre_archivo_jobs, nombre_archivo_employment, nombre_archivo_skills, nombre_archivo_multilocations
            
            
            # Se crea el controlador asociado a la vista
            control = new_controller(decisión)

            
            print("Cargando información de los archivos ....\n")
            data = load_data(control, tupla_nombres)
            lst_jobs = data[1]

            
            
            print('Ofertas de trabajo cargadas: ' + str(data[0]))
            print('Ubicaciónes de la empresa cargadas: ' + str(data[2]))
            print('Habilidades solicitadas cargadas: ' + str(data[3]))
            print('Tipos de contratación cargados: ' + str(data[4]))
            print("El tiempo de carga fue de: " + str(data[5]) + "ms.")
            
            print("Seleccione el metodo de ordenamiento: ")
            print("1. Insertion sort")
            print("2. Mergesort")
            print("3. Quicksort")
            print("4. Selectionsort")
            print("5. Shellsort")

            rta = int(input("Opcion: "))
            
            controller.decidir_metodo_sort(rta, control["model"]["jobs"])
            

            primeros_3 = controller.imprimir_n(control, 1, 3)
   
            ultimos_3 = controller.imprimir_n(control, lt.size(control["model"]["jobs"])-2,3)

            print("Primeras 3 ofertas de trabajo: ")
            mostrar_en_pantalla(primeros_3)
            print("Últimas 3 ofertas de trabajo: ")
            mostrar_en_pantalla(ultimos_3)
                
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
            print(decidir_metodo_ordenamiento(control["model"]["jobs"]))
            
            

        elif int(inputs) == 0:
            working = False
            print("\nGracias por utilizar el programa") 
        else:
            print("Opción errónea, vuelva a elegir.\n")
    sys.exit(0)

default_limit = 1000
# main del ejercicio
if __name__ == "__main__":
    # TODO ajuste del main para reserar memoria (parte 2)
    threading.stack_size(67108864*2) # 128MB stack
    sys.setrecursionlimit(default_limit*1000000)
    thread = threading.Thread(target=menu_cycle)
    thread.start()