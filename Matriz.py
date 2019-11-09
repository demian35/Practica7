class Matriz(object):

	def createList(self,n):
		listamatriz=[]
		for i in range(n):
			listamatriz.append(random.randint(0,100))
		return listamatriz	

	def Matriz(self, m,l ):
		matriz= []
		for i in range(m):
			matriz.append(createList(l))
		for i in range(m):
			fila= ""
			for j in range(l):
				espacios= ' '*(5-len(str(matriz[i][j])))
				fila= fila+espacios+str(matriz[i][j])
			print(fila)
		return matriz		

	def busca(self, coorAltura, coorLargo):
		pass 

    #def __init__(self, arg):
