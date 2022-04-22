class Plane:
    def __init__(self, coefficients, quantity):
        self.coefficients = coefficients
        self.quantity = quantity

    
    def getFlipped(self):
        coefficients = [-el for el in self.coefficients]
        quantity = -self.quantity
        plane = Plane(coefficients, quantity)
        return plane