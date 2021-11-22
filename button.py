from consts import *
from draw_classes import Vector as vec
import pygame as pg
from draw_funks import *


class Button:
    color = WHITE

    def __init__(self, pos, width, height, txt, txt_pos, txt_size, funk=lambda: None):
        self.height = height
        self.width = width
        self.text = txt
        self.funk = funk
        self.rect = pg.Rect(pos[0], pos[1], width, height)
        self.txt_pos = txt_pos
        self.txt_size = txt_size

    def highlight(self, mouse_pos):
        if self.in_boards(mouse_pos):
            self.color = YELLOW
        else:
            self.color = WHITE

    def in_boards(self, mouse_pos):
        if self.rect.x <= mouse_pos[0] <= self.rect.x + self.width:
            if self.rect.y <= mouse_pos[1] <= self.rect.y + self.height:
                return True
        return False

    def draw(self, screen):
        pg.draw.rect(screen, self.color, self.rect)
        draw_text(screen, self.txt_pos, self.text, self.txt_size, BLACK)

    def click(self):
        return self.funk()

