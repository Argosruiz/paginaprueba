import json

fname = input('Escriba el nombre del archivo : ')
class calcular:
    def contar(self,fname):
        try:
            obj_file = open(fname)
        except :
            print('El archivo no exite vuelva a intentarlo')
            return()

        nombre = dict()
        contador = {}

        for linea in obj_file:
            palabras = linea.split() # separa lineas por palabras, por espacios en blanco
            for palabra in palabras:
                palabra = palabra.lower().strip(".,") # cambia a minuscula y quita puntuacion
                if palabra not in contador:
                    contador[palabra] = 1
                else:
                    contador[palabra] += 1
        print('Total de palabras distintas: ', len(contador))
        print('palabras: ', contador)
    # contar(fname)

        for word in sorted(contador,key = contador.get, reverse = True)[:10]:
             print('\t',word,':', contador[word],'veces')

cuanto = calcular()
cuanto.contar(fname)          
    
