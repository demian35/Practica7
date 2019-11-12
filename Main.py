import os
from PIL import Image
from Imagen import Imagen
from Lector import Lector
def main():
    print ("1. Resolver un Nonograma.")
    print ("2. Verificar una solucion.")
    print ("3.Salir")
    try:
        opcion = int(input("Elige tu opcion\n"))
        os.system('clear')
        while opcion > -1 and opcion < 4:

            contar = Imagen()
            lector = Lector()

            if opcion == 1:

                print("Elegiste opcion 1")
                texto = input("Nombre del archivo txt\n")
                txt = open('%s.txt' %texto , 'r+')
                t = txt.read()
                lin = lector.contarLineas(t)
                lin1 = lector.contadornumeros(t,lin)
                print('%s' %lin)
                print('%s' %lin1)
                main()


            elif opcion == 2:

                print("Eliegiste opcion 2")
                Imagenes = input("Nombre de la imagen\n")
                img = Image.open('./Archivos/%s.png' %Imagenes)
                texto = input("Nombre del txt\n")
                txt = open('./Archivos/%s.txt' %texto ,'r+')
                t = txt.read()

                coory = 1
                coorX = 1
                list1 = []
                list2 = []

                v = contar.contarPixelesV(img)
                p = contar.contarPartesV(img, coorX, coory, v)
                r = v/p
                while coory != v and coory < v:
                    m = contar.contadorHorizontal(img,coorX,coory,p, v)
                    coory = coory + r
                    list1.append(m)

                coory = 1
                h = contar.contarPixelesH(img)
                p1 = contar.contarPartesH(img, coorX, coory, h)
                r = h/p1

                while coorX != h and coorX < h:
                    n = contar.contadorVertical(img,coorX,coory,p1, h)
                    coorX = coorX + r
                    list2.append(n)


                list3 = []
                list4 = []
                list5 = []
                numero = ""
                itxt = 0

                while itxt != len(t) - 1:

                    if t[itxt] == '[':

                        while t[itxt] != ']':

                            while t[itxt] != ')':

                                if t[itxt].isdigit():
                                    list5.append(t[itxt])
                                    itxt = itxt + 1

                                else:

                                    itxt = itxt + 1

                                list3.append(list5)
                                list5 = []
                                itxt = itxt + 1

                        if len(list4) == 0:
                            list4 = list3
                            list3 = []

                    itxt = itxt + 1

                if list4 == list1 and list3 == list2:
                    print('\tEl Nonograma es valido\n')
                    print('Quieres continuar S o N \n')
                    resp = input(' ')
                    if resp == 'S':
                        main()
                    if resp == 'N':
                        return
                    else:
                        print('Respuesta Incorrecta')

                else:
                    print('\tEl Nonograma es invalido\n')
                    print('Quieres continuar S o N \n')
                    resp = input(' ')

                    if resp == 'S':
                        main()
                    if resp == 'N':
                        return
                    else:
                        print('Respuesta Incorrecta')

            elif opcion == 3:
                print("adios")
                return
            else:
                print("Opcion Incorrecta, intente de nuevo")
                main()
    except ValueError as err:
            print('Respuesta Incorrecta')
            main()
    except FileNotFoundError as err:
            print('Archivo no encontrado')
            main()

if __name__ == "__main__":
    main()
