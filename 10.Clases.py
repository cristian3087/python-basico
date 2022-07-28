#Clases, deben ir con Camelcase y en singular
class CamelCase:
    pass

# Atributos de Clase

class Usuario: 
    username='Cristian'
    email='cristian@gmail.com'
    edad=0

Usuario.username='Otro Nombre'

print(Usuario.username)

#Atributos de instancia(Objeto)
user=Usuario() #crear un objeto Usuario()
#Proceso de python con los atributos.
"""
1.Verifica si el atributo existe dentro del objeto
2.Verifica si el atributo existe dentro de la clase (Para lectura)
3.Muestra error que no existe el atributo
"""
#__dict___ : Al macena los atributos que tiene el objeto  
user.name='Cristian'  #creando nuevo atributo al objeto
user.nuevoAtributo='Nuevo' #creando un nuevo atributo al objeto
print(user.__dict__)
print(user.name)

#Constructores
class User:
    def __init__ (self,name='',edad=0): #Metodo constructor para iniciar atributos
        self.name=name
        self.edad=edad
    #Metodos
    def saludar(self):
        print(f'Hola {self.name}')


user1=User('Cristian',35)
user1.saludar()
print(user1.__dict__)

#Heredar (ClaseA,ClaseB,etc)
class Alumno(User):
    yo='CP'
    def __init__(self, name='', edad=0,escuela='X'):
        super().__init__(name, edad)
        self.escuela=escuela
    def saludar(self):
        print(f'Hola soy el alumno {self.name}, de la escuela {self.escuela}')

    #Declarar métodos de clase, o clase estatica
    @classmethod
    def me(cls):
        print(f'Yo soy: {cls.yo}')

alu=Alumno('Juan','20')
alu.saludar()
Alumno.me()

