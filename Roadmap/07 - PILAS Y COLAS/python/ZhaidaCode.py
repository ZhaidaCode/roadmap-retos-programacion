"""
Ejercicio 7: PILAS Y COLAS
"""

# Pila/Stacks (LIFO - Last In, First Out)

stack = []

# push
stack.append(1)
stack.append(2)
stack.append(3)
print(stack)

# pop
print(stack.pop())
print("---------")

# Cola/Queue (FIFO - First In, First Out)

queue = []

#enqueue
queue.append(1)
queue.append(2)
queue.append(3)
print(queue)

#dequeue
print(queue.pop(0))


"""
Extra
"""

def web_navigation():
    stack =[]

    while True:

        action = input("Añade una URL ó interactúa con palabras adelante/atrás/salir: ")

        if action == "salir":
            print("Saliendo del navegador...")
            break
        elif action == "adelante":
            pass
        elif action == "atrás":
            stack.pop()
            pass
        else:
            stack.append(action)

        if len(stack) > 0:
            print(f"Has navegado a: {stack[len(stack) - 1]}" )
        else:
            print("Ahora estás en la página de inicio")

#web_navigation()

#Colas
def shared_printer():
    queue = []

    while True:
        action = input("Añade un documento a imprimir ó interactúa con palabras imprimir/salir: ")

        if action == "salir":
            print("Saliendo de la cola de impresión...")
            break
        elif action == "imprimir":
            if len(queue) > 0:
                print(f"Imprimiendo: {queue.pop(0)}")
            else:
                print("No hay documentos en la cola de impresión.")
        else:
            queue.append(action)
            print(f"Documento ${action} añadido a la cola de impresión.")
            
shared_printer()