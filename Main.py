import os
from PIL import Image
def main():
    print ("1. Resolver un Nonograma.")
    print ("2. Verificar una solucion.")
    print ("3.Salir")
    opcion = int(input("Elige tu opcion\n"))
    os.system('clear')
    while opcion > -1 and opcion < 4:
        ##nombre = input('Escribe el nombre del archivo con su extencion .---\n')
        img = Image.open('ejemploA.png')
        if opcion == 1:
            print("Elegiste opcion 1")
            main()
        elif opcion == 2:
            print("Eliegiste opcion 2")
            main()
        elif opcion == 3:
            print("adios")
            return
        else:
            os.system('clear')
            print("Opcion Incorrecta, intente de nuevo")
            main()

if __name__ == "__main__":
    main()
