class Employee:
    rasing_amount = 5.4
    def __init__(self,first_name,last_name,age,salary):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.salary = salary
    def __str__(self): #self is referred to instance of the class
        return f"Name: {self.first_name} {self.last_name}, Age: {self.age}, Salary: {self.salary}"
    def display(self):
        print("Name: ",self.first_name,self.last_name)
        print("Age: ",self.age)
        print("Salary: ",self.salary)
    def give_raise(self):
        self.salary = self.salary*Employee.rasing_amount #Class variable can be accessed by instance as well as class
        return self.salary
    @classmethod # class method accepts class as argument
    def set_rasing_amount(cls,amount):
        cls.rasing_amount = amount
    @classmethod
    def from_string(cls,emp_str):
        first_name,last_name,age,salary = emp_str.split("-")
        return cls(first_name,last_name,age,salary)
    @staticmethod # doesn't take any instance or class as argument
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True
"""""
emp1 = Employee.from_string("John-Doe-25-4500")
print(emp1)
"""
import datetime as dt
my_date = dt.date(2016,7,10)
print(Employee.is_workday(my_date))
'''
emp1.display()
Employee.set_rasing_amount(12.5) # change the raised amount from class method 
Employee.rasing_amount=12.5 # we can change the class variable value from out side the class
emp2 = Employee("John", "Doe", 25,4500)
emp2.display()
print(emp1.rasing_amount)
'''