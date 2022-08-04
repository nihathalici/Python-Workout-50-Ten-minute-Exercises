
class Person():
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f'Hello, {self.name}'

class Employee(Person):
    def __init__(self, name, id_number):
        super().__init__(name)
        self.id_number = id_number

e = Employee('empname', 1)

print(e.greet())
