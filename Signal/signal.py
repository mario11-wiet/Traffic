class TrafficSignal:
    def __init__(self, roads):
        self.roads = roads
        self.cycle = [(False, True), (True, False)]
        self.slow_distance = 50
        self.slow_factor = 0.4
        self.stop_distance = 10
        self.current_cycle_index = 0
        self.last_t = 0
        for i in range(len(self.roads)):
            for road in self.roads[i]:
                road.set_traffic_signal(self, i)

    @property
    def current_cycle(self):
        return self.cycle[self.current_cycle_index]

    def update(self, time):
        cycle_length = 30
        k = (time // cycle_length) % 2
        self.current_cycle_index = int(k)
