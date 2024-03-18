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
from tabulate import tabulate
import traceback
import threading


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""


def new_controller(tipo_lst):
    """
        Se crea una instancia del controlador
    """
    control = controller.new_Controller(tipo_lst)
    return control 

    #TODO: Llamar la función del controlador donde se crean las estructuras de datos
    


def print_menu():
    print("Bienvenido a Just Join IT, seleccione una opción:")
    #print("10- Elegir tipo de lista")
    print("1- Cargar información")
    print("2- Listar las últimas N ofertas según experticia y país (Req 1)")
    print("3- Listar las últimas N ofertas según empresa y ciudad (Req 2)")
    print("4- Consultar ofertas publicadas en una empresa específica durante un periodo de tiempo (Req 3)")
    print("5- Consultar ofertas publicadas en un país específico durante un periodo de tiempo (Req 4)")
    print("6- Consultar las ofertas que se publicaron en una ciudad durante un periodo de tiempo (Req 5)")
    print("7- Clasificar N ciudades con mayor número de ofertas por experticia en un rango de tiempo (Req 6)")
    print("8- Clasificar N países con mayor número de ofertas de trabajo según nivel de experticia (Req 7)")
    print("9- Escoger ordenamiento")
    print("10- Ordenar")
    print("0- Salir")    


def loadData(control, muestra):
    """
    Carga los datos
    """
    jobs = controller.loadData(control, muestra)
    return jobs
    #TODO: Realizar la carga de datos
    

def print_data(control, id):
    """
        Función que imprime un dato dado su ID
    """
    #TODO: Realizar la función para imprimir un elemento
    pass

def print_ultimosNPaisExp(control, codpais, exp, n):
 
    a, size, tiempo = controller.ultimosNPaisExp(control, codpais, exp, n)
    sizeof = lt.size(a)
    print ("Hay", size, "ofertas de esa ciudad y esa empresa.")

    final = [0]*sizeof

    i = 0
    while i < sizeof:
        temp = {}
        for key in a["elements"][i]:
            if key == "country_code"  or key == "published_at" or key == "city" or key == "company_name" or key == "title" or key == "experience_level" or key == "remote_interview" or key == "workplace_type":
                temp[key] = a["elements"][i][key]

        final[i] = temp
        i+=1

    table = tabulate(final, headers = "keys", tablefmt = "fancy_outline")
    print (table)  
    print("") 
    DeltaTime = f"{tiempo:.3f}"
    print("El tiempo es:",
    str(DeltaTime), "[ms]")

    

def print_req_2(control, n , city, emp):
    """
        Función que imprime la solución del Requerimiento 2 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 2
    ofertas, size, tiempo = controller.req_2(control, n, city, emp)
    sizeof = lt.size(ofertas)
    print ("Hay", size, "ofertas de esa ciudad y esa empresa.")

    final = [0]*sizeof
    
    i = 0
    while i < sizeof:
        temp = {}
        for key in ofertas["elements"][i]:
            if key == "country_code"  or key == "published_at" or key == "city" or key == "company_name" or key == "title" or key == "experience_level" or key == "remote_interview" or key == "workplace_type":
                temp[key] = ofertas["elements"][i][key]

        final[i] = temp
        i+=1

    table = tabulate(final, headers = "keys", tablefmt = "fancy_outline")
    print (table)  
    print("") 
    DeltaTime = f"{tiempo:.3f}"
    print("El tiempo es:",
    str(DeltaTime), "[ms]")



def print_req_3(control, empresa, fecha_i, fecha_f):

    ofers, tiempo = controller.req_3(control, empresa, str(fecha_i), str(fecha_f))
    sizeof = lt.size(ofers[0])
    print ("Hay", ofers[1], " ofertas con experticia junior")
    print ("Hay", ofers[1], " ofertas con experticia junior")
    print ("Hay", ofers[2], " ofertas con experticia mid")
    print ("Hay", ofers[3], " ofertas con experticia senior")

    final = [0]*sizeof

    i = 0
    while i < sizeof:
        temp = {}
        for key in ofers["elements"][i]:
            if key == "country_code"  or key == "published_at" or key == "city" or key == "company_name" or key == "title" or key == "experience_level" or key == "remote_interview" or key == "workplace_type":
                temp[key] = ofers["elements"][i][key]

        final[i] = temp
        i+=1

    table = tabulate(final, headers = "keys", tablefmt = "fancy_outline")
    print (table)  
    print("") 
    DeltaTime = f"{tiempo:.3f}"
    print("El tiempo es:",
    str(DeltaTime), "[ms]")
    
    
    
    """
        Función que imprime la solución del Requerimiento 3 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 3
    pass


def print_req_4(control, codPais, datei, datef):
    """
        Función que imprime la solución del Requerimiento 4 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 4

    rango, empresas, cities, tiempo = controller.paisRangoT(control, codPais, datei, datef)
    sizeof = lt.size(rango)
    sizeemp =lt.size(empresas)

    print ("Hay",sizeof, "ofertas")
    print ("Hay ofertas de", sizeemp, "empresas diferentes")
    if cities[0] == 0:
        print ("No hay ciudad con mayor número de ofertas")
    else: 
        print ("La ciudad con más ofertas es", cities[0], "con,", cities[1], "ofertas.")
    if cities[2] == 0:
        print ("No hay ciudad con menor número de ofertas")
    else: 
        print ("La ciudad con más ofertas es", cities[2], "con,", cities[3], "ofertas.")


    if sizeof != 0: 
        final_primeros3=[0,0,0]
        i=0
        while i<3:
            temp={}
            for key in rango["elements"][i]:
                if key == "title" or key == "published_at" or key == "experience_level" or key == "company_name" or key == "city" or key == "workplace_type" or key == "open_to_hire_ukrainians":
                  temp[key] = rango["elements"][i][key]

            final_primeros3[i]=temp
            i+=1
    
        final_ultimos3=[0,0,0]
        i=0
        while i<3:
            temp={}
            numjobs=sizeof
            for key in rango['elements'][numjobs-i-1]:
                if key == "title" or key == "published_at" or key == "experience_level" or key == "company_name" or key == "city" or key == "workplace_type" or key == "open_to_hire_ukrainians":
                    temp[key]=rango['elements'][numjobs-i-1][key]

            final_ultimos3[i]=temp
            i+=1
                
        #Printing de las sublistas depuradas
        print("Los primeros tres son:")
        print("")
        table_primeros3 = tabulate(final_primeros3,headers='keys',tablefmt="fancy_outline")
        print(table_primeros3)
        print("")
    
        print("Los ultimos tres son:")
        print("")
        table_ultimos3 = tabulate(final_ultimos3,headers='keys',tablefmt="fancy_outline")
        print(table_ultimos3)
        print("") 

    DeltaTime = f"{tiempo:.3f}"
    print("El tiempo es:",
    str(DeltaTime), "[ms]")

    

    


def print_req_5(control, ciudad, fecha_inicial, fecha_final):
    """
        Función que imprime la solución del Requerimiento 5 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 5
    
    #ans=[sublistCities, mayorNombre, mayorNum, menorNombre, menorNum, total_empresas]
    answer = controller.req_5(control, ciudad, fecha_inicial, fecha_final)

    ans = answer[0]
    tiempo = answer[1]
    
    size_sortedJobs=lt.size(ans[0])

    final_primeros3=[0,0,0]
    i=0
    while i<3:
        temp={}
        for key in ans[0]['elements'][i]:
            if key=="title" or key=="company_name" or key=="company_size" or key=="workplace_type" or key=="published_at":
                temp[key]=ans[0]['elements'][i][key]

        final_primeros3[i]=temp
        i+=1

    final_ultimos3=[0,0,0]
    i=0
    while i<3:
        temp={}
        numjobs = size_sortedJobs 
        for key in ans[0]['elements'][numjobs-i-1]:
            if key=="title" or key=="company_name" or key=="company_size" or key=="workplace_type" or key=="published_at":
                temp[key]=ans[0]['elements'][numjobs-i-1][key]

        final_ultimos3[i]=temp
        i+=1    
    

    print("Los primeros tres son:")
    print("")
    table_primeros3 = tabulate(final_primeros3,headers='keys',tablefmt="fancy_outline")
    print(table_primeros3)
    print("")
    
    print("Los ultimos tres son:")
    print("")
    table_ultimos3 = tabulate(final_ultimos3,headers='keys',tablefmt="fancy_outline")
    print(table_ultimos3)
    print("") 


    print("Hay un total de",size_sortedJobs,"ofertas de trabajo en la ciudad entre", fecha_inicial,"y",fecha_final,".")
    
    print("Hay un total de",ans[5],"empresas ofreciendo trabajo")
    
    print("La empresa con mayor ofertas fue",ans[1],"con",ans[2],"ofertas.")
    print("La empresa con menor ofertas fue",ans[3],"con",ans[4],"ofertas.")
    print("")
    DeltaTime = f"{tiempo:.3f}"
    print("El tiempo es:",
    str(DeltaTime), "[ms]")
            


def print_req_6(control, numCiudades, codPais, exp_level, fecha_inicial, fecha_final):
    """
        Función que imprime la solución del Requerimiento 6 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 6
    
    #ans=[ultima_lista, size_sublistN_cities, empresas_totales, sumatoria_jobs, (sumatoria_salario_totales/size_sublistN_cities), ciudad_más_ofertas, ciudad_menos_ofertas]
    #ans=[ultima_lista, size_sublistN_cities, empresas_totales, sumatoria_jobs, (sumatoria_salario_totales/size_sublistN_cities), ciudad_más_ofertas, ciudad_menos_ofertas]
    answer=controller.req_6(control, numCiudades, codPais, exp_level, fecha_inicial, fecha_final)

    ans = answer[0]
    tiempo = answer[1]

    """"
    ans=[ultima_lista, size_sublistN_cities, empresas_totales, sumatoria_jobs, salario_promedio_total, 
    ciudad_más_ofertas, ciudad_menos_ofertas]
    """

    size_of = lt.size(ans[0])
    ciudad_mayor = (ans[5])[0]
    mayor = (ans[5])[1]

    ciudad_menor = (ans[6])[0]
    menor = (ans[6])[1]

    print ("Hay ", ans[1], "ciudades.")
    print("Hay ", ans[2], "empresas.")
    print("Hay ", size_of, "ofertas.")
    print("El salario promedio es de ", ans[4], "PLN.")
    print ("La ciudad con mayor número de ofertas es ", ciudad_mayor , "con ", mayor, "ofertas.")
    print ("La ciudad con menor número de ofertas es ", ciudad_menor , "con ", menor, "ofertas.")
    #Tabla ofertas
    
    final_sortedJobs=[0]*size_of
    
    i=0
    while i<size_of:
        temp={}
        for key in ans[0]['elements'][i]:
            if key=="Ciudad" or key=="Numero_total_ofertas" or key=="Salario_promedio" or key=="Numero_total_empresas" or key=="Empresa_con_mas_ofertas" or key == "Mejor_oferta" or key == "Peor_oferta":
                temp[key]=ans[0]['elements'][i][key]

        final_sortedJobs[i]=temp
        i+=1
    
    
    table_sortedJobs = tabulate(final_sortedJobs,headers='keys',tablefmt="fancy_outline")
    print("")
    print(table_sortedJobs)
    print("")
    DeltaTime = f"{tiempo:.3f}"
    print("El tiempo es:",
    str(DeltaTime), "[ms]")
    


def print_req_7(control, numPaises, fecha_inicial, fecha_final):
    """
        Función que imprime la solución del Requerimiento 7 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 7
    answer=controller.req_7(control, numPaises, fecha_inicial, fecha_final)
    ans = answer[0]
    tiempo = answer[1]
    
    """
    ans=[listImpresion, lt.size(listTotalJobs), lt.size(jobsxciudades),
    [ciudadMayorJobs, ciudadMayorJobs_Num], paisMayorOfertas]
    """
    print("Hay", ans[1], "ofertas en total.")
    print("Hay", ans[2], "ciudades.")
    print("El país con más ofertas es", ans[3][0], "con", ans[3][1], "ofertas.")
    print("La ciudad con más ofertas es", ans[4][0], "con", ans[4][1], "ofertas.")
    print("")
    print("//////")

    for pais in lt.iterator(ans[0]):
        code = (lt.getElement(pais, 0))["País"]
        print("El listado de", code, ":")

        size_pais=lt.size(pais)
    
        final=[0]*size_pais
    
        i=0
        while i<size_pais:
            temp={}
            for key in pais['elements'][i]:
                if key=="Nivel de experiencia" or key=="Numero_habilidades_solicitadas" or key=="Habilidad_mas_solicitada" or key=="Habilidad_menos_solicitada" or key=="Promedio_nivel_mínimo_de_hablidades" or key=="Numero_empresas_totales" or key=="Empresa_mayor_ofertas" or key=="Empresa_menor_ofertas" or key=="Numero_empresas_multisedes" :
                    temp[key]=pais['elements'][i][key]

            final[i]=temp
            i+=1
    
    
        table = tabulate(final,headers='keys',tablefmt="fancy_outline")
        print("")
        print(table)
        print("")
    DeltaTime = f"{tiempo:.3f}"
    print("El tiempo es:",
    str(DeltaTime), "[ms]")
    




def print_ordenar(control):
    """
        Función que imprime la solución del Requerimiento 7 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 7
    print("Ordenando las ofertas ....")
    result=controller.sortJobsDate(control)
    sortedJobs = result[0]
    DeltaTime = f"{result[1]:.3f}"
    print("El tiempo es:",
    str(DeltaTime), "[ms]")
    
    final_primeros3=[0,0,0]
    i=0
    while i<3:
        temp={}
        for key in sortedJobs['elements'][i]:
            if key=="title" or key=="company_name" or key=="city" or key=="country_code" or key=="published_at" or key=="experience_level":
                temp[key]=sortedJobs['elements'][i][key]

        final_primeros3[i]=temp
        i+=1
    
    final_ultimos3=[0,0,0]
    i=0
    while i<3:
        temp={}
        numjobs=sortedJobs["size"]
        for key in sortedJobs['elements'][numjobs-i-1]:
            if key=="title" or key=="company_name" or key=="city" or key=="country_code" or key=="published_at" or key=="experience_level":
                temp[key]=sortedJobs['elements'][numjobs-i-1][key]

        final_ultimos3[i]=temp
        i+=1
                
    #Printing de las sublistas depuradas
    print("Los primeros tres son:")
    print("")
    table_primeros3 = tabulate(final_primeros3,headers='keys',tablefmt="fancy_outline")
    print(table_primeros3)
    print("")
    
    print("Los ultimos tres son:")
    print("")
    table_ultimos3 = tabulate(final_ultimos3,headers='keys',tablefmt="fancy_outline")
    print(table_ultimos3)
    print("")
            
            
    pass


def print_seleccion_ordenamiento(control):
    """
        Función que imprime la solución del Requerimiento 8 en consola
    """
    opciones = """Seleccione el algoritmo de ordenamiento:
                1. Selection Sort ||
                 2. Insertion Sort ||
                 3. Shell Sort ||
                 4. Merge Sort ||
                 5. Quick Sort ||
                 6. Heap Sort ||
                 7. Bogo Sort ||
                 8. Custom Sort (Tim Sort):"""
    ordenamiento_picked=input(opciones)
    ordenamiento_picked=int(ordenamiento_picked)
    
    return ordenamiento_picked



# Se crea el controlador asociado a la vista

opciones_yes = ("s", "S", "1", True, "true", "True", "si", "Si", "SI")

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
            muestra = input("Indique el tamaño de la muestra: ")
            
            
            list = input("Desea utiilizar una lista enlazada?: ") 
            if list in opciones_yes:
                tipo_lst = "SINGLE_LINKED"
            else: 
                tipo_lst = "ARRAY_LIST"
                
            control = new_controller(tipo_lst)
         
            print("Cargando información de los archivos ....\n")
            

            numJobs, primeros3, ultimos3 = loadData(control, muestra)
            
            print("Se cargo",numJobs,"ofertas de trabajo publicadas")
            print("")
            
            #Depuración de la información de las sublistas de los primeros y ultimos 3
            final_primeros3=[0,0,0]
            i=0
            while i<3:
                temp={}
                for key in primeros3['elements'][i]:
                    if key=="title" or key=="company_name" or key=="city" or key=="country_code" or key=="published_at" or key=="experience_level":
                        temp[key]=primeros3['elements'][i][key]
        
                final_primeros3[i]=temp
                i+=1
            
            final_ultimos3=[0,0,0]
            i=0
            while i<3:
                temp={}
                for key in ultimos3['elements'][i]:
                    if key=="title" or key=="company_name" or key=="city" or key=="country_code" or key=="published_at" or key=="experience_level":
                        temp[key]=ultimos3['elements'][i][key]
        
                final_ultimos3[i]=temp
                i+=1
            
            #Printing de las sublistas depuradas
            print("Los primeros tres son:")
            print("")
            table_primeros3 = tabulate(final_primeros3,headers='keys',tablefmt="fancy_outline")
            print(table_primeros3)
            print("")
            
            print("Los ultimos tres son:")
            print("")
            table_ultimos3 = tabulate(final_ultimos3,headers='keys',tablefmt="fancy_outline")
            print(table_ultimos3)
            print("")
          

            
        elif int(inputs) == 2:
            pais = str(input("Ingrese el codigo del pais: "))
            exp = str(input("Ingrese el nivel de experiencia (junior, mid, o senior): "))
            n = int(input("Ingresa la cantidad de trabajos a consultar: "))
            print_ultimosNPaisExp(control, pais, exp, n)

        elif int(inputs) == 3:
            n = int(input("Número N de datos más recientes que desea conocer: "))
            city = input("Ciudad: ")
            emp = input("Empresa: ")
            print_req_2(control, n, city, emp)

        elif int(inputs) == 4:
            empresa=  str(input("ingrese el nombre de la empresa "))
            fecha_i=  str(input("ingrese la fecha inicial (forma a-m-d)"))
            fecha_f=  str(input("ingrese la fecha final (forma a-m-d) "))
            print_req_3(control, empresa, fecha_i, fecha_f)

        elif int(inputs) == 5:
            datei = input("Ingrese la fecha mínima (forma a-m-d): ")
            datef = input("Ingrese la fecha máxima (forma a-m-d): ")
            codPais= input("Ingrese el código de  un país: ")
            print_req_4(control, codPais, datei, datef)



        elif int(inputs) == 6:
            ciudad=input("Digite el nombre de la ciudad que quiere buscar: ")
            fecha_inicial=input("Digite la fecha inicial del periodo a consultar: ")
            fecha_final=input("Digite la fecha final del periodo a consultar: ")
            print_req_5(control,ciudad, fecha_inicial, fecha_final)

        elif int(inputs) == 7:
            
            numCiudades = int(input("Ingrese el número N de ciudades a consultar: "))
            
            eleccion_pais=input("Desea consultar en un pais específico?")
            if eleccion_pais in opciones_yes:
                codPais=input("Digite el código del país que quiere consutlar: ")
            else:
                codPais=None   
            
            exp_level = input("Ingrese el nivel de experiencia: ")
            fecha_inicial = input("Ingrese la fecha mínima (aa-mm-dd): ")
            fecha_final = input("Ingrese la fecha máxima (aa-mm-dd): ")

            
            print_req_6(control, numCiudades, codPais, exp_level, fecha_inicial, fecha_final)


        elif int(inputs) == 8:
            
            numPaises=int(input("Digite el número de países que desea consultar: "))
            
            fecha_inicial=input("Digite la fecha inicial del periodo a consultar: ")
            fecha_final=input("Digite la fecha final del periodo a consultar: ")
            
            
            print_req_7(control, numPaises, fecha_inicial, fecha_final)
            
        elif int(inputs) == 9:
            
            picked=print_seleccion_ordenamiento(control)
            mensaje_picked=controller.setSortAlgorithm(picked)
            print(mensaje_picked)
            

        elif int(inputs) == 10:
            print_ordenar(control)

        
        elif int(inputs) == 0:
            working = False
            print("\nGracias por utilizar el programa") 
        else:
            print("Opción errónea, vuelva a elegir.\n")
            
    sys.exit(0)

# main del reto
if __name__ == "__main__":
    default_limit=1000
    threading.stack_size(67108864*2) # 128MB stack
    sys.setrecursionlimit(default_limit*1000000)
    thread = threading.Thread(target= menu_cycle)
    
    #el thread.start() nos está poniendo problema pero no sabemos porque, el error solo aparece en el terminal y no afecta al programa
    thread.start()
    
