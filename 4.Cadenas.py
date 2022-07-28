palabras=['Uno','Dos','Tres','Cuatro']

tuplas=('Abeja','ratón', 'burro')
#Unir valores de una lista o Tupla, retorna cadena de texto
print("-".join(palabras))
print("/".join(tuplas))

# De Cadena de texto a Lista
cadena="Esta es una cadena de texto"
print(cadena.split(' '))

#Unir cadenas +
imprimir='Mi nombre es %s y mi apellido es %s '%('Cristian','Paguay')
print(imprimir)

##PLACE HOLDERS
print("Una  {}  de color {}".format("Pelota", "Red"))
n='Juan'
otra=f'Es otra forma de {n} y repito su {n}'
print(otra)

#Especificar la separacion en la impresión
print('Texto','en','formato',sep='|')

#Funciones de Cadena
print("otorringolaringolo".count('o')) #cuenta el texto de una cadena
print("otorringolaringolo" in ('rin')) #Busca cadena, retorna un bool
print("otorringolaringolo" not in ('rin')) #Busca cadena, retorna un bool, negar el resultado
print("HOla".lower()) #Minusculas
print("upper".upper()) #Minusculas
print(otra.lower().startswith('es')) # Devuelve un Bool, si encuentra al inicio de la cadena
print(otra.lower().endswith('su')) # Devuelve un Bool, si encuentra al inicio de la cadena

#Alinear Cadena rjust(20) ->Alinea a la derecha ljust(14) -> Alinear a la izquierda, center(#)-> centrar
msn='!Hola mundo!'.center(20)
print (msn)

