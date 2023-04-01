class Flower:
    flowers = []

    def __init__(self, name, color, petals):
        self._name = name
        self._color = color
        self._petals = petals
        self.flowers.append(self)

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def bloom(self):
        print(f"The {self._name} flower with {self._color} color has {self._petals} petals and is in bloom.")

    @classmethod
    def total_flowers(cls):
        return len(cls.flowers)

class Rose(Flower):
    def __init__(self, name, color, petals):
        super().__init__(name, color, petals)

    def fragrance(self):
        print(f"The {self._name} rose has a fragrant smell.")

class Sunflower(Flower):
    def __init__(self, name, color, petals):
        super().__init__(name, color, petals)

    def follow_sun(self):
        print(f"The {self._name} sunflower follows the sun.")

rose = Rose("Rose", "Red", 6)
sunflower = Sunflower("Sunflower", "Yellow", 32)

rose.bloom() 
sunflower.bloom()

print(f"Total flowers: {Flower.total_flowers()}")

rose.set_name("BABY FACE")
print(rose.get_name()) 
