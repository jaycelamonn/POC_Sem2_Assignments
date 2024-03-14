@@ -22,9 +22,9 @@ def get_perimeter(self) -> float:
    # Youdo get_area method
    def get_area(self) -> float:
        return self._base * self

    def __str__(self) -> str:
        # Rectangle of base:3, height:4
        return "Rectangle of base:" + self.__base + ", height:" + self.__height
        pass
        #Rectangle with base:3, height:4
        return "Rectangle with base:" + str(self.__base) + ", height:" + str(self.__height)


rec1 = Rectangle (3, 4)


rec2 = Rectangle (3, 4)



# YOUDO>  create two rectangles.  print their base, height, perimeter, and area