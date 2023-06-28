# Окно
WIN_WIDTH = 1000
WIN_HEIGHT = 700
WIN_NAME = "Пушка, хы"
# Цвета
COLORS = {"white": (246, 249, 255),
          "grey": (189, 189, 0),
          "red": (178, 2, 47),
          "yellow": (254, 208, 0),
          "cyan": (19, 181, 169),
          "blue": (62, 201, 193),
          "green": (143, 177, 65),
          "black": (47, 48, 40),
          "dark_grey": (53, 54, 46)}
COLOR_white = COLORS["white"]
COLOR_green = COLORS["green"]
COLOR_grey = COLORS["grey"]
COLOR_red = COLORS["red"]
COLOR_yellow = COLORS["yellow"]
COLOR_cyan = COLORS["cyan"]
COLOR_blue = COLORS["blue"]
COLOR_black = COLORS["black"]
COLOR_dark_grey = COLORS["dark_grey"]
# Игра
TEST_MODE = True
FPS = 100
# Шарик
RANDOM_COLOR = True
RANDOM_COLOR_ALLWAYS = False
BALL_COLOR = COLOR_blue
G = 9.8 / FPS
R = 25
AIR = 0.1
AIR = AIR / FPS
ELAST_COF = 0.8
FRICT_COF = 0.9
WALL_COF = 0.7
# Оптимизация
MAX_LIFE = 10
MAX_LIFE = MAX_LIFE * FPS
MAX_BALLS_COUNT = 100
# Пушка
GUN_LEN = 30
GUN_COLOR = COLOR_cyan
GUN_WIDTH = 5
GUN_STRONG = 1400
SHOTS_PER_SECOND = 10
INTERVAL_PFPS = FPS // SHOTS_PER_SECOND
# ПУШКИ
GUN_COUNT = 100

GUNS = []
floors = 2
first_y = WIN_HEIGHT * 0.9
second_y = WIN_HEIGHT * 0.1
third_y = WIN_HEIGHT // 2
# Создать все пушки
diaposon = WIN_WIDTH // (GUN_COUNT + 1)
ys = [first_y, second_y, third_y][:floors]
for y in (ys):
    for x in range(diaposon, WIN_WIDTH-1, diaposon):
        GUNS.append(
            (x, y)
        )
# Перерасчет
