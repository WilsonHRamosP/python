#clase con atributos y metodos

class Persona:
    #metodos
    def __init__(self,nombre,apellido,edad):  #constructor def funcion 
        self.nombre=nombre
        self.apellido=apellido
        self.edad=edad

    def saludar(self):  #metodo
        print(f"hola soy {self.nombre} {self.apellido} y tengo {self.edad} años")

    def saludar2(self):  #metodo
        print(f"Buenos dias {self.apellido} {self.nombre} tienes {self.edad} años")

    def mostrar_edad(self):  #metodo
        print(f"tengo {self.edad} años")