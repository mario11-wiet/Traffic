from Settings.default_map import default_map

import pygame as pg

PIXELS = default_map['pixels_per_unit']

ROAD_IMG = pg.image.load('../Assets/road.png')
ROAD = pg.transform.scale(ROAD_IMG, (PIXELS, PIXELS))

class Road:
    def __init__(self, max_speed):
        self.speed = max_speed
        self.available = True
        self.road = []
        self.traffic_lights = False
        self.char = " "
        self.driving_direction = None
        self.image = None

    def __str__(self):
        return self.char


class Map:
    def __init__(self, city_map=default_map):
        self.default_map = city_map
        self.city = None

    def create_city(self):
        self.city = [[Road(self.default_map['max_speed']) for _ in range(self.default_map['map_size']["width"])]
                     for _ in range(self.default_map['map_size']["height"])]
        for road in self.default_map["road"]:
            self.create_road(road)

        self.create_crossroad()

    def create_crossroad(self):
        for i in range(self.default_map['map_size']["width"]):
            for j in range(self.default_map['map_size']["height"]):
                if len(self.city[i][j].road) > 1:
                    self.city[i][j].char = "+"
                    print(i, j, self.city[i][j].road)

    def create_road(self, road_number):
        road = self.default_map["road"][road_number]
        start = road["start"]
        end = road["end"]
        char = self.draw_road(start, end)
        if start[0] == end[0]:
            for i in range(start[1], end[1]):
                for j in range(start[0], start[0] + road["right_lane"]):
                    self.city[i][j].char = char
                    self.city[i][j].road.append(road_number)
                    self.city[i][j].driving_direction = "right"
                    self.city[i][j].image = pg.transform.rotate(ROAD, 90)
                for j in range(start[0] + road["right_lane"], start[0] + road["right_lane"] + road["left_lane"]):
                    self.city[i][j].char = char
                    self.city[i][j].road.append(road_number)
                    self.city[i][j].driving_direction = "left"
                    self.city[i][j].image = pg.transform.rotate(ROAD, 270)

        if start[1] == end[1]:
            for i in range(start[0], end[0]):
                for j in range(start[1], start[1] + road["right_lane"]):
                    self.city[j][i].char = char
                    self.city[j][i].road.append(road_number)
                    self.city[j][i].driving_direction = "bottom"
                    self.city[j][i].image = pg.transform.rotate(ROAD, 180)
                for j in range(start[1] + road["right_lane"], start[1] + road["right_lane"] + road["left_lane"]):
                    self.city[j][i].char = char
                    self.city[j][i].road.append(road_number)
                    self.city[j][i].driving_direction = "top"
                    self.city[j][i].image = ROAD

    def draw_road(self, start, end):
        return "|" if start[0] == end[0] else "-"

    def print_city(self):
        for i in range(self.default_map['map_size']["width"]):
            for j in range(self.default_map['map_size']["height"]):
                print(self.city[i][j], end='')
            print('\n', end='')


maps = Map()
maps.create_city()
maps.print_city()
