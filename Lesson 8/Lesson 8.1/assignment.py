import math

class RightTriangle2:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
       return (1/2 ) * self.base * self.height
    
    def hypotenuse(self):
        return math.hypot(self.height * self.base)
    
    def perimeter(self):
        return self.base + self.height + self.hypotenuse
    
class RightTriangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
       return (1/2 ) * self.base * self.height
    
    def hypotenuse(self):
        return math.hypot(self.height * self.base)
    
    def perimeter(self):
        return self.base + self.height + self.hypotenuse



tri1 = RightTriangle(3, 4)
print("The base of tri1 is", tri1.base)
print("The height of tri1 is", tri1.height)
print("The area of tri1 is", tri1.area())


tri1l= RightTriangle2(5, 10)
print("The base of tri1 is", tri1.base)
print("The height of tri1 is", tri1.height)
print("The area of tri1 is", tri1.area())
