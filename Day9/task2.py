class Employee:
    rasing_amount = 5.4
    def __init__(self,first_name,last_name,age,salary):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.salary = salary
    def __str__(self):
        return f"Name: {self.first_name} {self.last_name}, Age: {self.age}, Salary: {self.salary}"
    def give_raise(self):
        self.salary = self.salary*self.rasing_amount #Class variable can be accessed by instance as well as class
        return self.salary
class Developer(Employee):
    rasing_amount=1.10
    def __init__(self,first_name,last_name,age,salary,prog_lang): # constructor of child class
        super().__init__(first_name,last_name,age,salary) # super() is used to call the parent class constructor for handling the common attributes
        self.prog_lang = prog_lang
class Manager(Employee):
    def __init__(self,first_name,last_name,age,salary,employees=None):
        super().__init__(first_name,last_name,age,salary)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees
    def add_emp(self,emp):
        if emp not in self.employees:
            self.employees.append(emp)
    def remove_emp(self,emp):
        if emp in self.employees:
            self.employees.remove(emp)
    def print_emp(self):
        for emp in self.employees:
            print("-->",emp)

dev_1=Developer("John","Doe",25,4500,"Python")
mge=Manager("John","Doe",25,4500,[dev_1])
print(mge)
mge.add_emp(dev_1)
mge.print_emp()
print(dev_1.first_name)
print(dev_1.prog_lang)
print(isinstance(mge,Manager))
print(isinstance(mge,Employee))
print(issubclass(Developer,Employee))
print(issubclass(Developer,Manager))