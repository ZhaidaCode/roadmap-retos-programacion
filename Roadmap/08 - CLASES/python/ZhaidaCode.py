"""
Ejercicio 8 - clases
"""

class Programer:
    def __init__(self, name: str, age: int, language: list):
        self.name = name
        self.age = age
        self.language = language

    def print(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Language: {', '.join(self.language)}")  


my_programer = Programer("Zhaida", 20, ["Python", "JavaScript", "C++"])
my_programer.print()

"""
extra
"""

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if self.count() == 0:
            return None
        return self.stack.pop()

    def count(self):
        return len(self.stack)

    def print(self):
        for item in reversed(self.stack):
            print(item)


my_stack = Stack()
my_stack.push(1)
my_stack.push(2)
my_stack.push(3)
my_stack.print()