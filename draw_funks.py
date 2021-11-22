from draw_classes import Vector as vec
from math import sqrt
from consts import *
import pygame as pg


def draw_triangle(surface, color, vectors):
    points = [(v.x, v.y) for v in vectors]
    pg.draw.polygon(surface, color, points)


def triangle_s(a, b, c):
    A = c.dist(b)
    B = a.dist(c)
    C = a.dist(b)
    p = (A+B+C)/2
    return sqrt(p*(p-A)*(p-B)*(p-C))


def draw_background_rhomb(surface):
    center = vec(350, 400)
    a = FIELD_R
    left_down_point = center + vec(-a, 0).rotate(-60)
    left_up_point = left_down_point + vec(0, -2*a)
    right_up_point = 2*center - left_down_point
    right_down_point = 2*center - left_up_point
    draw_triangle(surface, RED, [center, left_up_point, left_down_point])
    draw_triangle(surface, RED, [center, right_down_point, right_up_point])
    draw_triangle(surface, BLUE, [center, right_down_point, left_down_point])
    draw_triangle(surface, BLUE, [center, left_up_point, right_up_point])


def draw_hex(surface, color, pos_vec, a):
    x, y = pos_vec.x, pos_vec.y
    points = [(x-a/2, y-a*sqrt(3)/2),
              (x+a/2, y-a*sqrt(3)/2),
              (x+a, y),
              (x+a/2, y+a*sqrt(3)/2),
              (x-a/2, y+a*sqrt(3)/2),
              (x-a, y)]
    pg.draw.polygon(surface, color, points)
    pg.draw.polygon(surface, YELLOW, points, 3)


def get_hex_a(size):
    center = vec(350, 400)
    left_down_point = center + vec(-FIELD_R, 0).rotate(-60)
    right_up_point = 2 * center - left_down_point
    field_width = right_up_point.x - left_down_point.x
    a2_count = (size + 1)//2
    a1_count = size // 2 + (0.5 if size % 2 == 0 else 0)
    return field_width / (a2_count * 2 + a1_count)


def is_in_hex(pos, x, y, a):
    point = vec(pos)
    points = [(x + a, y), (x + a / 2, y + a * sqrt(3) / 2),
              (x - a / 2, y + a * sqrt(3) / 2), (x - a, y),
              (x - a / 2, y - a * sqrt(3) / 2), (x + a / 2, y - a * sqrt(3) / 2)]
    points = list(map(vec, points))
    sum = 0
    for i in range(-1, 5):
        sum += triangle_s(points[i], points[i + 1], point)
    S = a * a * 3 * sqrt(3) / 2
    return abs(S - sum) < 1e-5

def draw_text(screen, pos, text, size, color):
    font = pg.font.Font(None, size)
    text = font.render(text, True, color)
    screen.blit(text, pos)
