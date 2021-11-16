from consts import *
from draw_classes import Vector as vec
from draw_funks import *
from state_class import State
import pygame as pg


class Game:
    def __init__(self, size):
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        self.clock = pg.time.Clock()
        self.size = size
        self.state = [[State.FREE for _ in range(self.size)] for __ in range(self.size)]
        self.hex_a = get_hex_a(size) * 0.995
        center = vec(350, 400)
        left_up_point = center + vec(-FIELD_R, 0).rotate(-60) + vec(0, -2 * FIELD_R)
        self.origin = vec(left_up_point.x + self.hex_a, left_up_point.y + self.hex_a * sqrt(3))
        self.move_count = 0
        self.in_game = True

    def run_game(self):
        run = True
        while run:
            self.clock.tick(FPS)
            mouse_pos = pg.mouse.get_pos()
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    run = False
                elif event.type == pg.MOUSEBUTTONDOWN:
                    self.do_move(mouse_pos)
            self.screen.fill(WHITE)
            draw_background_rhomb(self.screen)
            self.highlight(mouse_pos)
            self.draw_hexes()
            pg.display.flip()
        return run

    def do_move(self, mouse_pos):
        for a in range(self.size):
            for b in range(self.size):
                x, y = self.coords(a, b)
                if self.state[a][b] == State.LIGHT and is_in_hex(mouse_pos, x, y, self.hex_a):
                    if self.move_count % 2 == 0:
                        self.state[a][b] = State.P1
                    else:
                        self.state[a][b] = State.P2
                    self.move_count += 1
                    return

    def coords(self, a, b):
        x = self.origin.x + a * 1.5 * self.hex_a
        y = self.origin.y + (a + 2*b) * self.hex_a * sqrt(3)/2
        return int(x), int(y)

    def draw_hexes(self):
        for a in range(self.size):
            for b in range(self.size):
                x, y = self.coords(a, b)
                if self.state[a][b] == State.FREE:
                    draw_hex(self.screen, GRAY, vec(x, y), self.hex_a)
                elif self.state[a][b] == State.LIGHT:
                    if self.move_count % 2 == 0:
                        draw_hex(self.screen, PINK, vec(x, y), self.hex_a)
                    else:
                        draw_hex(self.screen, SKY_BLUE, vec(x, y), self.hex_a)
                elif self.state[a][b] == State.P1:
                    draw_hex(self.screen, RED, vec(x, y), self.hex_a)
                else:
                    draw_hex(self.screen, BLUE, vec(x, y), self.hex_a)

    def highlight(self, mouse_pos):
        for a in range(self.size):
            for b in range(self.size):
                x, y = self.coords(a, b)
                if self.state[a][b] == State.FREE and is_in_hex(mouse_pos, x, y, self.hex_a):
                    self.state[a][b] = State.LIGHT
                elif self.state[a][b] == State.LIGHT and not is_in_hex(mouse_pos, x, y, self.hex_a):
                    self.state[a][b] = State.FREE


