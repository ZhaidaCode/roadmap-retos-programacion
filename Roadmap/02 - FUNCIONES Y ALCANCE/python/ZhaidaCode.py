# EJERCICIO:
 #Crea ejemplos de funciones básicas que representen las diferentes
 #posibilidades del lenguaje:
 #Sin parámetros ni retorno, con uno o varios parámetros, con retorno...
 # Comprueba si puedes crear funciones dentro de funciones.
 # Utiliza algún ejemplo de funciones ya creadas en el lenguaje.
 # Pon a prueba el concepto de variable LOCAL y GLOBAL.
 # Debes hacer print por consola del resultado de todos los ejemplos.
#(y  tener en cuenta que cada lenguaje puede poseer más o menos posibilidades)

def saludar():
    nombre = "Zhaida"
    print("Hola, " + nombre)

saludar()

def areaTriangulo():
    ALTURA = 8
    BASE = 2
   
    area = (BASE * ALTURA)/2
    print("El area del triángulo es: " + str(area))

areaTriangulo()

""" 
Funciones definidas por el usuario
"""

#Función simple
def greet():
    print("Hola, Python")

greet()

def return_greet():
    return("Hola, Python")

print(return_greet())

#Función con un argumento
def arg_greet(name):
    print(f"Hola, {name}")

arg_greet("Zhaida")

def args_greet(greet, name):
    print(f"{greet}, {name}")

args_greet("Hello","Zhaida")

def default_arg_greet(name="Xovi"):
    print(f"Hola, {name}")

default_arg_greet("Misky")
default_arg_greet()

def varios_args_greets(*names):
    for name in names:
        print(f"Hi, {name}")

varios_args_greets("Zhaida", "Misky", "Xovi", "Vanchi", "Rosa")

"""
Funciones dentro de funciones
 """

def antes_de_saludo():
    def saludo():
        print("Holaaaaaa")
    saludo()

antes_de_saludo()

"""
Funciones del lenguaje
"""

print(len("Zoe"))
print(type("Zhaida"))
print("zka".upper())

"""
Extra
"""

def numeros_puros(str1,str2):
    contador = 0
    i = 0
    for i in range(1,101,1):
        if i % 3 == 0 and i % 5 == 0:
            print(f"{str1} {str2} {i}")
        elif i % 3 ==0:
            print(f"{str1} {i}")    
        elif i % 5 ==0:
            print(f"{str2} {i}")
        else: contador = contador + 1
    
    print(f"Los numeros que no son multiplos de 3 ni de 5 son: {contador}") 

    return contador


numeros_puros("xovi", "misky")

