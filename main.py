import pygame
import classes
import config as conf

# Инициализация pygame
pygame.init()
# Инициализация окна, и переменных цикла
sc = pygame.display.set_mode((conf.WIN_WIDTH, conf.WIN_HEIGHT))
pygame.display.flip()
pygame.display.set_caption(conf.WIN_NAME)
clock = pygame.time.Clock()
guns = [classes.Gun(sc, x, y) for x, y in conf.GUNS]
rep = 0
# Основной цикл
running = True
while running:
    # Зажатие кнопик
    if conf.TEST_MODE:
        mouse = pygame.mouse.get_pressed()
        if mouse[0]:
            if rep == conf.INTERVAL_PFPS:
                for gun in guns:
                    gun.shot_ball()
                    if len(gun.shoted_balls) > conf.MAX_BALLS_COUNT:
                        gun.shoted_balls = gun.shoted_balls[-conf.MAX_BALLS_COUNT:]
                rep = 0
            rep += 1
    # Обработчик событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEMOTION:
            for gun in guns:
                gun.update_gun()
        if event.type == pygame.MOUSEBUTTONDOWN:
            for gun in guns:
                gun.shot_ball()
        if event.type == pygame.KEYDOWN:
            for gun in guns:
                gun.shoted_balls = []

    # Отрисовка
    sc.fill(conf.COLOR_dark_grey)
    for gun in guns:
        gun.draw_gun()
        if len(gun.shoted_balls) != 0:
            i = 0
            while i < (len(gun.shoted_balls)):
                gun.shoted_balls[i].update_ball()
                gun.shoted_balls[i].draw_ball()
                if gun.shoted_balls[i].life > conf.MAX_LIFE:
                    gun.shoted_balls.pop(i)
                else:
                    i += 1
    # Кол-во шариков на экране
    csum = 0
    for gun in guns:
        csum += len(gun.shoted_balls)
    pygame.display.set_caption(str(len(guns)) + " ; " + str(csum))
    # Апдейт и следующий цикл
    pygame.display.flip()
    clock.tick(conf.FPS)

pygame.quit()