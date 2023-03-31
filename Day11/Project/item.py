import csv
class Item():
    pay_rate = 0.8
    all =[]
    def __init__(self, name: str, price: int, quantity: int):
        assert price >= 0, "Price cannot be negative!"  
        assert quantity >= 0, "Quantity cannot be negative!"
        self.__name = name
        self.__price = price
        self.quantity = quantity
        Item.all.append(self)
    @property #For Encapsulation and Data Hiding Getters
    def name(self):
        return self.__name
    @name.setter #For setting the value of the private attribute
    def name(self, new_name):
        if len(new_name) < 10:
            raise ValueError("Your Name is too long characters!")
        else:
            self.__name = new_name
    @property 
    def price(self):
        return self.__price
    def apply_discount(self):
        self.__price = self.__price * Item.pay_rate
    def apply_increase(self,increment):
        self.__price = self.__price * increment
    @price.setter
    def price(self, new_price):
        if new_price >= 0:
            self.__price = new_price
        else:
            raise ValueError("Price cannot be negative!")
    def calculate_total_price(self):
        return self.__price * self.quantity
    def apply_discount(self):
        self.__price = self.__price * Item.pay_rate
    @classmethod #decorator
    def instantiate_from_csv(cls):
        with open("item.csv",'r') as file:
            reader = csv.DictReader(file)
            items = list(reader)
        for item in items:
            Item(
                name=item.get("name"),
                price=float(item.get("price")),
                quantity=float(item.get("quantity")),
            )
    def __repr__(self):
        return f"{self.name} costs {self.price} and we have {self.quantity} in stock."
    @staticmethod #decorator
    def is_integer(num):
        if isinstance(num, int):
            return True
        else:
            return False
