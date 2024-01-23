number1 = int(input("Enter a number: "))
number2 = int(input("Enter a number: "))

try:
   value = number1 / number2
   print('The division of',number1, "and", number2, "is",  number1 / number2)
except ZeroDivisionError:
    print("Cannot divide by zero")
except:
    print("Something strange happenend")