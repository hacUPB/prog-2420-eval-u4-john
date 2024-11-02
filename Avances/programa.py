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



main()