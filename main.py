import pygame
from parametrs import *
from sprites import Player


# игровое окно
pygame.init()  # запуск pygame
pygame.mixer.init()  # запуск работы звука

screen = pygame.display.set_mode((WIDTH, HEIGHT))  # размер дисплея
pygame.display.set_caption("Моя первая игра")  # заголовок
pygame.display.set_icon(icon)
clock = pygame.time.Clock()  # переменная для работы с частотой кадров


# группы спрайтов
players_sprites = pygame.sprite.Group()  # создаю группу спрайтов
player = Player()  # создаю спрайт героя
players_sprites.add(player)  # добавляю спрайт в группу

running = True  # переменная для запуска игрового цикла
while running:  # запуск игрового цикла
    # контроль FPS
    clock.tick(FPS)

    players_sprites.update()  # обновление спрайтов

    # отрисовка
    screen.fill(GREEN)
    players_sprites.draw(screen)  # отрисовка спрайтов на экране

    # после отрисовки, переворачиваем экран
    pygame.display.flip()

    # обработка событий
    for event in pygame.event.get():
        # проверка на закрытие игры
        if event.type == pygame.QUIT:
            running = False
        # дальнейшая логика
        # проверка на направление

    # Отрисовка
    # Визуалицая(сборка)
pygame.quit()

