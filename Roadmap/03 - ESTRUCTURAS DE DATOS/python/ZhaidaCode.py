#Listas: donde guardo elementos ordenadamente y puedo modificar
my_list = ["Braiz", "kuroz", "Zhaida", "Santi"]
print(my_list)  

#Añadir un nuevo dato
my_list.append("keiko")
print(my_list)

#Eliminar un dato
my_list.remove("kuroz")
print(my_list)

#Actualizar un dato
my_list[3] = "Urpi"
print(my_list)

#Ordenar datos
my_list.sort()
print(my_list)

print("--------------------------------")

#Tuplas: estructura donde guardamos mas de un dato, 
# pero no se puede modificar

my_tuple = ("Zhaida", "Cazasola", "zhaida@gmail.com", 25)
print(my_tuple)

print("--------------------------------")

#Sets: estructura donde guardamos mas de un dato, desordenadamente
# y no se puede repetir

my_set = {"Zhaida", "Cazasola"}
print(my_set)

#Añadir datos
my_set.add("MoureDev")
print(my_set)

#Eliminar datos
my_set.remove("Cazasola")
print(my_set)

#Actualizar datos: no se puede, solo eliminar y volver añadir
#Ordenar datos: no se puede, solo convertir a lista y ordenar

print("--------------------------------")

#Diccionario: estructuras donde guardamos datos en pares 
# de clave-valor, desordenadamente y se puede modificar

my_dict = {
    "name": "Zhaida",
    "last_name": "Cazasola",
    "email": "zhaida@gmail.com",
    "age": 25
}

print(my_dict)

#Añadir un datos
my_dict["country"] = "Peru"
print(my_dict)

#Acceder a un dato
print(my_dict["age"])

#Actualizacion
my_dict["name"] = "Vander"
print(my_dict)

"""
Extra dificultad
"""

# Lista donde se guardarán todos los contactos
contactos = []


def agregar_contacto(nombre, numero):
    # Comprobar si el contacto ya existe
    for contacto in contactos:
        if contacto["nombre"].lower() == nombre.lower():
            print("Ese contacto ya existe")
            return

    # Validar el número
    if not numero.isdigit():
        print("El teléfono solo puede contener números")
        return

    if len(numero) > 11:
        print("El teléfono no puede tener más de 11 dígitos")
        return

    # Crear el nuevo contacto
    nuevo_contacto = {
        "nombre": nombre,
        "numero": numero
    }

    # Guardarlo en la lista
    contactos.append(nuevo_contacto)

    print("Contacto agregado correctamente")


def buscar_contacto(nombre):
    for contacto in contactos:
        if contacto["nombre"].lower() == nombre.lower():
            print("Nombre:", contacto["nombre"])
            print("Número:", contacto["numero"])
            return

    print("Contacto no encontrado")


def actualizar_contacto(nombre, nuevo_numero):
    # Validar el nuevo número
    if not nuevo_numero.isdigit():
        print("El teléfono solo puede contener números")
        return

    if len(nuevo_numero) > 11:
        print("El teléfono no puede tener más de 11 dígitos")
        return

    # Buscar el contacto
    for contacto in contactos:
        if contacto["nombre"].lower() == nombre.lower():
            contacto["numero"] = nuevo_numero
            print("Contacto actualizado correctamente")
            return

    print("Contacto no encontrado")


def eliminar_contacto(nombre):
    for contacto in contactos:
        if contacto["nombre"].lower() == nombre.lower():
            contactos.remove(contacto)
            print("Contacto eliminado correctamente")
            return

    print("Contacto no encontrado")


# Variable que controla el ciclo
opcion = ""


# El menú se repite mientras la opción no sea 5
while opcion != "5":
    print("\n--- AGENDA DE CONTACTOS ---")
    print("1. Buscar contacto")
    print("2. Agregar contacto")
    print("3. Actualizar contacto")
    print("4. Eliminar contacto")
    print("5. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        nombre = input("Nombre del contacto: ")
        buscar_contacto(nombre)

    elif opcion == "2":
        nombre = input("Nombre: ")
        numero = input("Número: ")
        agregar_contacto(nombre, numero)

    elif opcion == "3":
        nombre = input("Nombre del contacto: ")
        nuevo_numero = input("Nuevo número: ")
        actualizar_contacto(nombre, nuevo_numero)

    elif opcion == "4":
        nombre = input("Nombre del contacto: ")
        eliminar_contacto(nombre)

    elif opcion == "5":
        print("Programa finalizado")

    else:
        print("Opción no válida")