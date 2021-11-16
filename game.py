from consts import *
from draw_funks import *
import pygame as pg


class Game:
    def __init__(self, size):
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        self.clock = pg.time.Clock()
        self.size = size
        self.move_count = 0
        self.in_game = False

    def run_start_menu(self):
        run = True
        while run:
            self.clock.tick(FPS)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    run = False
            self.screen.fill(BLUE)
            draw_triangle(self.screen, RED, [Vector(0, 0), Vector(200, 0), Vector(0, 200)])
            pg.display.flip()
        return run

    def handle_mouse_button_down(self, mouse_pos):
        pass

