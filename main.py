from game import Game
from consts import *
import pygame as pg


game = Game(DEF_SIZE)

run = True
while run:
    game.clock.tick(FPS)
    if not game.in_game:
        run = game.run_start_menu()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
        elif event.type == pg.MOUSEBUTTONDOWN:
            print(pg.mouse.get_pos())
    pg.display.flip()

pg.quit()
