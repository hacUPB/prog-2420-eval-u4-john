import os




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
    opcion = input("Seleccione una opción: ")

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



main()