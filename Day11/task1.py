import csv
class Item():
    pay_rate = 0.8
    all =[]
    def __init__(self, name: str, price: int, quantity: int):
        assert price >= 0, "Price cannot be negative!"  
        assert quantity >= 0, "Quantity cannot be negative!"
        self.name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)
    def calculate_total_price(self):
        return self.price * self.quantity
    def apply_discount(self):
        self.price = self.price * Item.pay_rate
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
        return f"{self.__class__,__name__}{self.name} costs {self.price} and we have {self.quantity} in stock."
    @staticmethod #decorator
    def is_integer(num):
        if isinstance(num, int):
            return True
        else:
            return False
class Phone(Item):
    def __init__(self,name: str, price: int, quantity: int,broken_Phones=0):
        super().__init__(name, price, quantity)
        assert broken_Phones >= 0, "Broken phones cannot be negative!"
        self.broken_Phones = broken_Phones


phone_1 = Phone("LG", 340, 3, 2)
phone_2 = Phone("Panasonic", 400, 2, 2)
print(Item.all)
print(Phone.all)