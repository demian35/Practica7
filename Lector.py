class Lector(object):
    """docstring for ."""

    def contarLineas(self, Archivo):
        indice = 0
        contador = 0
        listaLineas = []
        while indice != len(Archivo) - 1:
            if Archivo[indice] == '[':
                while Archivo[indice] != ']':
                    if Archivo[indice] == ')':
                        contador = contador + 1
                    indice = indice + 1
                listaLineas.append(contador)
                contador = 0
                indice = indice + 1
            else:
                indice = indice + 1

        return listaLineas

    def contadornumeros(self, Archivo, lineas):
        indice = 0
        contador = 0
        suma = 0
        intColum = 0
        lista = []
        while indice != len(Archivo) - 1:
            if Archivo[indice] == '[':
                while Archivo[indice] != ']':
                    while Archivo[indice] != ')':
                        if Archivo[indice].isdigit():
                            suma = suma + int(Archivo[indice])
                            contador = contador + 1
                            indice = indice + 1
                        else:
                            indice = indice + 1
                    contador = contador - 1
                    suma = suma + contador
                    if suma > lineas[intColum]:
                        return "Solucion no encontrada"
                    else:
                        lista.append(suma)
                        contador = 0
                        suma = 0
                        indice = indice + 1
                intColum = intColum + 1
            else:
                indice = indice + 1
        ##return "Tiene Solucion"
        ## lista

    def agregarEnMatriz(self, matriz):
        pass
