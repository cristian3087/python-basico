#Funciones en python

from ast import arg


def nombre_funcion():
    pass

def suma(a,b=4):
    return (a+b),'suma:'
    
#Python puede retornar maximo 3 Valores

r,s=suma(5,b=6)
print(s,r)

#Funcion con argumentos, varios argumentos -> *
def promedio(*listado): # convencion *args  TUPLAS
    return sum(listado)/len(listado)

print(promedio(4,6,8))

def combinacion(p1,p2,*args):
    print(p1,p2,args)

combinacion(1,2,3,4,5,6,7,8)

def usuarios(x,y,pi=3.14,*args, **kwargs): #Diccionarios
    print(x,args)
    print(y, kwargs)
    print(pi)

usuarios(1,'z',2,3,cody=True,a=5,b=10)

#Scope de una variable: Es el ambito de la variable.
#global para declarar una variable global.
#Funciones Annidadas: Funcion dentro de otra función
def mi_funcion(a):
    def mul():
        return a*1
    return a
#Funciones de primera clase, funciones de primer orden, ciudadanos de primer orden
#Se puede asignar a una variable una función, o utilizar una funcion como parametros.
f=mi_funcion

#Funciones LAMBDA, funciones anonimas
flambda=lambda a,b:a+b
print(flambda(5,7))

#palindromo

palindromo=lambda palabra:palabra==palabra[::-1]

#Funciones anonimas con varios parametros tipo tupla y diccionario
varios=lambda *args,**kwargs:print(args,kwargs)
varios(1,2,3,4,7,nombre='Cristian',edad=35)
promedio=lambda *args:float(sum(args)/len(args))
promedio(9,8,7,6,9,10)

#SCOPE .- Alcance de una variable
def pasa(fpromedio,*args):
    p=fpromedio(*args)
    if(int(p)>=7):
        print(f'Pasa con {p}')
    else:
        print(f'No pasa con {p}')

pasa(promedio,7,8,8,7,6,5)

#Closures : funcion anidada que recuerda una variable de un scope superior.
# con la palabra -> nonlocal 
def saludar():
    def msn():
        print('Hola mundo')
    return msn

msn=saludar()
msn()