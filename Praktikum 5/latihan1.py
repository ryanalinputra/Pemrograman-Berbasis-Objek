class Person():
    def __init__(self, name, dateOfBirth, parents, children):
        self.name = name
        self.dateOfBirth = dateOfBirth
        self.parents = parents
        self.children = children

class Student(Person):
    def __init__(self, studentID, name, dateOfBirth, parents, children):
        super().__init__(name, dateOfBirth, parents, children)
        self.studentID = studentID

class Employee(Person):
    def __init__(self, employeeID, name, dateOfBirth, parents, children):
        Person().__init__(self, name, dateOfBirth, parents, children)
        self.employeeID = employeeID

