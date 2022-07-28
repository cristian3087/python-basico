#Declarar variables vacios
valor=None #Ausencia de valor

#Condiciones
condicion=True
if(condicion):
    print('VErdadero')
elif(condicion>1):
    print('ElseIF')
else:
    print('Else')

#If Ternario
valor='Azul' if condicion==False else 'Rojo'
# Resultado valorAfirmativo condicion Valor Negativo
#Operadores logicos or,and,not 

#Bucles Repetitivos
i=0
while(i<10):
    print('w:',i)
    i+=1
else:
    print('Fin de ciclo While')
#For, para cualquier tipo iterable, lista, tupla, diccionario, cadena
for i in range(0,10):
    print('f:',i)  

#range(11) <--> range(0,11), va desde 0 a < 11, range(valorInicial,valorFinal, Step)
num=[2,4,5,6,9]
#funcion enumerate(lista, tupla, o diccionario)
for indice,numero in enumerate(num):
    print(indice,numero)

#Romper o cuntinuar los bucles, brake o continue
for caracter in "Este es un texto":
    if(caracter=='e'):
        #break
        continue
    print(caracter)

