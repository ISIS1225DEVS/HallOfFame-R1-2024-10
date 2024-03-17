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
default_limit = 1000
sys.setrecursionlimit(default_limit*10)
import controller
#TODO: import your list and sorting implementations
assert cf
from tabulate import tabulate
import threading
import traceback
import New_Functions as nf

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
    control = controller.new_controller()
    return control


def print_menu():
    print("Bienvenido")
    print("1- Cargar información")
    print("2- Últimas ofertas de trabajo según su país y nivel de experiencia")
    print("3- Última ofertas de trabajo por empresa y ciudad")
    print("4- Consultar las ofertas que publicó una empresa durante un periodo especifico de tiempo")
    print("5- Consultar las ofertas que se publicaron en un país durante un periodo de tiempo")
    print("6- Consultar las ofertas que se publicaron en una ciudad durante un periodo de tiempo")
    print("7- Clasificar las ciudades con mayor número de ofertas de trabajo por experiencia entre un rango de fechas")
    print("8- Clasificar los países con mayor número de ofertas de trabajo por divisa")
    print("9- Comparar el desempeño histórico de dos selecciones en torneos oficiales")
    print("0- Salir")


def load_data(control):
    """
    Carga los datos
    """
    jobs, skills, employment_types, multilocation = controller.load_data(control)
    return jobs, skills, employment_types, multilocation


def print_data(control, id):
    """
        Función que imprime un dato dado su ID
    """
    #TODO: Realizar la función para imprimir un elemento
    pass

def print_req_1(control, codigo, nivel_experiencia, numero):
    """
        Función que imprime la solución del Requerimiento 1 en consola
    """
    info = controller.req_1(control, codigo, nivel_experiencia)
    size = info[0]
    print(size)
    lista = info[1]
    contador = info[2]
    trabajito_numero = 1
    print("Según la condición", nivel_experiencia, "hay", contador, "ofertas que cumplen esta condición")
    while numero > 0 and size != 0 and trabajito_numero != size:
        valor = lista["elements"][size-trabajito_numero] 
        print("Trabajo #", trabajito_numero, "="*60)
        print("Titulo de la oferta:", valor["title"])
        print("Fecha de publicación:", valor["published_at"])
        print("Nombre de la empresa:", valor["company_name"])
        print("Nivel de experiencia:", nivel_experiencia)
        print("País de la empresa:", valor["country_code"])
        print("Ciudad de la empresa:", valor["city"])
        print("Tamaño de la empresa:", valor["company_size"])
        print("Tipo de ubicación de trabajo:", valor["workplace_type"])
        print("Disponible a contratar ucranianos:", valor["open_to_hire_ukrainians"])
        numero -= 1
        trabajito_numero += 1
    #se puede imprimir de una manera más linda


def print_req_2(control, company_name, ciudad, numero):
    """
        Función que imprime la solución del Requerimiento 2 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 2
    info = controller.req_2(control, company_name, ciudad)
    size = info[0]
    lista = info[1]
    contador = info[2]
    trabajito_numero = 1
    diferencia = numero-size
    print("El número de ofertas que se ofrecen en", company_name, "y", ciudad, "son", contador)
    while numero > 0 and contador != 0 and trabajito_numero != size:
        print(numero, diferencia)
        valor = lista["elements"][size-trabajito_numero]
        print("Trabajo #", trabajito_numero, "="*60)
        print("Titulo de la oferta:", valor["title"])
        print("Fecha de publicación:", valor["published_at"])
        print("Nombre de la empresa:", company_name)
        print("Nivel de experiencia:", valor["experience_level"])
        print("Formato de aplicación (esta disponible en la plataforma web):", valor["display_offer"])
        print("Tipo de trabajo:", valor["workplace_type"])
        numero -= 1
        trabajito_numero += 1


def print_req_3(control, company_name, rango_abajo, rango_arriba):
    """
        Función que imprime la solución del Requerimiento 3 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 3
    info = controller.req_3(control, company_name, rango_abajo, rango_arriba)
    size = info[0]
    lista = info[1]
    num_ofertas_junior = info[2]
    num_ofertas_mid = info[3]
    num_ofertas_senior = info[4]
    trabajitos_numero = 1
    
    print("El número de ofertas que se ofrecen en", company_name, "y el rango", rango_abajo, "a", rango_arriba, "son", size)
    print("El número de ofertas junior son", num_ofertas_junior)
    print("El número de ofertas mid son", num_ofertas_mid)
    print("El número de ofertas senior son", num_ofertas_senior)
    
    for valor in lista:
        print("Trabajo #", trabajitos_numero, "="*60)
        print("Titulo de la oferta:", valor["title"])
        print("Fecha de publicación:", valor["published_at"])
        print("Nivel de experiencia:", valor["experience_level"])
        print("País de la empresa:", valor["country_code"])
        print("Ciudad de la empresa:", valor["city"])
        print("Tamaño de la empresa:", valor["company_size"])
        print("Tipo de trabajo:", valor["workplace_type"])
        print("Disponible a contratar ucranianos:", valor["open_to_hire_ukrainians"])
        trabajitos_numero += 1


def print_req_4(control):
    """
        Función que imprime la solución del Requerimiento 4 en consola.
        Consultar las ofertas que se publicaron en un país durante un periodo de tiempo.

        Argumentos:
            control Dict: Diccionario con la estructura de datos del modelo.

        Retorna:
            None
    """

    # Se solicita la información necesaria al usuario para realizar la consulta
    country_code = input("\nPor favor ingresa el código del país: ")
    start_date = input("Por favor ingresa la fecha de inicio de la consulta (En formato AAA-MM-DD): ")
    end_date = input("Por favor ingresa la fecha de fin de la consulta (En formato AAA-MM-DD): ")

    (
        jobs_found,
        qty_jobs_found,
        qty_companies,
        qty_cities,
        city_most_offers,
        city_less_offers,
        qty_city_most_offers,
        qty_city_less_offers
    ) = controller.req_4(control, country_code, start_date, end_date)

    keys_to_include = [ # Lista de llaves que se van a incluir en la tabla
        "published_at",
        "title",
        "experience_level",
        "company_name",
        "city",
        "workplace_type",
        "display_offer",
        "open_to_hire_ukrainians"
    ]

    # Se filtran las llaves que se van a incluir en la tabla
    jobs_found = [{key: job[key] for key in keys_to_include} for job in jobs_found]

    # Se tabula la información
    tabla = tabulate(jobs_found, headers = "keys", tablefmt = "fancy_grid")

    # Se imprime la información
    print(f"\nPara el país con código {country_code} y periodo de consulta ente {start_date} y {end_date} se encontraron:")
    print(f"\t- Total de ofertas: {qty_jobs_found}")
    print(f"\t- Total de empresas: {qty_companies}")
    print(f"\t- Total de ciudades: {qty_cities}")
    print(f"\t- La ciudad con más ofertas es {city_most_offers} con {qty_city_most_offers} ofertas.")
    print(f"\t- La ciudad con menos ofertas es {city_less_offers} con {qty_city_less_offers} ofertas.")

    print("\nLista de ofertas encontradas:")
    print(tabla, "\n")

    pass


def print_req_5(control, nombre, fecha_in, fecha_fin):
    """
        Función que imprime la solución del Requerimiento 5 en consola
    """
    data_structs= control["model"]["jobs"]
    result, time = controller.req_5(data_structs, nombre, fecha_in, fecha_fin)
    total_ofertas, total_empresas, e_mayor, mayor, e_menor, menor, tabla = result
    table_data, headers= tabla
    print('El total de ofertas publicadas en la ciudad en el periodo de consulta es de: ',total_ofertas )
    print('El total de empresas que publicaron por lo menos una oferta en la ciudad de consulta es de: ', total_empresas)
    print('La empresa con mayor número de ofertas es ', e_mayor, ' con ', mayor, 'oferta(s).')
    print('La empresa con menor número de ofertas es ', e_menor, ' con ', menor, 'oferta(s).')
    
    print(tabulate(table_data['elements'], headers=headers, tablefmt='fancygrid'))
    
    print(time)


def print_req_6(control, nivel_experiencia, rango_abajo, rango_arriba, numero, pais):
    """
        Función que imprime la solución del Requerimiento 6 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 6
    info = controller.req_6(control, nivel_experiencia, rango_abajo, rango_arriba, pais)
    #retorno -> #ciudades, #empresas, #ofertas_publicadas, salarios_promedio_total, ciudad_mayor_cantidad, ciudad_menor_cantidad, diccionario ciudades_info
    num_ciudades = info[0]
    num_empresas = info[1]
    num_ofertas_publicadas = info[2]
    salario_promedio_total = info[3]
    ciudad_mayor_cantidad = info[4]
    ciudad_menor_cantidad = info[5]
    size = info[7]
    info = info[6]
    ciudad_numero = 0
    ciudad_conteo = 0
    
    print("El número de ciudades que cumplen con las condiciones de consulta son: ", num_ciudades)
    print("El número de empresas que cumplen con las condiciones de consulta son: ", num_empresas)
    print("El número de ofertas publicadas que cumplen con las condiciones de consulta son: ", num_ofertas_publicadas)
    if pais != None:
        print("El promedio del salario ofertado de todas las ofertas que cumplen con las condiciones de la consulta es", salario_promedio_total)
    print("La ciudad con mayor cantidad de oferta de empleos es", ciudad_mayor_cantidad[0], "con", ciudad_mayor_cantidad[1], "empleos")
    print("La ciudad con menor cantidad de oferta de empleos es", ciudad_menor_cantidad[0], "con", ciudad_menor_cantidad[1], "empleos")
    while ciudad_conteo < numero and size != 0 and ciudad_numero != size:
        print("Ciudad #", ciudad_numero, "="*60)
        print("Nombre de la ciudad: ", info[ciudad_conteo]["nombre"])
        print("Total ofertas hechas: ", info[ciudad_conteo]["total_ofertas"])
        print("Salario promedio oferto: ", info[ciudad_conteo]["salario"])
        print("Número de empresas que publicaron por lo menos una oferta : ", nf.get_size(info[ciudad_conteo]["empresas"]))
        print("La empresa con el mayor número de ofertas es", info[ciudad_conteo]["mejor_empresa"]["elements"][0], "con", info[ciudad_conteo]["mejor_empresa"]["elements"][1])
        print("La mejor oferta fue: ", info[ciudad_conteo]["mejor_oferta"]["title"], "en la empresa", info[ciudad_conteo]["mejor_oferta"]["company_name"], "publicada el", info[ciudad_conteo]["mejor_oferta"]["published_at"])
        print("La peor oferta fue: ",  info[ciudad_conteo]["peor_oferta"]["title"], "en la empresa", info[ciudad_conteo]["peor_oferta"]["company_name"], "publicada el", info[ciudad_conteo]["peor_oferta"]["published_at"])
        ciudad_conteo += 1
        ciudad_numero += 1
        

def print_req_7(control, n, fecha_in, fecha_fin):
    """
        Función que imprime la solución del Requerimiento 7 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 7
    data_structs= control["model"]
    result, time = controller.req_7(data_structs, n, fecha_in, fecha_fin)
    total_ofertas, total_ciudades, p_mayor, mayor, c_mayor, cc_mayor, tabla = result
    table_data, headers, row_index = tabla
    print(headers)
    print('El total de ofertas publicadas en ', n, 'país(es) en el periodo de consulta es de: ',total_ofertas )
    print('El total de ciudades que publicaron una oferta en la ciudad de consulta es de: ', total_ciudades)
    print('El país con mayor número de ofertas es ', p_mayor, ' con ', mayor, ' oferta(s).')
    print('La ciudad con mayor número de ofertas es ', c_mayor, ' con ', cc_mayor, ' oferta(s).')

    print(tabulate(table_data['elements'], headers=headers, showindex= row_index, tablefmt='grid'))
    
    print(time)

def print_req_8(control):
    """
        Función que imprime la solución del Requerimiento 8 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 8
    pass


# Se crea el controlador asociado a la vista
control = new_controller()

# main del reto
if __name__ == "__main__":
    """
    Menu principal
    """
    working = True
    #ciclo del menu
    while working:
        print_menu()
        inputs = input('\nSeleccione una opción para continuar: ')
        if int(inputs) == 1:
            print("Cargando información de los archivos ....\n")
            data = load_data(control)
            print(data)
            #ordenado= controller.sort(control)
            
        elif int(inputs) == 2:
            codigo = input("Ingresar el código del país del cual se están buscando los trabajos: ")
            nivel_experiencia = input("Ingresar el nivel de experiencia del trabajo (junior, mid o senior): ")
            numero = int(input("Ingresar el número de trabajos que se quieren visualizar: "))
            print_req_1(control, codigo, nivel_experiencia, numero)

        elif int(inputs) == 3:
            company_name = input("Ingresar el nombre de la compañia: ")
            ciudad = input("Ingresar la ciudad donde está ubicado el trabajo: ")
            numero = int(input("Ingresar el número de trabajos que se quieren visualizar: "))
            print_req_2(control, company_name, ciudad, numero)

        elif int(inputs) == 4:
            company_name = input("Ingresar el nombre de la compañia: ")
            rango_abajo = input("Ingresar la fecha minima de la publicación del trabajo: ")
            rango_arriba = input("Ingresar la fecha máxima de la publicación del trabajo: ")
            print_req_3(control, company_name, rango_abajo, rango_arriba)
        
        elif int(inputs) == 5:
            print_req_4(control)

        elif int(inputs) == 6:
            nombre= input('Ciudad de la que quiere recibir ofertas: ')
            fecha_in= input('Fecha desde la cual quiere consultar ofertas: ')
            fecha_fin= input('Fecha hasta la cual quiere recibir ofertas: ')
            
            print_req_5(control, nombre, fecha_in, fecha_fin)

        elif int(inputs) == 7:
            numero = int(input("Ingresar el número de ciudades que se quieren visualizar: "))
            rango_abajo = input("Ingresar la fecha minima de la publicación del trabajo: ")
            rango_arriba = input("Ingresar la fecha máxima de la publicación del trabajo: ")
            nivel_experiencia = input("Ingresar el nivel de experiencia del trabajo (junior, mid o senior): ")
            opcion = input("Quieres ingresar el país (escribir si en minisculas o no en minisculas): ")
            if opcion == "si":
                pais = input("Ingresar el código del país: ")
            else:
                pais = None
            print_req_6(control, nivel_experiencia, rango_abajo, rango_arriba, numero, pais)

        elif int(inputs) == 8:
            n= int(input('Número de países que quiere consultar: '))
            fecha_in= input('Fecha desde la cual quiere consultar ofertas: ')
            fecha_fin= input('Fecha hasta la cual quiere recibir ofertas: ')
            
            print_req_7(control, n, fecha_in, fecha_fin)

        elif int(inputs) == 9:
            print_req_8(control)

        elif int(inputs) == 0:
            working = False
            print("\nGracias por utilizar el programa") 
        else:
            print("Opción errónea, vuelva a elegir.\n")
    threading.stack_size(67108864*2) # 128MB stack
    sys.setrecursionlimit(default_limit*1000000) 
    thread = threading.Thread(target=print_menu())
    thread.start()
    sys.exit(0)
