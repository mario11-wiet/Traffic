from numpy.random import randint

from Traffic.Vehicle.vehicle import Vehicle
from Traffic.Vehicle.vihicle_const import *


class Generator:
    def __init__(self, simulation, vehicles):
        self.simulation = simulation
        self.vehicles = vehicles
        self.last_added_time = 0
        self.upcoming_vehicle = self.generate_vehicle()

    def generate_vehicle(self):
        total = sum(pair[0] for pair in self.vehicles)
        r = randint(1, total + 1)
        for (weight, path) in self.vehicles:
            r -= weight
            if r <= 0:
                return Vehicle(path=path)

    def update(self):
        self.last_added_time += 1
        if self.last_added_time > TIME_TO_ADD:
            road = self.simulation.roads[self.upcoming_vehicle.path[0]]
            if len(road.vehicles) == 0 \
                    or road.vehicles[-1].x > S_0 + road.vehicles[-1].length:
                road.vehicles.append(self.upcoming_vehicle)
                self.last_added_time = 0
            self.upcoming_vehicle = self.generate_vehicle()
