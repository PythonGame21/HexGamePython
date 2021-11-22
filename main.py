from game import Game
from menu import Menu
from consts import *
import pygame as pg


pg.init()
menu = Menu()
run = True
while run:
    run = menu.run_start_menu()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
    pg.display.flip()

pg.quit()
