from Traffic.Simulation.simulation import Simulation
from Traffic.Visualization.visualization import Window

sim = Simulation()

n = 15
a = 2
b = 4
l = 300

# Nodes
WEST_RIGHT_START = (-b - l, a)
WEST_LEFT_START = (-b - l, -a)

SOUTH_RIGHT_START = (a, b + l)
SOUTH_LEFT_START = (-a, b + l)

EAST_RIGHT_START = (b + l, -a)
EAST_LEFT_START = (b + l, a)

NORTH_RIGHT_START = (-a, -b - l)
NORTH_LEFT_START = (a, -b - l)

WEST_RIGHT = (-b, a)
WEST_LEFT = (-b, -a)

SOUTH_RIGHT = (a, b)
SOUTH_LEFT = (-a, b)

EAST_RIGHT = (b, -a)
EAST_LEFT = (b, a)

NORTH_RIGHT = (-a, -b)
NORTH_LEFT = (a, -b)

# Roads
WEST_INBOUND = (WEST_RIGHT_START, WEST_RIGHT)
SOUTH_INBOUND = (SOUTH_RIGHT_START, SOUTH_RIGHT)
EAST_INBOUND = (EAST_RIGHT_START, EAST_RIGHT)
NORTH_INBOUND = (NORTH_RIGHT_START, NORTH_RIGHT)

WEST_OUTBOUND = (WEST_LEFT, WEST_LEFT_START)
SOUTH_OUTBOUND = (SOUTH_LEFT, SOUTH_LEFT_START)
EAST_OUTBOUND = (EAST_LEFT, EAST_LEFT_START)
NORTH_OUTBOUND = (NORTH_LEFT, NORTH_LEFT_START)

WEST_STRAIGHT = (WEST_RIGHT, EAST_LEFT)
SOUTH_STRAIGHT = (SOUTH_RIGHT, NORTH_LEFT)
EAST_STRAIGHT = (EAST_RIGHT, WEST_LEFT)
NORTH_STRAIGHT = (NORTH_RIGHT, SOUTH_LEFT)

sim.create_roads([
    WEST_INBOUND,
    SOUTH_INBOUND,
    EAST_INBOUND,
    NORTH_INBOUND,

    WEST_OUTBOUND,
    SOUTH_OUTBOUND,
    EAST_OUTBOUND,
    NORTH_OUTBOUND,

    WEST_STRAIGHT,
    SOUTH_STRAIGHT,
    EAST_STRAIGHT,
    NORTH_STRAIGHT
])
sim.create_vehicle(
    [
        [1, [1, 9, 7]],
        [1, [1, 9, 6]],
        [1, [0, 8, 6]],
        [1, [3, 11, 5]]

    ])

sim.create_signal([[0, 2], [1, 3]])

win = Window(sim)
win.zoom = 10
win.run(steps_per_update=5)
