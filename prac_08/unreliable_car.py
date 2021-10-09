from prac_08.car import Car
import random


class UnreliableCar(Car):

    def __init__(self, name, fuel, reliability):
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        random_number = random.randint(1, 100)
        print(random_number)
        if self.reliability > random_number:
            distance_driven = super().drive(distance)
        else:
            distance_driven = 0
        return distance_driven
