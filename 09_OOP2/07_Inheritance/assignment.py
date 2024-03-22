class Rectangle:
    def __init__(self, base: float, height: float) -> None:
        if (base < 0):
            self.__base = 0
        else:
            self.__base = base

        if (height < 0):
            self.__height = 0
        else:
            self.__height = height

    def get_height(self) -> float:
        return self.__height

    # YOUDO the get_base method
    def get_base(self) -> float:
        return self._base

    def get_perimeter(self) -> float:
        return 2 * self.__base + 2 * self.__height


    # Youdo get_area method
    def get_area(self) -> float:
        return self.__base * self.__height
    
    def __str__(self) -> str:
        #Rectangle with base:3, height:4
        return "Rectangle with base:" + str(self.__base) + ", height:" + str(self.__height)

rect1 = Rectangle (3, 4)
print(rect1)
print("The area of Rectangle1 is", rect1.get_area())

rect2 = Rectangle (3, 4)
print(rect2)
print("The area of Rectangle2 is", rect2.get_area())
    


# YOUDO>  create two rectangles.  print their base, height, perimeter, and area
# using only the methods not the fields/property/attributes
