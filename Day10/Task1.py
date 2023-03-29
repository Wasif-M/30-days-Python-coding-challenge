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

item1 = Item("Phone", 100, 1)
item2 = Item("Laptop", 1000, 3)
item3 = Item("Cable", 10, 5)
item4 = Item("Mouse", 50, 5)
item5 = Item("Keyboard", 75, 5)
for instances in Item.all:
    print(instances.name, instances.price, instances.quantity)

"""
item_1=Item("Dell",20000,3)
item_2=Item("HP",30000,2)
print(Item.__dict__)
print(item_1.__dict__)
print(item_1.calculate_total_price())
print(Item.pay_rate)
print(item_1.pay_rate)
print(item_2.pay_rate)
"""

