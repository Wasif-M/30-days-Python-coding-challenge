from item import Item
class Phone(Item):
    def __init__(self,name: str, price: int, quantity: int,broken_Phones=0):
        super().__init__(name, price, quantity)
        assert broken_Phones >= 0, "Broken phones cannot be negative!"
        self.broken_Phones = broken_Phones
