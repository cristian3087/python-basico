# Diccionario {} dic()
diccionario={
    'nombre':'Cristian',
    'edad':35,
    'estado_civil':'soltero'
    }
diccionario['llave']='valor'
diccionario[(1,2)]="La llave es una tupla"

#Longitud de una llave
print('Longitud:',len(diccionario))
print(diccionario)

#Obtener valores de un diccionario
print(diccionario['llave'])
print(diccionario.get('llav','La llave no existe'))
print(diccionario.setdefault('llave','No hay valor'))

#Busca llaves en un diccionario
print('llave' in diccionario)


#Imprime llaves
print(diccionario.keys())
#Imprime Valores
print(diccionario.values())
#Imprime ITEMS
print(diccionario.items())#retorna tuplas ('llave', 'valor')

#Elimanar valores de una lista
del (diccionario['llave'])
diccionario.pop('edad') #Elimina la llave y su valor
print(diccionario)

#Eliminar todos los elementos de un diccionario
diccionario.clear()

#Dictionary comprehensions
my_dic={i:i**3 for i in range(1,60) if i%3==0}
print(my_dic)

# Sumar diccionarios con el simbolo | con python 3.9
