#POO
"""
Abstraccion: Definir atributos, propiedades y metodos, clases abstractas
Encapsulamiento: getters-> @property , setter -> @variable.setter, private __, protected _
Herencia: (ClaseA,ClaseB,etc)  super()-> Método permite acceder a metodos y propiedades del padre
Polimorfismo: si pasa la prueba de es un. Los metodos se adaptan a cualquier objeto.
"""
from abc import ABC, abstractmethod


class User:
    #Atributos privados.
    __name='Cristian'  # __   nos dice que es privado.
    
    #Contexto: La referencia del objeto self
    #Metodo constructor, no debe ser complicado debe ser simple
    def __init__(self,name='SN') -> None:
        self.__name=name

    #crear metodos con def
    def hi(self):
        print(f'Hola mi nombre es: {self.name}')


#Herencia: hereda propiedades y metodos a su hijo.
class Student(User):
    #Modificadores de acceso, para proteger un metodo o un atributo _
    #protected _  , Private  __
    __score=10

    def __init__(self, name='SN') -> None:
        super().__init__(name)
    #super:accede a metodos o propiedades de su padre
    #Metodos getters setters
    @property
    def score(self):
        return self.__score 

    @score.setter
    def score(self, n):
        #validar valor
        n=int(n)
        if(n<0):
            raise ValueError("El valor debe ser mayor a 0")
        self.__score=n
    
st=Student('Cristian')
st.score='x'
print('Score: ',st.score)


#Instanciar objetos:
usuario=User()
#print(usuario)

#Importar
from abc import ABC, abstractmethod

##Clases Abstractas
class ClaseAbstracta(ABC):
    @abstractmethod
    def obtener():
        pass
    @abstractmethod
    def agregar():
        pass
