from draw_classes import Vector
from math import sqrt
import pygame as pg

def draw_triangle(surface, color, vectors):
    points = [(v.x, v.y) for v in vectors]
    pg.draw.polygon(surface, color, points)