import pygame
import config as conf
import math
from random import choice, randint


class Gun:
    def __init__(self, sc, x, y):
        self.sc = sc
        self.x = x
        self.y = y
        self.length = conf.GUN_LEN
        self.sec_gun_point_x = self.x + self.length
        self.sec_gun_point_y = self.y
        self.strong = conf.GUN_STRONG
        self.sin = 0
        self.cos = 0
        self.angel = 0
        self.shoted_balls = []
        self.gun = pygame.draw.line(sc, conf.GUN_COLOR, (self.x, self.y), (self.sec_gun_point_x, self.sec_gun_point_y),
                                    conf.GUN_WIDTH)

    def update_angel(self):
        mx, my = pygame.mouse.get_pos()
        a = mx - self.x
        b = my - self.y
        c = (a ** 2 + b ** 2) ** 0.5
        self.sin = a / c
        self.cos = b / c
        self.angel = abs(math.degrees(math.asin(self.sin)))

    def update_gun(self):
        self.update_angel()
        a = self.sin * self.length
        b = self.cos * self.length
        self.sec_gun_point_x = self.x + a
        self.sec_gun_point_y = self.y + b
        self.gun = pygame.draw.line(self.sc, conf.GUN_COLOR, (self.x, self.y),
                                    (self.sec_gun_point_x, self.sec_gun_point_y),
                                    conf.GUN_WIDTH)

    def draw_gun(self):
        self.gun = pygame.draw.line(self.sc, conf.GUN_COLOR, (self.x, self.y),
                                    (self.sec_gun_point_x, self.sec_gun_point_y),
                                    conf.GUN_WIDTH)

    def shot_ball(self):
        mx, my = pygame.mouse.get_pos()
        dx = (self.angel / 90) * self.strong / conf.FPS
        dy = ((90 - self.angel) / 90) * self.strong / conf.FPS
        dx = -dx if mx < self.x else dx
        dy = -dy if my < self.y else dy
        x = self.x
        y = self.y
        self.shoted_balls.append(CannonBall(self.sc, x, y, dx, dy))


class CannonBall:
    def __init__(self, screen, x, y, dx, dy):
        self.sc = screen
        self.x = x
        self.y = y
        self.dy = dy
        self.dx = dx
        self.life = 0
        self.g = conf.G
        self.r = conf.R
        self.color = conf.BALL_COLOR if not conf.RANDOM_COLOR else (randint(0, 255), randint(0, 255), randint(0, 255))
        self.ball = pygame.draw.circle(self.sc, self.color, (self.x, self.y), self.r)

    def update_ball(self):
        self.life += 1
        self.x += self.dx
        self.y += self.dy
        self.dy += self.g
        self.dx -= conf.AIR
        if self.y > conf.WIN_HEIGHT - self.r:
            self.dy = -abs(self.dy * conf.ELAST_COF)
            self.dx = self.dx * conf.FRICT_COF
        elif self.y - self.r <= 0:
            self.dy = abs(self.dy)
        if self.x < 0:
            self.dx = abs(self.dx)
            self.dx *= 0.9

        elif self.x > conf.WIN_WIDTH:
            self.dx = -abs(self.dx)
            self.dx *= 0.9

    def draw_ball(self):
        self.ball = pygame.draw.circle(self.sc, conf.COLOR_black, (self.x, self.y), self.r + 2)
        if conf.RANDOM_COLOR and conf.RANDOM_COLOR_ALLWAYS:
            self.ball = pygame.draw.circle(self.sc,
                                           self.color if not conf.RANDOM_COLOR else choice(
                                               list(conf.COLORS.values())),
                                           (self.x, self.y), self.r)
        else:
            self.ball = pygame.draw.circle(self.sc, self.color, (self.x, self.y), self.r)


class Target:
    pass
