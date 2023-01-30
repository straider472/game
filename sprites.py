import pygame
from parametrs import *

class Player(pygame.sprite.Sprite):
    'Класс, описывающий главного героя'
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))  # создадим поверхность 50 на 50
        self.image.fill(RED)
        self.rect = self.image.get_rect()  # прямоугольник спрайта
        self.rect.center = (WIDTH / 2, HEIGHT / 2)  # место создания спрайта
        self.direction = "RIGHT"

    def update(self):
        if self.direction == "LEFT":
            self.rect.right -= 10
        elif self.direction == "TOP":
            self.rect.top -= 10
        elif self.direction == "RIGHT":
            self.rect.right += 10
        elif self.direction == "BOTTOM":
            self.rect.top += 10

        # обработка выхода за границы экрана
        if self.rect.right > WIDTH or self.rect.right < 0\
                or self.rect.top > HEIGHT or self.rect.top < 0:
            if self.rect.right > WIDTH:
                self.rect.right = 0
            elif self.rect.right < 0:
                self.rect.right = WIDTH
            elif self.rect.top > HEIGHT:
                self.rect.top = 0
            elif self.rect.top < 0:
                self.rect.top = HEIGHT