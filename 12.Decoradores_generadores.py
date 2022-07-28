#Extender funcionalidades a una funcion

def funA(funB):
    def funC():
        funB()
    return funC

@funA
def saludar():
    print('Hola')

saludar()    


def decorador(funX):
    def funE(*args):
        print('****Antes de la F****')
        r=funX(*args)
        print('****Despues de F****')
        return(r)
    return funE

@decorador
def suma(a,b):
    s=str(a+b).center(20)
    print(s)

suma(6,8)

#Generadores, YIELD, suspende la ejecución bajo demanda por el uso de memoria.
#Distribucion perezosa
def generar_pares():
    for i in range(0,10,2):
        yield i
        print('se reanuda...')

for i in generar_pares():
    print(i)
print('****** Imprimir bajo demanda ******')
generador=generar_pares()
print(next(generador))
print(next(generador))
print(next(generador))