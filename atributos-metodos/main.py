#clase principal
from persona import Persona #importamos la clase persona

def main(): #funcion principal
    persona1=Persona("Wilson","Ramos",32) #creamos un objeto de la clase persona
    persona1.saludar() #llamamos al metodo saludar
    persona1.saludar2() #llamamos al metodo saludar2
if __name__ == "__main__": #funcion principal para ejecutar desde aqui el programa
    main()
