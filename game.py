from consts import *
from draw_classes import Vector as vec
from draw_funks import *
from state_class import State
from button import Button
import pygame as pg
from collections import deque


class Game:
    def __init__(self, size, screen, mode):
        self.screen = screen
        self.clock = pg.time.Clock()
        self.size = size
        self.state = [[State.FREE for _ in range(self.size)] for __ in range(self.size)]
        self.hex_a = get_hex_a(size)
        center = vec(350, 400)
        left_up_point = center + vec(-FIELD_R, 0).rotate(-60) + vec(0, -2 * FIELD_R)
        self.origin = vec(left_up_point.x + self.hex_a, left_up_point.y + self.hex_a * sqrt(3))
        self.move_count = 0
        self.mode = mode
        self.go_menu_button = Button((0, 0), 50, 50, '<', (7, -7), 90)
        self.end_game_button = Button((235, 400), 230, 70, 'Menu', (265, 405), 90)
        self.is_end = False
        self.winner = 0


    def run_game(self):
        run = True
        while run:
            self.clock.tick(FPS)
            mouse_pos = pg.mouse.get_pos()
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    run = False
                elif event.type == pg.MOUSEBUTTONDOWN:
                    if self.is_end:
                        if self.end_game_button.in_boards(mouse_pos):
                            return run
                    else:
                        if self.go_menu_button.in_boards(mouse_pos):
                            return run
                        self.do_move(mouse_pos)
            self.screen.fill(WHITE)
            draw_background_rhomb(self.screen)
            self.draw_hexes()
            self.go_menu_button.draw(self.screen)
            if not self.is_end:
                self.winner = self.check_win()
                if self.winner != 0:
                    self.is_end = True
            if self.is_end:
                self.show_end_game(self.winner, mouse_pos)
            else:
                self.go_menu_button.highlight(mouse_pos)
                self.highlight(mouse_pos)
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

    def check_win(self):
        for y in range(self.size):
            if self.state[0][y] == State.P1:
                if self.BFS_is_win((0, y), State.P1, (0, self.size - 1)):
                    return 1
        for x in range(self.size):
            if self.state[x][0] == State.P2:
                if self.BFS_is_win((x, 0), State.P2, (1, self.size - 1)):
                    return 2
        return 0

    def BFS_is_win(self, root, p, w_c):
        visited = [[False for _ in range(len(self.state[0]))] for __ in range(len(self.state))]
        visited[root[0]][root[1]] = True
        queue = deque([root])
        while queue:
            v = queue.popleft()
            for dx in range(-1, 2):
                for dy in range(-1, 2):
                    if dx == 0 and dy == 0 or abs(dx + dy) == 2:
                        continue
                    n_p = (v[0] + dx, v[1] + dy)
                    if self.in_bounds(n_p) and not visited[n_p[0]][n_p[1]] and self.state[n_p[0]][n_p[1]] == p:
                        if n_p[w_c[0]] == w_c[1]:
                            return True
                        visited[n_p[0]][n_p[1]] = True
                        queue.append(n_p)
        return False

    def in_bounds(self, pos):
        return 0 <= pos[0] < len(self.state) and 0 <= pos[1] < len(self.state[0])

    def shadow(self):
        shadow = pg.Surface((WIDTH, HEIGHT))
        shadow.set_alpha(200)
        self.screen.blit(shadow, (0, 0))

    def show_end_game(self, p, mouse_pos):
        self.shadow()
        res = 'RED' if p == 1 else 'BLUE'
        draw_text(self.screen, (160, 300), f'Player {res} win', 70, RED if p == 1 else BLUE)
        self.end_game_button.draw(self.screen)
        self.end_game_button.highlight(mouse_pos)
