import os
import csv
import matplotlib.pyplot as plt


def main():
    while True:  # Se repetira hasta que haya un break
        print("\n\nSeleccione el numero de la opcion que desea utilizar\nMenú Principal:")
        print("1. Listar archivos en la ruta actual o ingresar una ruta")
        print("2. Procesar archivo de texto (.txt)")
        print("3. Procesar archivo separado por comas (.csv)")
        print("4. Salir")
        opcion = input("Seleccione una opcion: ")

        if opcion == '1':
            listar_archivos()
        elif opcion == '2':
            submenu_txt()
        elif opcion == '3':
            submenu_csv()
        elif opcion == '4':
            print("Gracias por utilizarme!!!")
            break  # se sale completamente del programa en general
        else:
            print("Asegurate de ingresar un numero que este dentro de las opciones disponibles")



# funcion como ls de git
def listar_archivos():
    eleccion = input("Quieres listar la ruta actual? (si/no): ")
    if eleccion.lower() == 'si':
        ruta = os.getcwd()
    else:
        ruta = input("Ingrese la ruta a listar: ")
        if not os.path.exists(ruta):
            print("La ruta ingresada no se pudo encontrar, porfavor verifiquela")
            return

    archivos = os.listdir(ruta)
    print(f"Archivos en {ruta}:")
    for archivo in archivos:
        print(archivo)



def submenu_txt():
    print("\nProcesar archivo de texto (.txt):")
    print("a. Contar numero de palabras")
    print("b. Reemplazar una palabra por otra")
    print("c. Contar el numero de caracteres")
    opcion = input("Seleccione una opcion: ")

    if opcion.lower() == 'a':
        contar_palabras()
    elif opcion.lower() == 'b':
        reemplazar_palabra()
    elif opcion.lower() == 'c':
        contar_caracteres()
    else:
        print("Asegurate de ingresar una letra que este dentro de las opciones disponibles")



def contar_palabras():
    nombre_archivo = input("Ingrese el nombre del archivo de texto: ")
    archivo = open(nombre_archivo, 'r')
    contenido = archivo.read()
    palabras = contenido.split()
    print(f"El archivo contiene {len(palabras)} palabras.")
    archivo.close() 




def reemplazar_palabra():
    nombre_archivo = input("Ingrese el nombre del archivo de texto: ")
    palabra_cambiar = input("Ingrese la palabra a cambiar: ")
    palabra_reemplazo = input("Ingrese la palabra de reemplazo: ")

    archivo = open(nombre_archivo, 'r')
    contenido = archivo.read()
    archivo.close()  

    contenido_modificado = contenido.replace(palabra_cambiar, palabra_reemplazo)
    archivo = open(nombre_archivo, 'w')
    archivo.write(contenido_modificado)
    archivo.close()  
    print("Las palabras han sido reemplazadas exitosamente.")



def contar_caracteres():
    nombre_archivo = input("Ingrese el nombre del archivo de texto: ")
    archivo = open(nombre_archivo, 'r')
    contenido = archivo.read()
    archivo.close()
    total_caracteres = len(contenido)
    caracteres_sin_espacios = len(contenido.replace(" ", ""))
    print(f"Total de caracteres con espacios: {total_caracteres}")
    print(f"Total de caracteres sin espacios: {caracteres_sin_espacios}")




def submenu_csv():
    print("\nProcesar archivo CSV (.csv):")
    print("a. Mostrar las 15 primeras filas")
    print("b. Calcular estadisticas")
    print("c. Graficar una columna completa")
    opcion = input("Seleccione una opción: ")

    if opcion.lower() == 'a':
        mostrar_primeras_filas()
    elif opcion.lower() == 'b':
        calcular_estadisticas()
    elif opcion.lower() == 'c':
        graficar_columna()
    else:
        print("Asegurate de ingresar una letra que este dentro de las opciones disponibles")



def mostrar_primeras_filas():
    nombre_archivo = input("Ingrese el nombre del archivo CSV: ")
    archivo = open(nombre_archivo, 'r')
    lector_csv = csv.reader(archivo)
    for i, fila in enumerate(lector_csv):
        print(fila)
        if i == 14:
            break
    archivo.close()



def calcular_estadisticas():
    nombre_archivo = input("Ingrese el nombre del archivo CSV: ")
    columna = input("Ingrese el nombre de la columna a analizar: ")
    
    archivo = open(nombre_archivo, 'r')
    lector_csv = csv.reader(archivo)
    encabezados = next(lector_csv)
    
    if columna not in encabezados:
        print("La columna ingresada no existe en el archivo.")
        archivo.close()  
        return

    indice_columna = encabezados.index(columna)
    datos = []

    for fila in lector_csv:
        try:
            dato = float(fila[indice_columna])
            datos.append(dato)
        except ValueError:
            continue

    archivo.close() 

    if datos:
        cantidad = len(datos)
        promedio = sum(datos) / cantidad
        mediana= calcular_mediana(datos)
        maximo = max(datos)
        minimo = min(datos)

        print(f"Cantidad de datos: {cantidad}")
        print(f"Promedio: {promedio}")
        print(f"Mediana: {mediana}")
        print(f"Maximo: {maximo}")
        print(f"Minimo: {minimo}")
    else:
        print("No se encontraron datos numericos en la columna.")



def calcular_mediana(datos):
    datos_ordenados = sorted(datos)  
    cantidad = len(datos)  

    if cantidad % 2 == 1:  
        
        mediana = datos_ordenados[cantidad // 2]
    else:   
        medio_1 = datos_ordenados[cantidad // 2 - 1]
        medio_2 = datos_ordenados[cantidad // 2]
        mediana = (medio_1 + medio_2) / 2
    
    return mediana



def graficar_columna():
    nombre_archivo = input("Ingrese el nombre del archivo CSV: ")
    columna = input("Ingrese el nombre de la columna a graficar: ")

    archivo = open(nombre_archivo, 'r',)
    lector_csv = csv.reader(archivo)
    encabezados = next(lector_csv)
    
    if columna not in encabezados:
        print("La columna ingresada no existe en el archivo.")
        archivo.close()  
        return

    indice_columna = encabezados.index(columna)
    datos = []

    for fila in lector_csv:
        try:
            dato = float(fila[indice_columna])
            datos.append(dato)
        except ValueError:
            continue

    archivo.close() 

    if datos:
        plt.figure(figsize=(10,5))
        plt.plot(datos, color='orange')
        plt.title(f"Grafico de la columna {columna}")
        plt.xlabel("Indices")
        plt.ylabel(columna)
        plt.show()
    else:
        print("No se encontraron datos numericos en la columna.")



main()