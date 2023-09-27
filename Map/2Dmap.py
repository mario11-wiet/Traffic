import pygame as pg

from Map.map import Map
from Settings.default_map import default_map

PIXELS = default_map['pixels_per_unit']
WIDTH, HEIGHT = default_map['map_size']['width'] * PIXELS, default_map['map_size']['height'] * PIXELS
FPS = 60

WIN = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Traffic simulation")

GRASS_IMG = pg.image.load('../Assets/grass.png')
CAR_IMG = pg.image.load('../Assets/red_car.png')
ROAD_IMG = pg.image.load('../Assets/road.png')
CROSS_IMG = pg.image.load('../Assets/cross_road.png')

GRASS_BG = pg.transform.scale(GRASS_IMG, (WIDTH, HEIGHT))
CAR = pg.transform.scale(CAR_IMG, (PIXELS, PIXELS))
ROAD = pg.transform.scale(ROAD_IMG, (PIXELS, PIXELS))
CROSS_ROAD = pg.transform.scale(CROSS_IMG, (PIXELS, PIXELS))


def main():
    run = True
    clock = pg.time.Clock()

    maps = Map()
    maps.create_city()
    maps.print_city()

    while run:
        clock.tick(FPS)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False

        generate_map(maps)

        pg.display.update()

    pg.quit()


def generate_map(maps):
    WIN.blit(GRASS_BG, (0, 0))
    for i in range(maps.default_map['map_size']["width"]):
        for j in range(maps.default_map['map_size']["height"]):
            if maps.city[i][j].char == "+":
                WIN.blit(CROSS_ROAD, (i * PIXELS, j * PIXELS))
            elif maps.city[i][j].char == "|":
                WIN.blit(maps.city[i][j].image, (i * PIXELS, j * PIXELS))
            elif maps.city[i][j].char == "-":
                WIN.blit(maps.city[i][j].image, (i * PIXELS, j * PIXELS))


if __name__ == "__main__":
    main()
