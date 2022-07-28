#TUPLAS SON INMUTABLES (), más rapidas para utilizar como objetos de lectura
mi_tupla=(1,2,3)
tupla=('valor',1,2,3,['a',2,3])
curso=('Python','C#','Js','Html')

#MOSTRAR VALORES DE TUPLAS
print(mi_tupla[0]) # Retorna el primer valor

#SUB-TUPLAS Slice
mi_tupla[:1] # Retorna dos valores [Star:End:Step]

#CONVERTIR
t=tuple([1,2,3,4])
l=list(t)
print(type(t),type(l))
