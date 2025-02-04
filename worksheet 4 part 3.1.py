class Car:

    def __init__(self, __year_model,__make,__speed = 0):
            self.year_model = __year_model
            self.make = __make
            self.speed = __speed
    def accelerate(self):
        self.speed += 5
    def brake(self):
        self.speed -= 5
    def get_speed(self):
        return self.speed

    def __str__(self) -> str:
        return "year: {}, make: {}, speed: {}".format(self.year_model, self.make, self.speed)
    def __repr__(self) -> str:
        return "year: {}, make: {}, speed: {}".format(self.year_model, self.make, self.speed)

Car1 = Car("1992", "maestro")
Car1.accelerate()
print(Car1.get_speed())
Car1.accelerate()
print(Car1.get_speed())
Car1.accelerate()
print(Car1.get_speed())
Car1.accelerate()
print(Car1.get_speed())
Car1.accelerate()
print(Car1.get_speed())
Car1.brake()
print(Car1.get_speed())
Car1.brake()
print(Car1.get_speed())
Car1.brake()
print(Car1.get_speed())
Car1.brake()
print(Car1.get_speed())
Car1.brake()
print(Car1.get_speed())

