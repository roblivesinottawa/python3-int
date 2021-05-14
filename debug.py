import pdb


class Vehicle:
    def __init__(self, make, year):
        pdb.set_trace()
        self.make = make
        self.year = year


car = Vehicle("Ford", 2012)
print(car.make)
