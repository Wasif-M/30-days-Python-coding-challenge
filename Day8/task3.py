class Employee:
    rasing_amount = 5.4
    def __init__(self,first_name,last_name,age,salary):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.salary = salary
    def __str__(self):
        return f"Name: {self.first_name} {self.last_name}, Age: {self.age}, Salary: {self.salary}"
    def display(self):
        print("Name: ",self.first_name,self.last_name)
        print("Age: ",self.age)
        print("Salary: ",self.salary)
    def give_raise(self):
        self.salary = self.salary*Employee.rasing_amount #Class variable can be accessed by instance as well as class
        return self.salary
    
Employee.rasing_amount=12.5 
emp1 = Employee("John", "Doe", 25,4500)
emp1.display()
print(emp1.rasing_amount)