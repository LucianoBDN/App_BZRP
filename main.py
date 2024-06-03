from class_video import *
from data import *
from os import system
"""
Consigna:
1. IMPLEMENTAR LOS METODOS VACIOS DE LA CLASE VIDEO

2. CREAR UN MENU DE USUARIO CON LAS SIGUIENTES OPCIONES:

A. NORMALIZAR OBJETOS: para cada video de la lista, se deberá llamar a los métodos de instancia: dividir_titulo, 
obtener_codigo_url y formatear_fecha, dado que la lista de objetos que nos pasan no cumple con las normas de estandarización 
de videos que nos solicitan.
B. MOSTRAR TEMAS: se deberá mostrar la lista de todos los temas
C. ORDENAR TEMAS: los temas se ordenarán por número de sesión de menor a mayor.
D. PROMEDIO DE VISTAS: mostrar el promedio de vistas expresado en k.
E. MAXIMA REPRODUCCION: mostrar el o los videos con mayor cantidad de vistas.
F. BUSQUEDA POR CODIGO: mostrar los videos cuyo código comiencen con la palabra "nick"
G. LISTAR POR COLABORADOR: el usuario ingresa el nombre de un colaborador y el programa deberá listar todos los videos de 
ese colaborador.
H. SALIR 

NOTA: 
1. Las opciones BCDEFG no serán accesibles si no se normalizan previamente los datos.
2. Todas las opciones tienen que estar resueltas en metodos de la clase Video que reciban una lista de videos sumado a los
parametros necesarios para lograr el objetivo y mantener independencia de código.
"""



bandera_cargada = False
bandera_seguir = True
while bandera_seguir == True:
    opcion = input("A.Normalizar objetos\nB.Mostrar temas\nC.Ordenar temas menos a mayor\nD.Promedio de vistas\nE.Mas reproducciones\nF.Busqueda por codigo\nG.Listar por cantante\nH.Salir\n")
    opcion = opcion.lower()

    match opcion:
        case "a":
            Video.normaliza_elemtos(lista_videos)
            bandera_cargada = True    
        case "b":
            if bandera_cargada == True:
                 Video.mostrar_lista_videos(lista_videos)
            else:
                print("Por favor, ingrese primero a la opcion A para continuar")    
                
        case "c":
            if bandera_cargada == True:
                lista_ordenada = Video.ordenar_menor_a_mayor(lista_videos)
                Video.mostrar_lista_videos(lista_ordenada)
            else:
                print("Por favor, ingrese primero a la opcion A para continuar")

        case "d":
            if bandera_cargada == True:
                promedio = Video.promedio_sesion(lista_videos)
                print(f"El promedio de las visitas de todas las sesion es {promedio}K")
            else:
                print("Por favor, ingrese primero a la opcion A para continuar")

        case "e":
            if bandera_cargada == True:
                mas_vistos = Video.mas_vistos(lista_videos)
                Video.mostrar_lista_videos(mas_vistos)
            else:
                print("Por favor, ingrese primero a la opcion A para continuar")

        case "f":
            if bandera_cargada == True:
                codigo = input("ingrese el codigo que desea buscar: ")
                Video.buscar_por_codigo(lista_videos, codigo)
            else:
                print("Por favor, ingrese primero a la opcion A para continuar")

        case "g":
            if bandera_cargada == True:
                colaborador = input("Ingrese nombre del colaborador: ")
                Video.buscar_por_nombre(lista_videos, colaborador)
            else:
                print("Por favor, ingrese primero a la opcion A para continuar")
        case "h":
            break



    system("pause")
    system("cls")
    