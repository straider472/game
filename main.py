import pygame

# параметры игры
WIDTH = 500  # ширина игрового окна
HEIGHT = 500  # высота игрового окна
FPS = 30  # частота кадров в секунду

# игровое окно
pygame.init()  # запуск pygame
pygame.mixer.init()  # запуск работы звука
screen = pygame.display.set_mode((WIDTH, HEIGHT))  # размер дисплея
pygame.display.set_caption("Моя первая игра")  # заголовок
clock = pygame.time.Clock()  # переменная для работы с частотой кадров

running = True  # переменная для запуска игрового цикла
while running:  # запуск игрового цикла
    pass
    # Ввод процесса(события)
    # Обновление
    # Визуалицая(сборка)

