from scipy.spatial import distance
from collections import deque

from Traffic.Vehicle.vihicle_const import V_MAX


class Road:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.vehicles = deque()
        self.length = distance.euclidean(self.start, self.end)
        self.has_traffic_signal = False
        self.traffic_signal = None
        self.traffic_signal_group = None

    def set_traffic_signal(self, signal, group):
        self.traffic_signal = signal
        self.traffic_signal_group = group
        self.has_traffic_signal = True

    @property
    def traffic_signal_state(self):
        if self.has_traffic_signal:
            i = self.traffic_signal_group
            return self.traffic_signal.current_cycle[i]
        return True

    def update(self):
        n = len(self.vehicles)

        if n > 0:
            self.vehicles[0].update(None)
            for i in range(1, n):
                lead = self.vehicles[i - 1]
                self.vehicles[i].update(lead)

            if self.traffic_signal_state:
                self.vehicles[0].unstop()
                for vehicle in self.vehicles:
                    vehicle.unslow()
            else:
                if self.vehicles[0].x >= self.length - self.traffic_signal.slow_distance:
                    self.vehicles[0].slow(self.traffic_signal.slow_factor * V_MAX)
                if self.length - self.traffic_signal.stop_distance <= \
                        self.vehicles[0].x <= self.length - self.traffic_signal.stop_distance / 2:
                    self.vehicles[0].stop()
