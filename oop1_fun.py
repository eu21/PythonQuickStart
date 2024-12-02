class Car():
    def __init__(self, color='noColor', brand='noBrand'):
        self.isRunning=False
        self.isDriving=False
        self.color=color
        self.brand=brand
        
    def startEngine(self):
        self.isRunning=True
    def startDriving(self):
        self.isDriving=True
        
    def stopEngine(self):
        self.isRunning=False
    def stopDriving(self):
        self.isDriving=True

car = Car("red", "BMW")

print(car.isRunning)
print(car.isDriving)
print(car.color)
print(car.brand)
