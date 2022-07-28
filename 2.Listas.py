#LISTAS
#Pueden crear listas con varios tipos de datos
lista=['a',2,True, 5.4]

#Recomendación, crear listas de un mismo tipo.
#            0     1      2     3
lenguajes=['JS','PYTHON','C#','C++']
#          -4     -3      -2   -1 

#Obtener el primer elemento
print(lenguajes[0])
#Obtener el ultimpo elemento
print(lenguajes[-1])
#Cambiar valor elementos
lenguajes[3]='JAVA'

#SUBLISTAS o SLICES
    #[Start:End:Skip]
print(lenguajes[0:3]) # o lenguajes[:3]
print('inverso:',lenguajes[::-1])

#MÉTODOS LISTAS
lenguajes.append('PHP') #Agrega un nuevo elemento al final
#len(lista) #Número de elementos de la lista
#lenguajes.clear() #Elimina todos los elementos
lenguajes.pop()#Elimina el utlimo elemnto
lenguajes.insert(1,'valor')#insert(posicion, valor)
lenguajes.extend(['CSS','HTML']) #Agregar listas
lenguajes.remove('CSS') #Remueve el elemento ingresado
del(lenguajes[0]) #Elimina el elemento de posicion 0
lenguajes.sort() #Ordena la lista
lenguajes.sort(reverse=True) #Ordena  a la inversa la lista
#min(lista) minimo  max(lista)
#Buscar en una LISTA
b='valor' in lenguajes #Busca valor en lista retorna bool
i=lenguajes.index('valor') #Retorna el índice si lo encuentra

print(lenguajes)

#MATRICES
f1=[1,2,3]
f2=[3,4,5]
m=[[10,20,30],[1,2,3]]
m1=[f1,f2]
print(m,m1)
print(m[0][2])

#List comprehensions
cuadrados= [print(i**2) for i in range(1,20) if i%3!=0]
#Crear, con un list comprehension, una lista de todos los
#múltiplos de 4 que a la vez también son múltiplos de 6 y de 9,
#hasta 5 digitos.
multiplos=[i for i in range(1,100) if i%36==0]
print(multiplos)