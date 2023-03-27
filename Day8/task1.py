class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Salary: {self.salary}"


emp1 = Employee("John", 25, 50000)
emp2 = Employee("David", 30, 60000)
print(emp1)
print(emp2)