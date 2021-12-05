from consts import *
from draw_classes import Vector as vec
import pygame as pg
from draw_funks import *
from game import Game
from button import Button


class Menu():
    def __init__(self):
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        self.clock = pg.time.Clock()
        self.play_button = Button((200, 250), 300, 100, 'Play', (305, 275), 65, self.create_game_and_run)
        self.size_inc_button = Button((457, 450), 50, 50, '+', (465, 441), 90, self.inc_size)
        self.size_dec_button = Button((457, 550), 50, 50, '-', (472, 541), 90, self.dec_size)
        self.change_mode_button = Button((350, 680), 150, 50, 'change', (360, 685), 50, self.change_mode)
        self.size = 4
        self.mode = 2

    def run_start_menu(self):
        run = True
        while run:
            self.clock.tick(FPS)
            mouse_pos = pg.mouse.get_pos()
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    run = False
                elif event.type == pg.MOUSEBUTTONDOWN:
                    if self.play_button.in_boards(mouse_pos):
                        run = self.play_button.click()
                    elif self.size_inc_button.in_boards(mouse_pos):
                        self.size_inc_button.click()
                    elif self.size_dec_button.in_boards(mouse_pos):
                        self.size_dec_button.click()
                    elif self.change_mode_button.in_boards(mouse_pos):
                        self.change_mode_button.click()
            self.screen.fill(WHITE)
            draw_text(self.screen, (200, 180), 'Hex Game', 90, BLACK)
            self.draw_settings()
            self.play_button.draw(self.screen)
            self.play_button.highlight(mouse_pos)
            self.size_inc_button.draw(self.screen)
            self.size_inc_button.highlight(mouse_pos)
            self.size_dec_button.draw(self.screen)
            self.size_dec_button.highlight(mouse_pos)
            self.change_mode_button.draw(self.screen)
            self.change_mode_button.highlight(mouse_pos)
            pg.display.flip()
        return run

    def draw_settings(self):
        draw_text(self.screen, (200, 500), str.format('Field size: {0}', self.size), 70, BLACK)
        if self.mode == 0:
            mode = 'Player1 vs Player2'
        elif self.mode == 1:
            mode = 'Player vs EazyComp'
        else:
            mode = 'Player vs HardComp'
        draw_text(self.screen, (50, 630), str.format('Mode: {0}', mode), 60, BLACK)

    def create_game_and_run(self):
        game = Game(self.size, self.screen, self.mode)
        return game.run_game()

    def inc_size(self):
        self.size = (self.size + 1) % 21
        if self.size < 3:
            self.size = 3

    def dec_size(self):
        self.size = (self.size - 1)
        if self.size < 3:
            self.size = 20

    def change_mode(self):
        self.mode = (self.mode + 1) % 3
