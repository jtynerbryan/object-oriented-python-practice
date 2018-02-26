import random

class Die:
    def __init__(self, sides=2, value=0):
        if not isinstance(sides, int):
            raise ValueError("Sides must be a whole number (type: int)")
        if not sides >= 2:
            raise ValueError("A Die must have at least 2 sides")
        if not isinstance(value, int):
            raise TypeError("Value must be whole number greater than 0")
        self.value = value or random.randint(1, sides)

class D6(Die):
    def __init__(self, value=0):
        super().__init__(sides=6, value=value)
