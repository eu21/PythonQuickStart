def printName(name):
    print(name)

def inputName():
    name=input("Enter your name: ")
    return name

name = inputName()
printName("Hello "+name+"!")
