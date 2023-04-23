import copy
import pygame as pg
from random import randint

print("Enter the value of the horizontal screen size")
width_count = int(input('L = '))


print("Enter the value of the vertical screen size")
height_count = int(input('H = '))

size = 10

resolution = width, height = width_count * size + 1, height_count * size + 1
FPS = 60

# creating a screen with a given resolution
screen = pg.display.set_mode(resolution)
clock = pg.time.Clock()

# random number generator to fill in
# 1 - painted cell
# 0 - empty
next_blocks_stage = [[0 for l in range(width_count)] for j in range(height_count)]
blocks = [[randint(0, 1) for l in range(width_count)] for j in range(height_count)]


def paint_block(field, pos):
    x, y = pos
    neighbors = 0
    for yS in range(y - 1, y + 2):
        for xS in range(x - 1, x + 2):
            if field[yS][xS] == 1:
                neighbors += 1

    if field[y][x]:
        neighbors -= 1
        if neighbors == 2 or neighbors == 3:
            return 1
        else:
            return 0
    else:
        if neighbors == 3:
            return 1
        else:
            return 0


while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            quit()

    screen.fill(pg.Color('black'))

    # grid
    [pg.draw.line(screen, (75, 75, 75), (x, 0), (x, height)) for x in range(0, width, size)]
    [pg.draw.line(screen, (75, 75, 75), (0, y), (width, y)) for y in range(0, height, size)]

    for x_block in range(1, width_count - 1):
        for y_block in range(1, height_count - 1):
            if blocks[y_block][x_block] == 1:
                pg.draw.rect(screen, (255, 255, 255), (x_block * size + 1, y_block * size + 1, size - 1, size - 1))
            next_blocks_stage[y_block][x_block] = paint_block(blocks, (x_block, y_block))

    blocks = copy.deepcopy(next_blocks_stage)

    pg.display.set_caption("FPS: " + str(int(clock.get_fps())))
    clock.tick(FPS)
    pg.display.flip()