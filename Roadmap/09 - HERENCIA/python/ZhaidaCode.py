"""
Ejercicio 
"""

# Superclase o clase padre
class Animal:
    def __init__(self, name: str):
        self.name = name

    def sound(self):
        pass

#Subclase o clase hija
class Dog(Animal):
    def sound(self):
        print("Woff")

class Cat(Animal):
    def sound(self):
        print("Miau")

def print_sound(animal: Animal):
    animal.sound()

my_dog = Dog("Firulais")
print_sound(my_dog)
my_cat = Cat("Michi")
print_sound(my_cat)

"""
Extra
"""

class Employee:
    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name
        self.employees = []

    def add(self, employee):
        self.employees.append(employee)

    def print_employees(self):
        print(f"{self.name} has the following employees:")
        for employee in self.employees:
            print(f"- {employee.name}")

class Manager(Employee):
    def cordinate_project(self):
        print(f"{self.name} is coordinating the project.")

class ProyectManager(Manager):
    def __init__(self, id: int, name: str, project: str):
        super().__init__(id, name)
        self.project = project

    def cordinate_project(self):
        print(f"{self.name} is coordinating the project as a Project Manager.")

class Programmer(Employee):
    def __init__(self, id: int, name: str, language: str):
        super().__init__(id, name)
        self.language = language

    def code(self):
        print(f"{self.name} is coding the language {self.language}.")

my_manager = Manager(1, "Alice")
my_project_manager = ProyectManager(2, "Bob", "Project X")
my_project_manager2 = ProyectManager(3, "Esponja", "Project z")
my_programmer = Programmer(4, "Charlie", "Python")
my_programmer2 = Programmer(5, "David", "Java") 
my_programmer3 = Programmer(6, "Eve", "C++")
my_programmer4 = Programmer(7, "Frank", "JavaScript")

my_manager.add(my_project_manager)
my_manager.add(my_project_manager2)
my_project_manager.add(my_programmer)
my_project_manager.add(my_programmer2)
my_project_manager2.add(my_programmer3)
my_project_manager2.add(my_programmer4)

my_programmer.code()
my_project_manager.cordinate_project()
my_manager.cordinate_project()

my_project_manager.print_employees()
my_manager.print_employees()


