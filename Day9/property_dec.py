class Employee:
    def __init__(self,first_name,last_name,age,salary):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.salary = salary
    def fullname(self):
        return f"{self.first_name} {self.last_name}"
    def email(self):
        return "{}.{}@gmail.com".format(self.first_name,self.last_name)
    
emp_1=  Employee("John","Doe",25,4500)
