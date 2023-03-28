class Employee:
    rasing_amount = 5.4
    def __init__(self,first_name,last_name,age,salary):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.salary = salary
    def fullname(self):
        return f"{self.first_name} {self.last_name}"
    def __str__(self):
        return f"Name: {self.first_name} {self.last_name}, Age: {self.age}, Salary: {self.salary}"
    def __repr__(self):
        return f"Employee({self.first_name},{self.last_name},{self.age},{self.salary})"
    def __add__(self,other):
        return self.salary+other.salary
    def __len__(self):
        return len(self.fullname())


emp_1=  Employee("John","Doe",25,4500)
emp_2=  Employee("Jane","Doe",25,4500)
print(len(emp_1))

#print(emp_1+emp_2)
#print(emp_1.__repr__())
#print(emp_1.__str__())