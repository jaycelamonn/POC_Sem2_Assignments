text = input("Enter some text: ")

result = text.find("the")

if result == -1:
    print("The word the is not in the string")
else:
    print("The word the in the string")
    print("The word the is at position", result)

