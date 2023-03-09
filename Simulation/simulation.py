from copy import deepcopy

from Traffic.Road.road import Road
from Traffic.Signal.signal import TrafficSignal
from Traffic.Vehicle.Generator.generator import Generator
from Traffic.Vehicle.vihicle_const import TRAFFIC_SIGNAL_TIME


class Simulation:
    def __init__(self):
        self.roads = []
        self.generators = []
        self.traffic_signals = []
        self.time = 0

    def create_road(self, start, end):
        road = Road(start, end)
        self.roads.append(road)
        return road

    def create_roads(self, road_list):
        for road in road_list:
            self.create_road(*road)

    def create_vehicle(self, vehicles):
        gen = Generator(self, vehicles)
        self.generators.append(gen)
        return gen

    def create_signal(self, roads):
        roads = [[self.roads[i] for i in road_group] for road_group in roads]
        sig = TrafficSignal(roads)
        self.traffic_signals.append(sig)
        return sig

    def update(self):
        for road in self.roads:
            road.update()

        for gen in self.generators:
            gen.update()

        for signal in self.traffic_signals:
            signal.update(self.time)

        for road in self.roads:
            if len(road.vehicles) == 0: continue
            vehicle = road.vehicles[0]
            if vehicle.x >= road.length:
                if vehicle.current_road_index + 1 < len(vehicle.path):
                    vehicle.current_road_index += 1
                    new_vehicle = deepcopy(vehicle)
                    new_vehicle.x = 0
                    next_road_index = vehicle.path[vehicle.current_road_index]
                    self.roads[next_road_index].vehicles.append(new_vehicle)
                road.vehicles.popleft()
        self.time += TRAFFIC_SIGNAL_TIME

    def run(self, steps):
        for _ in range(steps):
            self.update()
