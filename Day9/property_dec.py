class Employee:
    def __init__(self,first_name,last_name,age,salary):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.salary = salary
    @property
    def fullname(self):
        return f"{self.first_name} {self.last_name}"
    @property
    def email(self):
        return "{}.{}'@gmail.com".format(self.first_name,self.last_name)
    @fullname.setter
    def fullname(self,name):
        first,last = name.split(" ")
        self.first_name = first
        self.last_name = last
    @fullname.deleter
    def fullname(self):
        print("Delete Name!")
        self.first_name = None
        self.last_name = None
emp_1=  Employee("John","Doe")
emp_1.fullname = "Jane Doe"
print(emp_1.first_name)
print(emp_1.email)
print(emp_1.fullname)
del emp_1.fullname
