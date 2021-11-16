from game import Game
from consts import *
import pygame as pg


game = Game(11)

run = True
while run:
    game.clock.tick(FPS)
    if game.in_game:
        run = game.run_game()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
    pg.display.flip()

pg.quit()
