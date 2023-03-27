class userName:
    def __init__(self,first_name,last_name):
        self.first_name = first_name
        self.last_name= last_name
    def __int__(self):
        return f"Name: {self.first_name} {self.last_name}"
    def display(self):
        print("Name: ",self.first_name,self.last_name)
user_1 = userName("Wasif","Mehmood")
user_2 = userName("Ali","Ahmed")
user_1.display()
user_2.display()
print('{}{}'.format(user_1.first_name,user_1.last_name))
print('{}{}'.format(user_2.first_name,user_2.last_name))