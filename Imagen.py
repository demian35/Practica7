from PIL import Image
class Imagen(object):

    def contadorHorizontal(self, imagen, coorX, coory, partes, pixeles):
        list1 = []
        m = pixeles/partes
        negro = 0
        while coorX != pixeles and coorX < pixeles:
            dato_pixel = list(imagen.getpixel((coorX,coory)))
            if [0, 0, 0] == dato_pixel:
                coorX = coorX + m
                negro = negro + 1
            if [0, 0, 0] != dato_pixel:
                if negro != 0:
                    list1.append('%s' %negro)
                    negro = 0
            coorX = coorX + 1
        if negro != 0:
            list1.append('%s' %negro)
        return list1


    def contarPixelesV(self, img):
        i = img.size
        return(i[0])

    def contarPixelesH(self, img):
        i = img.size
        return(i[1])

    def contarPartesV(self, img, coorX, coory, pixeles):
        parte = 0
        while coorX <= pixeles:
            dato_pixel = list(img.getpixel((coorX, coory)))
            coorX = coorX + 1
            if [255, 0, 0] == dato_pixel:
                parte = parte + 1
                coorX = coorX + 3
        return parte

    def contarPartesH(self, img, coorX, coory, pixeles):
        parte = 0
        while coory <= pixeles:
            dato_pixel = list(img.getpixel((coorX, coory)))
            coory = coory + 1
            if [255, 0, 0] == dato_pixel:
                parte = parte + 1
                coory = coory + 3
        return parte

    def contadorVertical(self, imagen, coorX, coory, partes, pixeles):
        list1 = []
        m = pixeles/partes
        negro = 0
        while coory != pixeles and coory < pixeles:
            dato_pixel = list(imagen.getpixel((coorX,coory)))
            if [0, 0, 0] == dato_pixel:
                coory = coory + m
                negro = negro + 1
            if [0, 0, 0] != dato_pixel:
                if negro != 0:
                    list1.append('%s' %negro)
                    negro = 0
            coory = coory + 1
        if negro != 0:
            list1.append('%s' %negro)
        return list1
