class Dog():
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def bark(self):
        print(self.name, "is barking.")
        
    def addYear(self):
        self.age += 1
    
    def getDescription(self):
        print(self.name, " is ", self.age, " years old.")
        
class Poodle(Dog):
    def __init__(self, name, age, color, weight):
        self.name=name
        self.age=age
        self.color=color
        self.weight=weight
    
    def bark(self, manner="energetically"):
        print(f"{self.name} is barking {manner}.")
    
    def getDescription(self):
        print(f"{self.name} is a {self.age} years old {self.color} poodle and weights {self.weight} pounds.")
        
# fido = Dog("Fido", 2)
# print(fido.name)
# print(fido.age)
# fido.bark()

ella = Poodle("Ella", 3, "white", 6)
# print(ella.name)
# print(ella.age)
# print(ella.color)
ella.bark()
ella.getDescription()
ella.addYear()
ella.getDescription()