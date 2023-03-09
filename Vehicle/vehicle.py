import random

import numpy as np

from Traffic.Vehicle.vihicle_const import *


class Vehicle:
    def __init__(self, path):
        self.v_max = V_MAX
        self.v = self.v_max
        self.a_max = A_MAX
        self.a = 0
        self.b_max = B_MAX
        self.path = path
        self.current_road_index = 0
        self.length = random.randrange(1, 10)
        self.color = (random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255))

        self.x = 0
        self.stopped = False

    def update(self, lead):
        if self.v + self.a * TIME_SIMULATION < 0:
            self.x -= 1 / 2 * self.v * self.v / self.a
            self.v = 0
        else:
            self.v += self.a * TIME_SIMULATION
            self.x += self.v * TIME_SIMULATION + self.a * TIME_SIMULATION * TIME_SIMULATION / 2

        alpha = 0
        if lead:
            delta_x = lead.x - self.x - lead.length
            delta_v = self.v - lead.v

            alpha = (S_0 + max(0, self.v + delta_v * self.v / (2 * np.sqrt(self.a_max * self.b_max)))) / delta_x

        self.a = self.a_max * (1 - (self.v / self.v_max) ** 4 - alpha ** 2)

        if self.stopped:
            self.a = -self.b_max * self.v / self.v_max

    def stop(self):
        self.stopped = True

    def unstop(self):
        self.stopped = False

    def slow(self, v):
        self.v_max = v

    def unslow(self):
        self.v_max = V_MAX
