from prac_09.car import Car
import random


class UnreliableCar(Car):

    def __init__(self, reliability, name, fuel):
        super().__init__(name, fuel)
        self.reliability = reliability

    def __str__(self):
        return f"{super().__str__()}, reliability:{self.reliability}"

    def drive(self, distance):
        reliability = random.randint(0, 100)
        if reliability < float(self.reliability):
            return super().drive(distance)




